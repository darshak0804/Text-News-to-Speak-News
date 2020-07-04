def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ =='__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=d9bf0ac8a91d4bf48f87e94263e6aa0b')
    response =requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0,11):
        speak(my_json['articles'][i]['title'])
