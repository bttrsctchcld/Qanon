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
        self.users = []

    def load_tweets(self):
        try:
            with open("qanon.json","r") as file:
                self.hashtag = json.loads(file.read())
        except IOError:
            print("Missing hashtag file.")
        return self.hashtag
    
    def get_unique_screennames(self):
        self.load_tweets()
        return list(set([tweet["name"] for tweet in self.hashtag]))
        
    def get_user(self,users):
        users = self.get_unique_screennames()
        for user in users:
            yield user

    def update_user(self,user):
        user = get_user()
        self.profile["name"] = user
        self.users.append(self.profile)
        return

    def get_profile(self,user):
        for profile in tqdm(self.users):
            yield profile

    def match_updated_user(self,profile):
        profile = get_profile()
        for tweet in self.hashtag:
            if profile["name"] == tweet["name"]:
                profile["count"] += 1
                if profile["profile"] == None:
                    profile["profile"] = tweet["profile"]
        return

    def print_users(self):
        pprint.pprint(sorted(self.users,key=lambda n: n["count"],reverse=True[0:19]))

if __name__ == "__main__":
    tweets = Tweet()
