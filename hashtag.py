import logging, tweepy, json, re
from config import create_api

logger = logging.getLogger()

def hashtag(api):
    """ twitter api searches run more efficiently when pulling the full tweet._json object
    rather than specifying the relevant fields in the list comp; do that post hoc in parse.py """
    try:
        query = input("Twitter search term: ")
        with open('hashtag.json','w') as file:
            hashtag = [tweet._json for tweet in tweepy.Cursor(api.search,q=query,count=100,tweet_mode="extended").items() if not re.search("^RT @.*",tweet.full_text)]
            json.dump(hashtag,file)
    except KeyboardInterrupt:
        logger.warning("Process terminated by user.")
        raise SystemExit

def main():
    api = create_api()
    hashtag(api)

if __name__ == "__main__":
    main()
