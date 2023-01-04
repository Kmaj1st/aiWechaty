# aiWechaty
Wechaty that is combined with language models and ChatGPT (Sorry for my miserable buggy and inconvenient code)
You can have a chatbot with language models!

Used: 
Wechaty https://wechaty.js.org/
revChatGPT https://github.com/acheong08/ChatGPT
Bloom https://huggingface.co/bigscience/bloom
OpenAI https://openai.com/
源(Yuan) https://air.inspur.com/example

1. npm 
Install node.js, https://nodejs.org/en/download/package-manager/
run:
npm init
npm install wechaty

2. pip
run:
pip install requests FastAPI emoji 
pip install openai #If will you use OpenAI
pip install --upgrade revChatGPT #See https://github.com/acheong08/ChatGPT for any question about configuring ChatGPT
pip install uvicorn #If you use ChatGPT

3. config(not necessary)
config.json
Set "session_token" cookie on ChatGPT website in config.json 
	"session_token": "<YOUR_TOKEN>"
And you can also set your language. I don't really know the effect of it.

config.py
Other language models:
    Bloom: https://huggingface.co/bigscience/bloom
    blmKey = {"Authorization": "<YOUR_TOKEN>"}
    
    OpenAI: https://beta.openai.com/account/api-keys
    openai_api_key = "<YOUR_API_KEY>"
    
    源(Yuan): https://air.inspur.com/example
    yuan_account = "<YOUR_ACCOUNT>"
    yuan_phone = "<YOUR_PHONE>"
    
4. run
npm start #run the bot and scan to login
uvicorn GPT:app #if you are using ChatGPT
