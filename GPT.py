import json
import re
import os
from os.path import exists
from os import getenv

from revChatGPT.ChatGPT import Chatbot
from fastapi import FastAPI

cvrFile = 'cvr.txt'
app = FastAPI()

def getResponse(bot, prompt):
        if (prompt=="favicon.ico") : return        
        if prompt.startswith("!"):
            if prompt == "!help":
                return(
"!help - Show this message %0a!reset - Forget the current conversation %0a"+
"!refresh - Refresh the session authentication %0a"+
"!config - Show the current configuration %0a"+
"!rollback x - Rollback the conversation (x being the number of messages to rollback) %0a"+
"!exit - Exit the program"
                ,
                )
                
            elif prompt == "!reset":
                bot.reset_chat()
                return("Chat session reset.")
                
            elif prompt == "!refresh":
                bot.refresh_session()
                return("Session refreshed.\n")
                
            elif prompt == "!config":
                return(json.dumps(bot.config, indent=4))
                
            elif prompt.startswith("!rollback"):
                # Default to 1 rollback if no number is specified
                try:
                    rollback = int(prompt.split(" ")[1])
                except IndexError:
                    rollback = 1
                bot.rollback_conversation(rollback)
                return(f"Rolled back {rollback} messages.")
                
            elif prompt.startswith("!setconversation"):
                try:
                    bot.config["conversation"] = prompt.split(" ")[1]
                    return("Conversation has been changed")
                except IndexError:
                    return("Please include conversation UUID in command")
        else:
            try:
                message = bot.ask(
                prompt.replace("%SLASH%", "/"), conversation_id=bot.config.get("conversation"))
                return(message)
            except Exception as exc:
                return("Something went wrong! exc:"+ str(exc))

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

bot = Chatbot(configure())
readCvr(bot)

@app.get("/{prompt}")
def read_prompt(prompt: str):
    print(prompt) 
    prompt = prompt.replace("/", "%SLASH%")
    response = getResponse(bot, prompt)
    saveCvr(response)
    return re.sub(r'\r?\n', '', response["message"])
