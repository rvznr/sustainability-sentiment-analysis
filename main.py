import praw
import os
import pandas as pd
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

def scrape_reddit(subreddit_name, keyword=None, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.hot(limit=limit):
        if keyword and keyword.lower() not in post.title.lower():
            continue
        
        sentiment = analyze_sentiment(post.title)
        posts.append({
            'Date': pd.to_datetime(post.created_utc, unit='s'),
            'Title': post.title,
            'Upvotes': post.score,
            'Sentiment': sentiment
        })

    df = pd.DataFrame(posts)
    df.to_csv('reddit_posts.csv', index=False)
    print(f'Scraped {len(df)} posts from r/{subreddit_name} and saved to reddit_posts.csv!')
    return df

if __name__ == '__main__':
    subreddit_name = input("Enter subreddit name: ")
    keyword = input("Enter keyword to filter (press Enter to skip): ")
    limit = int(input("Enter number of posts to scrape: "))

    df = scrape_reddit(subreddit_name, keyword, limit)
    print(df.head())