
# Import the necessary libraries
import pytest
from your_project.components import YourComponentName
from your_project.models import InputBaseModel, OutputBaseModel
from your_project import config

# Define test cases with mocked input and expected output data
test_cases = [
    {
        "input": InputBaseModel(
            field1="sample_value1",
            field2="sample_value2",
        ),
        "output": OutputBaseModel(
            result_field="sample_result",
        )
    },
    # Add more test cases or edge cases
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("test_case", test_cases)
def test_your_component_name(test_case):
    # Initialize the component with its configuration
    component = YourComponentName(config.YOUR_COMPONENT_NAME)

    # Call the component's transform() method using the mocked input
    result = component.transform(test_case["input"])

    # Assert that the output matches the expected output
    assert result == test_case["output"]

    # Include error handling and edge case scenarios, if applicable
    # Example: test with invalid input
    with pytest.raises(ValueError):
        invalid_input = InputBaseModel(field1="invalid_value1", field2="invalid_value2")
        component.transform(invalid_input)
