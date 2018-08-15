import util
from random import randint
from tkinter import *

root = Tk()
root.title("Reddit Wallpaper Scraper")

frame = Frame(root)

title_label_text = StringVar()
title_label_text.set("subreddit name: ")
title_label = Label(frame, textvariable=title_label_text)
title_label.grid(row=0, column=0)

subreddit = StringVar(None)
subreddit_entry = Entry(frame, textvariable=subreddit, width=20)
subreddit_entry.grid(row=0, column=1)

post_type_label_text = StringVar()
post_type_label_text.set("post type: ")
post_type_label = Label(frame, textvariable=post_type_label_text)
post_type_label.grid(row=1, column=0)

POST_TYPE_OPTIONS = [
    "hot",
    "top"
]

post_type_default = StringVar()
post_type_default.set(POST_TYPE_OPTIONS[0]) # default value

post_type_menu = OptionMenu(frame, post_type_default, *POST_TYPE_OPTIONS)
post_type_menu.config(width=15)
post_type_menu.grid(row=1, column=1)

post_num_text = StringVar()
post_num_text.set("number of post: ")

post_num_label = Label(frame, textvariable=post_num_text)
post_num_label.grid(row=2, column=0)

post_num = StringVar(None)
post_num_entry = Entry(frame, textvariable=post_num, width=20)
post_num_entry.grid(row=2, column=1)

button = Button(frame, text="Change wallpaper")
button.grid(columnspan=2)

frame.pack()
root.mainloop()

subreddit = 'wallpapers'
post_nums = 15


wallpaper_subreddit = util.get_subreddit(subreddit)
hot_posts = util.get_hot_posts(wallpaper_subreddit, post_nums)
image_urls = util.get_image_urls(hot_posts)
image_url = image_urls[randint(0, post_nums - 1)]
image_file_path = util.download_image_url(image_url, subreddit)
util.set_windows_desktop_background(image_file_path)
