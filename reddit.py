# This script searches the top 100 'hot' posts on r/worldnews and creates history.csv
# which stores the title and links of all COVID-related posts. By Gabriel Yap.
import praw
import pandas as pd
import datetime
#The reddit_read_only variable is private authentication, do not share with anybody.
reddit_read_only = praw.Reddit(client_id="",         # your client id
                               client_secret="",      # your client secret
                               user_agent="")        # your user agent, important to make specific
#
subreddit = reddit_read_only.subreddit("worldnews")
numCovidPosts = 0
keywords = ['covid', 'covid-19', 'coronavirus', 'corona', 'vaccine', 'vaccination',
            'pandemic', 'quarantine', 'vaccinated', 'vaccin', 'lockdown', 'booster',
            'dose','cdc', 'omicron']
file = open('history.csv', 'a')
currTime = datetime.datetime.now()
file.write(currTime.strftime('%c')) # write current date before finding covid posts
file.write('\n')
for post in subreddit.hot(limit=100):
    myTitle = post.title
    for key in keywords:
        if (key.casefold() in myTitle.casefold()): #checks if key is a substring in title
            myTitle = myTitle.replace(',', '-')
            file.write(myTitle + ",")
            file.write("https://www.reddit.com" + post.permalink)
            file.write('\n')
            print(myTitle)
            print("https://www.reddit.com" + post.permalink)
            print()
            numCovidPosts += 1
            break
file.close()
dateFile = open('dates.csv', 'a')
dateFile.write(currTime.strftime('%j') + "," + str(numCovidPosts) + '\n')
dateFile.close()
