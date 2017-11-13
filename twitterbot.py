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
my_file = open('textfile.txt', 'r', encoding='utf-8')
# print(st.encode('ascii').decode('unicode-escape').encode('iso-8859-1').decode('utf-8'))

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.read()

# Close file
my_file.close()

from time import sleep

skip_these_char = ['\u2019','\u201c','\u201d','\u2013']

sentences =''

for line in file_lines:
    if line in skip_these_char:
        continue
    sentences+=line



#WHEN U SEE A NEWLINE CHAR: ADD THE STUFF BEFORE IT TO A LSIT AS A STRING
tweets = []
line =''
for char in sentences:
    if char =='\n':
        tweets+=line
    else:
        line+=char
print(len(tweets))
print(tweets)
# print(sentences)
# for line in sentences:
#     print (line)

# print(sentences.split("\n")[0])
