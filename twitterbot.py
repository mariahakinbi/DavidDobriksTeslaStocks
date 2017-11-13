#import Twitter credentials from credentials.py and tweepy
from credentials import *
import tweepy

#Access and authorize Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#Check Authentication!
# tweet = 'Hello, world!'
# api.update_status(status=tweet)

# Open text file verne.txt (or your chosen file) for reading
my_file = open('textfile.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

from time import sleep

for line in file_lines:
    # line = unicode(line, 'utf-8')
    print(line)
