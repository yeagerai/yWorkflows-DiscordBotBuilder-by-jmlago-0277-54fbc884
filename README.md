
# DiscordBotBuilder

The DiscordBotBuilder is a Yeager Workflow for creating a Discord bot with  user-defined slash commands. It takes a list of slash commands and their  descriptions as input, and comprises of three components: BotGenerator,  GenerateWorkflows, and CreateSlashCommands. BotGenerator uses GPT-4 and a  master_prompt parameter to create a bot.py file with the Discord bot's source  code. GenerateWorkflows iterates over the provided slash commands, invoking  WorkflowCreator.transform(args, callbacks) for each command and passing  the workflow description in args. Lastly, CreateSlashCommands leverages GPT-4  and a master_prompt parameter to generate a commands.py file with the slash  commands implemented as discord.py functions, with each function calling the  respective workflow's transform method.

## Initial generation prompt
A workflow called DiscordBotBuilder with input: a list of slash commands and their descriptions. The workflow should have 3 components. First the BotGenerator that uses GPT-4 and a master_prompt parameter to create a bot.py file with a Discord bot's source code. Then the GenerateWorkflows that iterates over user-defined slash commands, call WorkflowCreator.transform(args, callbacks) for each command, and pass in the workflow description as args. Finally, the CreateSlashCommands that uses GPT-4 and a master_prompt parameter to create a commands.py file with slash commands as discord.py functions. Each function should call the generated workflow's transform function.

## Authors: 
- yWorkflows
- jmlago#0277
        