import tweepy, json, re
from config import create_api

def hashtag(api):
    hashtag = input("Which hashtag? ")
    with open('hashtag.json','w') as file:
        hashtag = [tweet._json for tweet in tweepy.Cursor(api.search,q=hashtag,count=100,tweet_mode="extended").items() if not re.search("^RT @.*",tweet.full_text)]
        json.dump(hashtag,file)

def main():
    api = create_api()
    hashtag(api)

if __name__ == "__main__":
    main()
