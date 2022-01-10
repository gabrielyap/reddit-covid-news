# reddit-covid-news
A Python script that searches the top 100 "hot" posts on r/worldnews and creates a .csv file with the titles and links of all posts regarding the COVID-19 pandemic. Utilized Reddit’s API and gathered relevant news on current events.

# Instructions for authentication
1) Create a Reddit account then visit https://www.reddit.com/prefs/apps/. Then click "create an app".
2) Type a SPECIFIC name ex)myredditcovidnews. Then, check the "script" box. For redirect uri, use "http://localhost:8080" (no quotes). You should now have 
   an authorized app named what ever you named it. Use this for part 4.
4) In reddit.py line 6-8, paste your client_id (the sequence of letters, numbers underneath "personal use script" and above the secret ID).
   Paste in your client_secret (the sequence on letters and numbers after "secret").
   Paste in your user_agent (the title of your application).
5) The program should be set and authorized.
