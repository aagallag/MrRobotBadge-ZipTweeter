#!/usr/bin/env python2
import tweepy
from secret import consumer_key, consumer_secret, access_key, access_secret

def zip_tweeter(username, outfname):
    zip_data = ''

    # tweepy setup
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # iterate through the 200 most recent tweets
    tweets = api.user_timeline(screen_name=username, count=200)
    for tweet in tweets:
        txt = tweet.text.encode("utf-8")

        if len(txt) != 23:
            continue

        try:
            decoded = txt.replace(' ', '').decode('hex')
            zip_data = decoded + zip_data
        except:
            pass

        if txt == '50 4B 03 04 14 00 00 00':
            break

    # write the zipdata to a file
    with open(outfname, 'wb') as f:
        f.write(zip_data)
    print('Tweets written to file: %s' % outfname)


if __name__ == '__main__':
    #pass in the username of the account you want to download
    zip_tweeter('MrRobotBadge', 'mrrobotbadge.zip')
