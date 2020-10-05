# Qanon
hashtag research project using Twitter API
 
api search pulls tweets, as json objects, into json string.

forum discussion about Twitter API suggests some confusion about pulling tweets, as json objects, into a json string despite json serialization errors which might arise in iteration with the full tweet object or even with specified fields, e.g. "created_at" (datetime). the documentation isn't very clear about this, but basically, you can't just pull the tweet (e.g., tweet for tweet), you need to pull its json attribute (e.g., tweet._json for tweet) if you want to pull the full tweet and all its associated keys and values.

you're better off pulling tweets by their json attribute rather than specifying every key-value pair you want to pull for the tweet since the former option is cleaner code, allows you to use a list comprehension rather than append for the json dump, and allows you to avoid writing your json objects out to csv. in my experience, list comp is much, much more stable and effecient than append (list of dicts) or writerow (csv) during calls to the fussy Twitter API.

repurposing hashtag.py requires keys associated with the developer portal, which requires an application to Twitter.
