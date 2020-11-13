import logging, tweepy, json, re
from config import create_api

logger = logging.getLogger()

def search_hashtag(api):
    hashtag = input("Which hashtag? ")
    for tweet in tweepy.Cursor(api.search,q=hashtag,count=100,tweet_mode="extended").items():
        if not re.search("^RT @.*",tweet.full_text):
            yield tweet._json

def parse_hashtag():
    api = create_api()
    try:
        with open('hashtag.json','w') as file:
            for tweet in search_hashtag(api):
                json.dumps(tweet)
    except KeyboardInterrupt:
        logger.warning("Process terminated by user.")
        raise SystemExit

def main():
    parse_hashtag()

if __name__ == "__main__":
    main()
