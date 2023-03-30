
import typing
from typing import List
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class SlashCommand(BaseModel):
    command: str
    description: str


class DiscordBotBuilderIn(BaseModel):
    SlashCommandsList: List[SlashCommand]


class DiscordBotBuilderOut(BaseModel):
    bot_py_file: str
    commands_py_file: str


class DiscordBotBuilder(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: DiscordBotBuilderIn, callbacks: typing.Any
    ) -> DiscordBotBuilderOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        bot_py_file = results_dict["bot_py_file"].content
        commands_py_file = results_dict["commands_py_file"].content

        out = DiscordBotBuilderOut(
            bot_py_file=bot_py_file,
            commands_py_file=commands_py_file
        )

        return out

load_dotenv()
discord_bot_builder_app = FastAPI()


@discord_bot_builder_app.post("/transform/")
async def transform(
    args: DiscordBotBuilderIn,
) -> DiscordBotBuilderOut:
    discord_bot_builder = DiscordBotBuilder()
    return await discord_bot_builder.transform(args, callbacks=None)

