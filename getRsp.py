import json
from os.path import exists
from os import getenv

from revChatGPT.ChatGPT import Chatbot

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
                prompt, conversation_id=bot.config.get("conversation"))
                return(message)
            except Exception as exc:
                return("Something went wrong! exc:"+ str(exc))
