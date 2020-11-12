import logging, json, csv, re, copy, pprint
from tqdm import tqdm

logger = logging.getLogger()

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
        except FileNotFoundError:
            logging.error("Missing json file.",exc_info=True)
            raise
        logger.info("Tweets loaded from json.")
        return self.hashtag
    
    def parse_tweets(self):
        self.load_tweets()
        for tweet in self.hashtag:
            for word in tweet["text"].split():
                yield word
            for word in tweet["profile"].split():
                yield word

    def get_all_hashtags(self):
        for word in self.parse_tweets():
            if re.search("^#.*",word):
                self.hashtags.append(word.rstrip(",;:.").lower())
        return
    
    def update_hashtags(self):
        uniques = list(set(self.hashtags))
        uniques_generator = (unique for unique in uniques)
        for unique in uniques_generator:
            self.hashtag_count["hashtag"] = unique
            self.unique_hashtags.append(copy.copy(self.hashtag_count))

    def count_hashtags(self):
        uniques = (self.hashtag_count for self.hashtag_count in self.unique_hashtags)
        for self.hashtag_count in tqdm(uniques):
            for tag in self.hashtags:
                if self.hashtag_count["hashtag"] == tag:
                    self.hashtag_count["count"] += 1
        logger.info("Hashtags counted per usage.")
        return

    def print_hashtags(self):
        pprint.pprint(sorted(self.unique_hashtags,key=lambda n: n["count"],reverse=True)[0:99])

    def secondary_hashtag(self):
        self.load_tweets()
        secondary = input("Which hashtag do you want to cross-reference? ")
        with open("secondary.csv","w") as csvFile:
            fieldnames = ['datetime','name','profile','followers','text','favorites','retweets','verified']
            writer = csv.DictWriter(csvFile,fieldnames=fieldnames)
            writer.writeheader()
            for tweet in self.hashtag:
                if re.search(secondary,tweet["text"],re.IGNORECASE) or re.search(secondary,tweet["profile"],re.IGNORECASE):
                    writer.writerow(tweet)

if __name__ == "__main__":
    tweets = Tweet()
    tweets.get_all_hashtags()
    tweets.update_hashtags()
    tweets.count_hashtags()
    tweets.print_hashtags()
