
# CreateSlashCommands

The CreateSlashCommands component employs GPT-4 and a master_prompt parameter to generate the commands.py file containing the slash commands as discord.py functions, where each function calls the corresponding workflow's transform function.

## Initial generation prompt
description: "The CreateSlashCommands component employs GPT-4 and a master_prompt\
  \  parameter to generate the commands.py file containing the slash commands  as\
  \ discord.py functions, where each function calls the corresponding  workflow's\
  \ transform function. Inputs and Outputs are: Input:\n  - Master_Prompt (text)\n\
  \  - ListGeneratedWorkflows\nOutput:\n  - Source Code: (Generated commands.py)\n"
name: CreateSlashCommands


## Transformer breakdown
- Load GPT-4 model with helper functions
- Process the input, Master_Prompt and ListGeneratedWorkflows
- For each workflow in ListGeneratedWorkflows, create a corresponding command function using GPT-4 and the master_prompt
- Write the generated command functions to commands.py
- Return the Source_Code as output

## Parameters
[{'default_value': '', 'description': 'The master prompt that GPT-4 will utilize', 'name': 'master_prompt', 'type': 'text'}]

        