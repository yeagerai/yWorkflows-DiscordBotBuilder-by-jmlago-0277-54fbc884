
import os
from typing import Optional

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import openai

from core.abstract_component import AbstractComponent


class BotGeneratorInputDict(BaseModel):
    master_prompt: str


class BotGeneratorOutputDict(BaseModel):
    source_code: str
    total_tokens_used: int
    model_response: str
    internal_status: int


class BotGenerator(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.openai_api_key: Optional[str] = os.environ.get(
            yaml_data["parameters"]["openai_api_key"]
        )
        self.master_prompt: str = yaml_data["parameters"]["master_prompt"]

    def transform(
        self, args: BotGeneratorInputDict
    ) -> BotGeneratorOutputDict:
        openai.api_key = self.openai_api_key
        print(f"Executing the transform of the {type(self).__name__} component...")

        o_model = "gpt-4"
        o_model_pricing_every_1000 = 0.03

        completion = openai.ChatCompletion.create(
            model=o_model,
            messages=[
                {"role": "system", "content": self.master_prompt},
                {"role": "user", "content": args.master_prompt},
            ],
        )

        print(
            f"Total spent by {type(self).__name__} using the {o_model}: {completion.usage.total_tokens} tokens for {completion.usage.total_tokens*o_model_pricing_every_1000/1000} $"
        )

        try:
            response = (
                completion.choices[0].message.content.split("