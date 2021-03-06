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
        self.users = []

    def load_tweets(self):
        try:
            with open("stop.json","r") as file:
                self.hashtag = json.loads(file.read())
        except FileNotFoundError:
            logger.error("Missing json file.",exc_info=True)
            raise
        logger.info("Tweets loaded from json.")
        return self.hashtag
    
    def get_unique_screennames(self):
        self.load_tweets()
        screennames = list(set([tweet["name"] for tweet in self.hashtag]))
        for user in screennames:
            yield user

    def update_user(self):
        for user in self.get_unique_screennames():
            self.profile["name"] = user
            self.users.append(copy.copy(self.profile))

    def match_updated_user(self):
        profiles = (profile for profile in self.users)
        try:
            for profile in tqdm(profiles):
                for tweet in self.hashtag:
                    if profile["name"] == tweet["name"]:
                        profile["count"] += 1
                        if profile["profile"] == None:
                            profile["profile"] = tweet["profile"]
        except KeyboardInterrupt:
            logger.warning("Process terminated by user.")
            raise SystemExit
        logger.info("Hashtag usage-per-user counted.")
        return

    def print_users(self):
        pprint.pprint(sorted(self.users,key=lambda n: n["count"],reverse=True)[0:19])

if __name__ == "__main__":
    tweets = Tweet()
    tweets.get_unique_screennames()
    tweets.update_user()
    tweets.match_updated_user()
    tweets.print_users()
