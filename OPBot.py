import tweepy
import os
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_API = os.getenv("SECRET_API")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
SECRET_ACCESS = os.getenv("SECRET_ACCESS")

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=SECRET_API,
    access_token=ACCESS_TOKEN,
    access_token_secret=SECRET_ACCESS
)
FILE = Path("tweets.json")

def save_tweets(tweets):
    if FILE.exists():
        with open(FILE, "r") as f:
            old = json.load(f)
    else:
        old = []

    all_tweets = old + [t for t in tweets if t not in old]

    with open(FILE, "w") as f:
        json.dump(all_tweets, f, indent=4)


def getTweetFromAccout(username):
    try:
        response = client.get_user(username = username)
        user_id = response.data.id

        responseTweet = client.get_users_tweets(id = user_id, max_results = 20)
        if responseTweet.data:

            tweets = [tweet.text for tweet in responseTweet.data]


    except tweepy.TooManyRequests as e:
        # Print rate limit info if available
        print("Rate limit exceeded!")
        if hasattr(e.response, 'headers'):
            reset_timestamp = int(e.response.headers.get('x-rate-limit-reset'))
            reset_time = datetime.fromtimestamp(reset_timestamp)
            print(f"Rate limit: {e.response.headers.get('x-rate-limit-limit')} requests")
            print(f"Remaining: {e.response.headers.get('x-rate-limit-remaining')}")
            print(f"Reset time: {reset_time.strftime('%I:%M:%S %p')}")

    return tweets


def main():
    # Check rate limit status
    tweets = getTweetFromAccout("WorstGenHQ")

    save_tweets(tweets)

if __name__ == "__main__":
    main()