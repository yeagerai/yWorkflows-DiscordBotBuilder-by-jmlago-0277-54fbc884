
import os
from typing import List, Optional

import yaml
import openai
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class CreateSlashCommandsInputDict(BaseModel):
    master_prompt: str
    list_generated_workflows: List[str]


class CreateSlashCommandsOutputDict(BaseModel):
    source_code: str


class CreateSlashCommands(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.master_prompt: str = yaml_data["parameters"]["master_prompt"]
        self.openai_api_key: Optional[str] = os.environ.get("OPENAI_API_KEY")

    def transform(
        self, args: CreateSlashCommandsInputDict
    ) -> CreateSlashCommandsOutputDict:

        openai.api_key = self.openai_api_key

        command_functions = []

        for workflow in args.list_generated_workflows:
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.master_prompt},
                    {"role": "user", "content": f"Create a command function for {workflow}"}
                ]
            )

            command_function = (
                completion.choices[0].message.content.split("