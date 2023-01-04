import requests
from oneString import compactTxt, save
from keys import blmKey

prompt = input()

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = blmKey

memoryFile = "memory.txt"
memoryTxt = compactTxt(memoryFile)
askPrefix = memoryTxt+"Q:How are you\nA:I am fine\nQ:Who are you\nA:Not telling ya\nQ:What robot are you\nA:Artificial Intelligence\nQ:"
queryTxt = askPrefix+prompt+"\nA:"

def txtCleaner(text):
    parts = text.split("\a")[0].split("Q:")
    return parts[0]


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	txt = txtCleaner(response.json()[0].get('generated_text').replace(askPrefix+prompt,"").replace("A:","").replace("A：","").replace("\n",""))
	print(txt)
	save(prompt, txt, memoryFile)
	
output = query({
	"use_cache": "true",
	"inputs": queryTxt,
	"temperature": "90",
	"top_k": "5",
	"top_p":"2.5",
	"repetition_penalty":"90",
	"max_time": "6"
})


