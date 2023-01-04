import json
import re
import os
from os.path import exists
from os import getenv


from revChatGPT.ChatGPT import Chatbot

from fastapi import FastAPI
from getRsp import getResponse
cvrFile = 'cvr.txt'
app = FastAPI()

def get_input(prompt):
    print(prompt, end="")
    user_input = input()
    return(user_input)


def configure():
    config_files = ["config.json"]
    xdg_config_home = getenv("XDG_CONFIG_HOME")
    if xdg_config_home:
        config_files.append(f"{xdg_config_home}/revChatGPT/config.json")
    user_home = getenv("HOME")
    if user_home:
        config_files.append(f"{user_home}/.config/revChatGPT/config.json")

    config_file = next((f for f in config_files if exists(f)), None)
    if config_file:
        with open(config_file, encoding="utf-8") as f:
            config = json.load(f)
    else:
        print("No config file found.")
        raise Exception("No config file found.")
    return config

def saveCvr(response):
    with open(cvrFile, 'w') as f_out:
        print(response['conversation_id']+"=Conversation")
        f_out.write(response['conversation_id']+'\n')
        print(response['parent_id']+"=Parent")
        f_out.write(response['parent_id'])

def readCvr(bot):
    if os.path.exists(cvrFile):
        with open(cvrFile, 'r') as f:
            lines = [line.strip() for line in f]
            bot.conversation_id = lines[0]
            bot.parent_id = lines[1]
    else:
        print("No conversation save file found. Will be created after your first conversation.")

   


def chatGPT_main():
    print("Logging in...")
    while True:
        prompt = get_input("\nYou:")
        if prompt == "!exit" : return('break')
        print(getResponse(bot, prompt)["message"])


bot = Chatbot(configure())
readCvr(bot)

@app.get("/{prompt}")
def read_prompt(prompt: str):
    print(prompt)
    response = getResponse(bot, prompt)
    print(response)
    saveCvr(response)
    return re.sub(r'\r?\n', '', response["message"])
def main():
    chatGPT_main()


if __name__ == "__main__":
    main()
