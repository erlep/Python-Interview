#!/usr/bin/env python

# Python code running in VS Code terminal but throwing error in output tab - https://bit.ly/3M4es83
# vscode-code-runner output utf8 chars incorrect https://bit.ly/46U4sGC
import emoji

print(emoji.emojize('I :red_heart:  Python!'))

# {
#     "code-runner.runInTerminal": true
# }

# {
#     "code-runner.executorMap": {
#         "python": "set PYTHONIOENCODING=utf8 && python"
#     }
# }