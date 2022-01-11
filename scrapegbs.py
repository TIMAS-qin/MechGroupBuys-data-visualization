import praw
import csv


reddit = praw.Reddit(client_id='ttuPXocpk8VbeL-stkV8dA', client_secret='gj0ryshloRnJDibYWu9LqQTsdzQrkA', user_agent='Thomas')

i=0

with open('newkeebinfo.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    for submission in reddit.subreddit('MechGroupBuys').new(limit=3000):
            upvotes = submission.score
            comments = submission.num_comments
          #  info = submission.comments[0]
            title = submission.title        
            writer.writerow([title, upvotes, comments])
            i = i+1
            print(i)

