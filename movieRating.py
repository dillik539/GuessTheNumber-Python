import requests
import os
key = 'd14fee3e'
base_url = 'http://www.omdbapi.com/'
movie = input("Enter the name of a movie: ")
params = {'apikey' : key, 't' : movie}
data = requests.get(base_url, params).json()
print(data)
print("Rating for that movie: ")
print(data['Ratings'][0]['Value'])
