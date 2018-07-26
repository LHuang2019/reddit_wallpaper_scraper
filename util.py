import config
import praw
import re

reddit_instance = praw.Reddit(client_id = config.REDDIT_CLIENT_ID,
                              client_secret = config.REDDIT_CLIENT_SECRET,
                              user_agent = config.USER_AGENT)


def get_subreddit(subreddit_name):
    return reddit_instance.subreddit(subreddit_name)


def get_top_posts(subreddit, num_post):
    return subreddit.top(limit = num_post)


def get_hot_posts(subreddit, num_post):
    return subreddit.hot(limit = num_post)


def get_image_urls(posts):
    image_urls = []
    for submission in posts:
        if not submission.over_18:
            url = re.sub(R"\?.*", "", submission.url) # remove trailing arguments
            if url.endswith(".jpg") or url.endswith(".png"):
                image_urls.append(submission.url)

    return image_urls

