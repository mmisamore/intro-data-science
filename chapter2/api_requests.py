import json
import requests
import pprint

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain. 
    
    data = requests.get(url).text
    data = json.loads(data)
    
    return data['topartists']['artist'][0]['name']

url = 'http://ws.audioscrobbler.com/2.0?method=geo.gettopartists&country=Spain&format=json&api_key=57ee3318536b23ee81d6b27e36997cde'
pprint.pprint(api_get_request(url))

