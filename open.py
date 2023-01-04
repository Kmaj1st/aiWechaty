import os
import openai
import emoji
import re
from keys import openai_api_key
openai.api_key = openai_api_key

inTxt = input();

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Q:How are you\nA:I am fine\nQ:Who are you\nA:Not telling ya\nQ:What robot are you\nA:Artificial Intelligence\nQ:"+inTxt+"\nA:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=["Q:", "A:"]
)

outTxt = response.choices[0].text;
print(outTxt)
humanMsg = emoji.replace_emoji(inTxt, replace="[表情]")
aiMsg= emoji.replace_emoji(outTxt, replace="[表情]")
f = open("memory.txt", "a")
try:
  f.write(humanMsg+"\n")
  f.write(aiMsg+"\n")
finally:f.close();

# list to store file lines
lines = []
# read file
with open(r"memory.txt", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()

# Write file
with open(r"memory.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 1 and 2. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in [0, 1]:
            fp.write(line)
