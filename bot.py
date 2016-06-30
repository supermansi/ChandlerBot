from tweepy.auth import OAuthHandler
from tweepy.api import API
import tweepy
import random
import lines
CONSUMER_KEY = 'oF2OKu4mAWGAhbf40mdr50bDH'
CONSUMER_SECRET = 'ulGAGnilOCST73V3TygLts0CvzOTsqX2ok5ZuV8bkbugDm0jbM'
ACCESS_KEY = '746079334524411904-ZFNQOloZpDjuF1vrV9P4wRWEnQqzrem'
ACCESS_SECRET = '9HDrKuWcbUWmvJBfZNPv6nvS48CSIH1xnsXUwoaXu7lhj'

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = API(auth)
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        sn = status.user.screen_name
        n = random.randint(0,11)
        message = "@" + sn + lines.say[n]
        api.update_status(message,status.id)

myStreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#print("Testing")
myStream.filter(track=['#chandlerbot'])
