import logging,json,copy
from tqdm import tqdm

class Tweet:
    def __init__(self,hashtag=None):
        if hashtag is None:
            self.hashtag = []
        else:
            self.hashtag = list(hashtag)
        self.processed_tweet = {"datetime":None,"name":None,"profile":None,"followers":0,"text":None,"favorites":0,"retweets":0,"verified":False}
        self.processed_tweets = []

    def load_tweets(self):
        try:
            with open("hashtag.json","r") as file:
                self.hashtag = json.loads(file.read())
        except FileNotFoundError:
            logging.error("Missing json file.",exc_info=True)
            raise
        return self.hashtag

    """ reprocess large, two-dimensional tweet._json objects as smaller, 
    one-dimensional dictionaries, preserving only the relevant key-value pairs """

    def process_tweets(self):
        self.load_tweets()
        for tweet in tqdm(self.hashtag):
            self.processed_tweet["datetime"] = tweet["created_at"]
            self.processed_tweet["name"] = tweet["user"]["screen_name"]
            self.processed_tweet["profile"] = tweet["user"]["description"]
            self.processed_tweet["followers"] = tweet["user"]["followers_count"]
            self.processed_tweet["text"] = tweet["full_text"]
            self.processed_tweet["favorites"] = tweet["favorite_count"]
            self.processed_tweet["retweets"] = tweet["retweet_count"]
            self.processed_tweet["verified"] = tweet["user"]["verified"]
            self.processed_tweets.append(copy.copy(self.processed_tweet))

    def return_tweets(self):
        self.process_tweets()
        with open("processed_hashtag.json","w") as file:
            json.dump(self.processed_tweets,file)

if __name__ == "__main__":
    tweets = Tweet()
    tweets.return_tweets()
