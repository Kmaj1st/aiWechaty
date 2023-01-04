import requests
from urllib.parse import unquote

def main() :
    response = requests

    text = input()
    if (text=="favicon.ico") : return
    
#    try:
    response = requests.get('http://localhost:8000/'+unquote(text))
#    except Exception as exc:
#        response.text = "Something went wrong! exc:"+ str(exc)

    print(response.text.replace("\n","")[1:-1])

    
main()
