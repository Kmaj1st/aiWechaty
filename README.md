# aiWechaty<br /> 
This one is only built and tested with wechaty-puppet-whatsapp, some functions may be invalid and if you change the puppet.<br /> 
Wechaty that is combined with language models and ChatGPT (Sorry for my miserable buggy and inconvenient code, someone help me fix my code)<br /> 
You can have a chatbot with language models!<br /> 
<br /> 
<br /> 
Send messages to the bot and it shall reply you.<br /> 
To use ChatGPT, send "::YOUR_TEXT,." to the bot.<br /> 
<br /> 
<br /> 
Features:<br /> 
1. Talk to you<br />
2. "Broken sentence"-combining <br /> 
3. It is cool.<br /> 
<br /> 
Used: <br /> 
Wechaty https://wechaty.js.org/<br /> 
revChatGPT https://github.com/acheong08/ChatGPT<br /> 
Bloom https://huggingface.co/bigscience/bloom<br /> 
OpenAI https://openai.com/<br /> 
源(Yuan) https://air.inspur.com/example<br /> 
<br /> 
1. npm <br /> 
Install node.js, https://nodejs.org/en/download/package-manager/<br /> 
run:<br /> 
npm init<br /> 
npm install wechaty<br /> 
<br /> 
2. pip<br /> 
run:<br /> 
pip install requests FastAPI emoji <br /> 
pip install openai #If will you use OpenAI<br /> 
pip install --upgrade revChatGPT #See https://github.com/acheong08/ChatGPT for any question about configuring ChatGPT<br /> 
pip install uvicorn #If you use ChatGPT<br /> 
<br /> 
3. config(not necessary)<br /> 
config.json<br /> 
Set "session_token" cookie on ChatGPT website in config.json <br /> 
	"session_token": "YOUR_TOKEN"<br /> 
And you can also set your language. I don't really know the effect of it.<br /> 
<br /> 
config.py<br /> 
Other language models:<br /> 
    Bloom: https://huggingface.co/bigscience/bloom<br /> 
    blmKey = {"Authorization": "YOUR_TOKEN"}<br /> 
    <br /> 
    OpenAI: https://beta.openai.com/account/api-keys<br /> 
    openai_api_key = "YOUR_API_KEY"<br /> 
    <br /> 
    源(Yuan): https://air.inspur.com/example<br /> 
    yuan_account = "YOUR_ACCOUNT"<br /> 
    yuan_phone = "YOUR_PHONE"<br /> 
    <br /> 
4. run<br /> 
npm start #run the bot and scan to login<br /> 
uvicorn GPT:app #if you are using ChatGPT
