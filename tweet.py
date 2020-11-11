import json, csv, re, copy, pprint
from tqdm import tqdm

class Tweet:
    def __init__(self):
        self.hashtag = []
        self.for_users = {"name":None,"profile":None,"count":0}
        self.for_hashtags = {"hashtag":None,"count":0}

    def load_tweets(self):
        try:
            with open("qanon.json","r") as file:
                self.hashtag = json.loads(file.read())
        except IOError:
            print("Missing hashtag file.")
        return self.hashtag
    
    def top_users(self):
        self.load_tweets()
        users = []
        screen_names = [tweet["name"] for tweet in self.hashtag]
        unique_names = list(set(screen_names))
        for name in unique_names:
            self.for_users["name"] = name
            users.append(copy.copy(self.for_users))
        for self.for_users in tqdm(users):
            for tweet in self.hashtag:
                if self.for_users["name"] == tweet["name"]:
                    self.for_users["count"] += 1
                    if self.for_users["profile"] == None:
                        self.for_users["profile"] = tweet["profile"]
        sorted_users = sorted(users,key=lambda n: n["count"],reverse=True)
        pprint.pprint(sorted_users[0:19])

    def other_hashtags(self):
        self.load_tweets()
        hashtags = []
        clean_hashtags = []
        for tweet in self.hashtag:
            for word in tweet["text"].split():
                if re.search("^#.*",word):
                    hashtags.append(word.rstrip(",;:.").lower())
            for word in tweet["profile"].split():
                if re.search("^#.*",word):
                    hashtags.append(word.rstrip(".;:.").lower())
        unique_hashtags = list(set(hashtags))
        for unique in unique_hashtags:
            self.for_hashtags["hashtag"] = unique
            clean_hashtags.append(copy.copy(self.for_hashtags))
        for self.for_hashtags in tqdm(clean_hashtags):
            for tag in hashtags:
                if self.for_hashtags["hashtag"] == tag:
                    self.for_hashtags["count"] += 1
        sorted_hashtags = sorted(clean_hashtags,key=lambda n: n["count"],reverse=True)
        pprint.pprint(sorted_hashtags[0:99])

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

tweets = Tweet()
tweets.other_hashtags()
