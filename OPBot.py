import tweepy
import os
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from google import genai

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
            try:
                old = json.load(f)
            except json.JSONDecodeError:
                old = []
    else:
        old = []

    all_tweets = old + [t for t in tweets if t not in old]

    with open(FILE, "w") as f:
        json.dump(all_tweets, f, indent=4)


def getTweetFromAccout(username):
    tweets = []
    try:
        response = client.get_user(username = username)
        user_id = response.data.id
        print(f"Found user: {response.data.username} (ID: {user_id})")

        responseTweet = client.get_users_tweets(id = user_id, max_results = 35)
        if responseTweet.data:
            print(f"Retrieved {len(responseTweet.data)} tweets")
            for tweet in responseTweet.data:
                if "#ONEPIECE1165" in tweet.text:
                    tweets.append(tweet.text)
                    print(f"Found matching tweet: {tweet.text[:50]}...")

            if not tweets:
                print("No tweets found with hashtag #ONEPIECE1165")
        else:
            print("No tweets returned from API")

    except tweepy.TooManyRequests as e:
        print("Rate limit exceeded!")
        if hasattr(e.response, 'headers'):
            reset_timestamp = int(e.response.headers.get('x-rate-limit-reset'))
            reset_time = datetime.fromtimestamp(reset_timestamp)
            print(f"Rate limit: {e.response.headers.get('x-rate-limit-limit')} requests")
            print(f"Remaining: {e.response.headers.get('x-rate-limit-remaining')}")
            print(f"Reset time: {reset_time.strftime('%I:%M:%S %p')}")

    except tweepy.TwitterServerError as e:
        print(f"Twitter server error: {e}")
        print("The Twitter API is temporarily unavailable. Please try again later.")

    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")

    return tweets

geminiClient = genai.Client()

def analyzeSpoilers():
    if FILE.exists():
        with open(FILE, "r") as f:
            try:
                tweetsToAnalyze = json.load(f)
            except json.JSONDecodeError:
                tweetsToAnalyze = []
    else:
        tweetsToAnalyze = []

    prompt = "Summarize these vague spoilers for one piece's new chapter"
    tweetsToAnalyze.insert(0, prompt)
    geminiAnalysis = geminiClient.models.generate_content(
        model = "gemini-2.5-flash",
        contents = tweetsToAnalyze
    )

    print(geminiAnalysis.text)


def main():
    tweets = getTweetFromAccout("WorstGenHQ")

    save_tweets(tweets)

    #analyzeSpoilers()

if __name__ == "__main__":
    main()