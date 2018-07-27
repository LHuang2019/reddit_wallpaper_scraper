import util
import config

wallpaper_subreddit = util.get_subreddit('wallpapers')
top_posts = util.get_hot_posts(wallpaper_subreddit, 15)
image_urls = util.get_image_urls(top_posts)

image_file_path = util.download_image_url(image_urls[0], 'wallpapers')
util.set_windows_desktop_background(image_file_path)
