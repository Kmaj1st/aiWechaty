from inspurai import Yuan, set_yuan_account,Example
import emoji
import re
from oneString import save
from keys import yuan_account, yuan_phone
memoryFile = "memory.txt"
set_yuan_account(yuan_account, yuan_phone)

yuan = Yuan(engine="dialog",
            temperature=0.8,
            max_tokens=100,
            topK=50,
            topP=0.5,
	    input_prefix="Q：“",
            input_suffix="”",
            output_prefix="A：“",
            output_suffix="”",)
            
yuan.add_example(Example(inp="我发一段语音，[VOICET2]，听得到吗",
                        out="我耳朵聋了，听不到，打字!"))
yuan.add_example(Example(inp="我发一段语音，[VOICET2]，听得到吗",
                        out="你投资我点钱让我装个听音模型吧"))
yuan.add_example(Example(inp="你的眼睛看不到[IMGT6]是图片",
                        out="我眼睛瞎了，打字吧!"))
yuan.add_example(Example(inp="[表情]",
                        out="发啥表情阿，不会打字？"))
                        
f = open(memoryFile, "r")
for x in range(5):{
  Q:=f.readline(),
  A:=f.readline(),
  yuan.add_example(Example(inp=Q,
                        out=A))
}
prompt = emoji.replace_emoji(input(), replace="[表情]")
response = yuan.submit_API(prompt=prompt,trun="”")


print(response);
save(prompt, response, memoryFile)
