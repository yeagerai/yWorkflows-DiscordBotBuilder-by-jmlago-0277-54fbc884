
# GenerateWorkflows

The GenerateWorkflows component iterates over the user-defined slash commands, invoking WorkflowCreator.transform(args, callbacks) with the workflow description as args for each command.

## Initial generation prompt
description: "The GenerateWorkflows component iterates over the user-defined slash\
  \  commands, invoking WorkflowCreator.transform(args, callbacks) with the  workflow\
  \ description as args for each command. Inputs and Outputs are: Input:\n  - Slash\
  \ Commands and Descriptions\nOutput:\n  - List of Generated Workflows for Each Command\n"
name: GenerateWorkflows


## Transformer breakdown
- Iterate over the user-defined slash commands and their descriptions
- For each command, invoke WorkflowCreator.transform(args, callbacks) with the workflow description as args
- Collect the generated workflows in a list
- Return the list of generated workflows

## Parameters
[]

        