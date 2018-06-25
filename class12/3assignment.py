import tweepy
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
n= input("enter the word without hashtag ..?")
n = "#" + n
tweets=api.search(n , lang="en" , count=5 , tweet_mode="extended")
#print(tweets)
for tweet in tweets:
    print("------------------")
    print(tweet.full_text)
    print("------------------")