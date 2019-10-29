import requests

response = requests.get('https://api.chucknorris.io/jokes/random')

responseCode = response.status_code
responseJoke = response.json()['value']

all_freq = {} 
  
for i in responseJoke: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1

print(responseJoke, '\n')
print ("Count of all characters in the joke is :\n "
                                        +  str(all_freq)) 