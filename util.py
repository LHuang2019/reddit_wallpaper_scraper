import config
import praw
import re
import os
import urllib.request

reddit_instance = praw.Reddit(client_id=config.REDDIT_CLIENT_ID,
                              client_secret=config.REDDIT_CLIENT_SECRET,
                              user_agent=config.USER_AGENT)


def get_subreddit(subreddit_name):
    return reddit_instance.subreddit(subreddit_name)


def get_top_posts(subreddit, num_post, time):
    return subreddit.top(limit=num_post, time_filter=time)


def get_hot_posts(subreddit, num_post, time):
    return subreddit.hot(limit=num_post, time_filter=time)


def get_image_urls(posts):
    image_urls = []
    for submission in posts:
        if not submission.over_18:
            url = re.sub(R"\?.*", "", submission.url) # remove trailing arguments
            if url.endswith(".jpg") or url.endswith(".png"):
                image_urls.append(submission.url)

    return image_urls


def download_image_url(url, dir_name):
    ensure_dir(dir_name)
    if not dir_name.endswith('\\'):
        dir_name = dir_name + '\\'

    urllib.request.urlretrieve(url, dir_name + url.split('/')[-1])


def ensure_dir(dir_name):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, dir_name)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)