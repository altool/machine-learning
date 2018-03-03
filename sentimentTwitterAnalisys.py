import tweepy
import sys
from textblob import TextBlob

print('Analyzing for {}'.format(sys.argv[1]))

consumerKey = 'tXRQ85DRM29iBr6agtYqtuicx'
consumerSecret = 'c03KetUUucBXqTiLeT02k09rv1C73d9BkPtOnzKJ0SkK84iPL5'
accessToken = '372742883-jSL7EQf8jUnIMKLdmmaOYVgJpXY1hLzZpqSc1mtP'
accessTokenSecret = 'rllHkUpzC3ZOBjSkAdKuYHcgqainQsImXoQrXQSjdwAce'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

publicTweets = api.search(sys.argv[1])

for tweet in publicTweets:
    analyze = TextBlob(tweet.text)
    print(tweet.text)
    print("{} \nall ".format(analyze.sentiment))
