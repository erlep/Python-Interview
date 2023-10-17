#!/usr/bin/env python

# Python code running in VS Code terminal but throwing error in output tab - https://bit.ly/3M4es83
# vscode-code-runner output utf8 chars incorrect https://bit.ly/46U4sGC

# https://pypi.org/project/emoji   https://www.webfx.com/tools/emoji-cheat-sheet
# https://carpedm20.github.io/emoji/
import emoji

print(emoji.emojize('I :red_heart:  Python!'))

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', language='alias'))
print(emoji.demojize('Python is 👍'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
print(emoji.is_emoji("👍"))


print(emoji.emojize('Flag Czechia :flag_czechia:')) # nefunguje
print(emoji.emojize('Flag Czechia :Czechia:'))
print(emoji.emojize('Python is :thumbs_up:'))
first_token = next(emoji.analyze('Python is 👍'))
print('first_token',first_token)

# {
#     "code-runner.runInTerminal": true
# }

# {
#     "code-runner.executorMap": {
#         "python": "set PYTHONIOENCODING=utf8 && python"
#     }
# }
