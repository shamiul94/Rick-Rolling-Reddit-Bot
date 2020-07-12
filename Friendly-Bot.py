#!venv/bin/python
import praw
import re
import random

reddit = praw.Reddit('bot1')
friend = input("Enter your friend's Reddit handle: ") 
redditor = reddit.redditor(friend)

comments = redditor.comments.new(limit=50)

for comment in comments: 
    try: 
        reply = "Take this bruh - https://www.youtube.com/watch?v=dQw4w9WgXcQ . I love you 3000."
        comment.reply(reply)
        print(comment.body)
        print('#'*50)
    except: 
        print('could not post')
        continue
    
            
