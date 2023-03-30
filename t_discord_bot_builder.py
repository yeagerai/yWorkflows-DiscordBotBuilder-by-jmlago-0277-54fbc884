
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from discord_bot_builder import DiscordBotBuilder, DiscordBotBuilderIn, DiscordBotBuilderOut, SlashCommand

client = TestClient(DiscordBotBuilder)

test_cases = [
    (
        DiscordBotBuilderIn(SlashCommandsList=[
            SlashCommand(command="!hello", description="Say hello"),
            SlashCommand(command="!goodbye", description="Say goodbye")
        ]),
        {"bot_py_file": "test content", "commands_py_file": "test content"}
    ),
    (
        DiscordBotBuilderIn(SlashCommandsList=[]),
        {"bot_py_file": "test content", "commands_py_file": "test content"}
    ),
]

def mock_transform(args, callbacks):
    for case in test_cases:
        if args == case[0]:
            return case[1]
    raise Exception("Failed to find matching test case.")

DiscordBotBuilder.transform = mock_transform

@pytest.mark.parametrize(
    "input_data, expected_output",
    [test_case for test_case in test_cases],
)
def test_transform(input_data, expected_output):
    response = client.post("/transform/", json=input_data.dict())

    assert response.status_code == 200

    output = response.json()
    assert output == expected_output

def test_bad_input():
    with pytest.raises(ValidationError):
        DiscordBotBuilderIn(SlashCommandsList=[
            {"bad_key": "invalid_data"}
        ])
