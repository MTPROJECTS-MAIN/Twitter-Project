import tweepy
import time
import datetime
from time import sleep
import random

auth = tweepy.OAuthHandler('6OSwzzAuNzE0GFMKZIf3GFaFe', '2VMu9Kyhp1v5QDDix6aA5oCdqCObFycVX5Gxmvtar5atEZX6gv')
auth.set_access_token('967911484704657408-7ShuEHQDhXFrUrNeJXTkIXbBxQutzSE', 'eTFB5Ypm19t2DlomsCyyFrGqlmpzsNtRhdv52OCfbC4mv')
api = tweepy.API(auth)

class twitterStuff:



    def followPeople(self):

        numberOfFOllowers = (random.randint(10, 30))
        print('Number of followers before rest: ' + str(numberOfFOllowers))

        counter = 0
        dailyCounter = 0
        totalcounter = 0
        for follower in tweepy.Cursor(api.search, q="#Crypto").items():

            # The number of followers this account currently has
            followersCount =(follower.author.followers_count)
            # The number of users this account is following
            followingCount = (follower.author.friends_count)
            # The number of statuses by the user
            statusCount = (follower.author.statuses_count)
            #followers name
            name = (follower.author.screen_name)

            if(dailyCounter == 400):
                sleep(10800)
                dailyCounter = 0

            if (counter == numberOfFOllowers):
                counter = 0
                sleepTime = (random.randint(5, 15))
                print('Sleep time: ' + str(sleepTime))
                print('Total counter: ' + str(totalcounter))
                sleep(sleepTime * 60)
                numberOfFOllowers = (random.randint(10, 30))
                print('Number of followers before rest: ' + str(numberOfFOllowers))

            if(followersCount >= 150 and followingCount >= 300 and followingCount > followersCount and statusCount >= 200 and counter <= numberOfFOllowers):
                counter += 1
                dailyCounter += 1
                totalcounter += 1
                api.create_friendship(name)
                print(str(counter) + ') ' + follower.author.screen_name + ':: Following: ' + str(followingCount) + ' :: Followers: ' + str(followersCount)
                      + ' :: Status Count: ' + str(statusCount))

               # api.send_direct_message(follower.author.screen_name,'Hey if you are active in the Crypto community'
                                                                    #'give my buddy @the_bitbybit a follow and also follow me back!'
                                                                    #'We are trying to grow the crypto community and following back '
                                                                    #'everyone that follows us!')
                sleep(10)




















tweets = twitterStuff()

while(True):
    try:
        tweets.followPeople()
    except Exception as e:

        print('program has crashed : ' + str(datetime.datetime.now()))

        sleep(60)







