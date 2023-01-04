from revChatGPT.ChatGPT import Chatbot
import json
# Get config
config = open("config.json", "r").read()
config = json.loads(config)
# Create a chatbot object
chatbot = Chatbot(config)

chatbot.refresh_session()

# Get a response
response = chatbot.ask("What is an egg?")

conversation = response['conversation_id']
parent_id = response['parent_id']
message = response['message']
print(message)

del chatbot

chatbot = Chatbot(config)
chatbot.conversation_id = conversation
chatbot.parent_id = parent_id
response = chatbot.ask("continue")
message = response['message']
print(message)
