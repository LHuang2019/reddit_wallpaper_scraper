import praw

username = input("input reddit username: ")
password = input("input reddit password: ")

reddit_instance = praw.Reddit(client_id = 'R__rt8SuE-XbAA',
                              client_secret = 'ME7w-NDfmaHRHIz2xDDtg3V3fQA',
                              username = username,
                              password = password,
                              user_agent = 'reddit_wallpaper_scraper_v1')

subreddit = reddit_instance.subreddit('python')
hot_python = subreddit.hot(limit=5)

for submission in hot_python:
    print(submission)