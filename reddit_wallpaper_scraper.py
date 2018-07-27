import util
import config

wallpaper_subreddit = util.get_subreddit('wallpaper')
top_posts = util.get_top_posts(wallpaper_subreddit, 15, "all")
image_urls = util.get_image_urls(top_posts)

for url in image_urls:
    print(url)

util.download_image_url(image_urls[0], 'wallpaper')