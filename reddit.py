# This script searches the top 100 'hot' posts on r/worldnews and prints the titles and links
# of all posts regarding the COVID-19 pandemic. By Gabriel Yap.
import praw
import pandas as pd
#The reddit_read_only variable is private authentication, do not share with anybody.
reddit_read_only = praw.Reddit(client_id="",         # your client id
                               client_secret="",      # your client secret
                               user_agent="")        # your user agent, important to make it specific or
#                                                      script will not work ex)mycovidscript
subreddit = reddit_read_only.subreddit("worldnews")
keywords = ['covid', 'covid-19', 'coronavirus', 'corona', 'vaccine', 'vaccination',
            'pandemic', 'quarantine', 'vaccinated', 'vaccin', 'lockdown', 'booster',
            'dose','cdc', 'omicron']
for post in subreddit.hot(limit=100):
    myTitle = post.title
    for key in keywords:
        if (key.casefold() in myTitle.casefold()): #checks if key is a substring in title
            print(myTitle)
            print("https://www.reddit.com" + post.permalink)
            print()
            break
