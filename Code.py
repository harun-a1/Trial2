import requests
import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080
sock.bind(('', port)) # actually bind
sock.listen(1)

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
