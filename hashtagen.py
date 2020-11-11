import json, csv, re, copy, pprint
from tqdm import tqdm

class Tweet:
    def __init__(self,hashtag=None):
        if hashtag is None:
            self.hashtag = []
        else:
            self.hashtag = list(hashtag)
        self.profile = {"name":None,"profile":None,"count":0}
        self.hashtag_count = {"hashtag":None,"count":0}
        self.hashtags = []
        self.unique_hashtags = []

    def load_tweets(self):
        try:
            with open("qanon.json","r") as file:
                self.hashtag = json.loads(file.read())
        except IOError:
            print("Missing hashtag file.")
        return self.hashtag
    
    def parse_tweets(self):
        self.load_tweets()
        clean_hashtags = []
        for tweet in self.hashtag:
            for word in tweet["text"].split():
                yield word
            for word in tweet["profile"].split():
                yield word

    def get_all_hashtags(self,word):
        word = parse_tweets()
        if re.search("^#.*",word):
            self.hashtags.append(word.rstrip(",;:.").lower())
            return
    
    def get_unique_hashtags(self):
        uniques = list(set(self.hashtags))
        for unique in uniques:
            yield unique

    def update_hashtags(self,unique):
        unique = self.get_unique_hashtags()
        self.hashtag_count["hashtag"] = unique
        for tag in self.hashtags:
            if self.hashtag_count["hashtag"] == tag:
                self.hashtag_count["count"] += 1
        self.unique_hashtags.append(self.hashtag_count)
        return

    def print_hashtags(self):
        pprint.pprint(sorted(self.unique_hashtags,key=lambda n: n["count"],reverse=True[0:99]))

if __name__ == "__main__":
    tweets = Tweet()
