import requests
import os
try:
    key = 'd14fee3e'
    base_url = 'http://www.omdbapi.com/'
    print()#prints empty line.
    movie = input("Enter the name of a movie: ")
    print()#prints empty line.
    #set the parameters, t parameter gets the name of the movie
    params = {'apikey' : key, 't' : movie}
    #get the data of specified movie in a json format, generates a python dictionary
    data = requests.get(base_url, params).json()

    print(data)
    print("Following information can be obtained about "+ movie + ":")
    print()#prints empty line.
    #this prints all the information that can be obtained about of the specified movie
    for key in data.keys():
        print(key)
    #asks what the user want information about of this movie
    print()#prints empty line.
    info = input("What information you want to obtain? ")
    print() #prints empty line.
    #this converts the first letter to uppercase and the remaining to lowercase
    #to match with the information key(exactly the way they are coded)
    first_Letter = info[0].upper()
    rem_Letters = info[1:].lower()
    info = first_Letter+rem_Letters
    #this prints the information user has requested to obtain.
    if info not in data:
        print("The information cannot be found.")
    else:
        if (info == "Ratings"):
            print(info + " of " +movie + ": " + data[info][0]['Value'])
        else:
            print(info + " of " +movie + ": "+ data[info])
except Exception as err:
    print(err)
