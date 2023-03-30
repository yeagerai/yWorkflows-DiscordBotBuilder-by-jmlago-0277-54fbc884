
import pytest
import openai
from unittest.mock import patch, MagicMock

from your_component_path import CreateSlashCommands, CreateSlashCommandsInputDict, CreateSlashCommandsOutputDict

test_data = [
    (
        CreateSlashCommandsInputDict(
            master_prompt="Python Development",
            list_generated_workflows=["Example Workflow 1", "Example Workflow 2"]
        ),
        CreateSlashCommandsOutputDict(
            source_code="mocked source code"
        )
    ),
    (
        CreateSlashCommandsInputDict(
            master_prompt="Web Development",
            list_generated_workflows=["Example Workflow 3", "Example Workflow 4"]
        ),
        CreateSlashCommandsOutputDict(
            source_code="mocked source code"
        )
    )
]

@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_transform(input_data, expected_output):
    with patch("your_component_path.CreateSlashCommands._read_yaml_config", lambda self: {"parameters": {"master_prompt": "mock_parameter"}}):
        with patch("your_component_path.CreateSlashCommands.component_configuration_path", lambda self: "config.yml"):
            with patch("your_component_path.CreateSlashCommands.openai_api_key", new_callable=PropertyMock) as mock_openai_api_key:
                mock_openai_api_key.return_value = "mocked_api_key"

                with patch("your_component_path.CreateSlashCommands.transform.openai") as mock_openai:
                    mock_openai.ChatCompletion.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content="mocked source code"))])
                    create_slash_commands = CreateSlashCommands()

                    # Call the component's transform() method
                    output_data = create_slash_commands.transform(input_data)

                    # Assert that the output matches the expected output
                    assert output_data == expected_output
