# farm fresh code for the official Senate Stalker (TM) tool
# authors: tessa ward, aislin paton, greta mayer, parker mayer

# importing the appropriate packages
from datapackage import Package
import datapackage
import pandas as pd
from datetime import datetime
from dateutil.parser import parse
import tweepy
import time
import os
from os import environ

# setting up keys
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_TICKET = environ['ACCESS_TICKET']

# setting up tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_TICKET)
api = tweepy.API(auth)

# all senators who voted against the Green New Deal
# (to be updated with a more long-term friendly method of handle collection)
senators = ['@SenToddYoung', '@SenatorWicker', '@SenToomey', '@SenThomTillis', '@SenJohnThune', '@SenDanSullivan', '@SenShelby', '@SenatorTimScott', '@SenRickScott', '@SenSasse', '@marcorubio', '@SenatorRomney', '@SenatorRounds', '@SenPatRoberts', '@SenatorRisch', '@senrobportman', '@sendavidperdue', '@RandPaul', '@lisamurowski', '@JerryMoran', '@SenMcSallyAZ', '@senatemajldr', '@SenatorLoeffler', '@SenMikeLee', '@SenatorLankford', '@SenJohnKennedy', '@SenRonJohnson', '@JimInhofe', '@SenHydeSmith', '@SenJohnHoever', '@HawleyMO', '@ChuckGrassley', '@LindseyGrahamSC', '@SenCoryGardner', '@SenatorFisher', '@SenJoniErnst', '@SenatorEnzi', '@SteveDaines', '@SenTedCruz', '@SenKevinCramer', '@MikeCrapo', '@SenTomCotton', '@JohnCornyn', '@SenatorCollins', '@SenBillCassidy', '@SenCapito', '@SenatorBurr', '@SenatorBraun', '@JohnBoozman', '@RoyBlunt', '@MarshaBlackburn', '@SenJohnBarrasso', '@SenAlexander', '@Sen_JoeManchin', '@SenatorSinema', '@SenDougJones', '@SenAngusKing']

# dividing senators into batches
senators_batch_1 = senators[0:14]
senators_batch_2 = senators[14:28]
senators_batch_3 = senators[28:42]
senators_batch_4 = senators[42:len(senators)-1]

while True:

    print("*rubs hands* get ready.")
    # grabbing the url of the data
    package = Package('https://datahub.io/core/co2-ppm-daily/datapackage.json')

    # uncomment to print list of all resources:
    #print(package.resource_names)

    # this function takes in the carbon dataframe and
    # its batch of senators
    def calculate_and_tweet_1(df, senators_batch_1):                         # today is saturday
        # grabbin' today's and (today - 1 year)'s carbon levels (in ppm)
        todays_carbon_level = df.loc[(len(df)- 1), 1]
        last_years_carbon_level = df.loc[(len(df)- 366), 1]

        # tweeting each of the senatorsTM
        for i in range(len(senators_batch_1)):
            tweet = str("Hey "+senators_batch_1[i]+"! Did you know that today, the level of CO2 in the atmosphere is "+todays_carbon_level+" parts per million? One year ago, it was "+last_years_carbon_level+" parts per million. Super cool, amirite? And it's thanks to your inaction! Source: https://carbon.datahub.io/# "+todays_date)
            api.update_status(status = (tweet))
            time.sleep(60)

    # this function is the same as calculate_and_tweet_1,
    # with a different batch of senators
    def calculate_and_tweet_2(df, senators_batch_2):                         # today is sunday
        todays_carbon_level = df.loc[(len(df)- 1), 1]
        last_years_carbon_level = df.loc[(len(df)- 366), 1]

        for i in range(len(senators_batch_2)):
            tweet = str("Hey "+senators_batch_1[i]+"! Here’s a fun reminder for you: today’s level of atmospheric CO2 is "+todays_carbon_level+" parts per million! A year ago, it was "+last_years_carbon_level+" parts per million. Wow, sure seems like something should be done about that! Source: https://carbon.datahub.io/# "+todays_date)
            api.update_status(status = (tweet))
            time.sleep(60)

    # this function is the same as calculate_and_tweet_1,
    # with a different batch of senators
    def calculate_and_tweet_3(df, senators_batch_3):                         # today is monday
        todays_carbon_level = df.loc[(len(df)- 1), 1]
        last_years_carbon_level = df.loc[(len(df)- 366), 1]

        for i in range(len(senators_batch_3)):
            tweet = str("Hey "+senators_batch_1[i]+"! Did you know that today, the level of CO2 in the atmosphere is "+todays_carbon_level+" parts per million? One year ago, it was "+last_years_carbon_level+" parts per million. Super cool, amirite? And it's thanks to your inaction! Source: https://carbon.datahub.io/# "+todays_date)
            api.update_status(status = (tweet))
            time.sleep(60)
    # this function is the same as calculate_and_tweet_1,
    # with a different batch of senators
    def calculate_and_tweet_4(df, senators_batch_4):                         # today is tuesdayyy
        todays_carbon_level = df.loc[(len(df)- 1), 1]
        last_years_carbon_level = df.loc[(len(df)- 366), 1]

        for i in range(len(senators_batch_4)):
            tweet = str("Hey "+senators_batch_1[i]+"! Here’s a fun reminder for you: today’s level of atmospheric CO2 is "+todays_carbon_level+" parts per million! A year ago, it was "+last_years_carbon_level+" parts per million. Wow, sure seems like something should be done about that! Source: https://carbon.datahub.io/# "+todays_date)
            api.update_status(status = (tweet))
            time.sleep(60)
    # this function pauses the program for 23 hours,
    # and is used to better space out the time-checking
    def go_to_sleep():
        time.sleep(60*60*23)

    # read in all the relevant data
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            co2_data = resource.read()

    # turning the data into a dataframe
    df = pd.DataFrame(co2_data)

    # grabbing today's date
    todays_date = datetime.now()
    print(todays_date)
    # checking the day and time, then tweeting appropriate senators (or taking a nop)
    if todays_date.weekday() == 5:   # if it's saturday
        calculate_and_tweet_1(df, senators_batch_1)
        go_to_sleep()
    elif todays_date.weekday() == 6: # if it's sunday
        calculate_and_tweet_2(df, senators_batch_2)
        go_to_sleep()
    elif todays_date.weekday() == 0: # if it's monday
        calculate_and_tweet_3(df, senators_batch_3)
        go_to_sleep()
    elif todays_date.weekday() == 1: # if it's tuesdayyy
        calculate_and_tweet_4(df, senators_batch_4)
        go_to_sleep()
    elif todays_date == 2:
        go_to_sleep()
        go_to_sleep()

    #update pause
    time.sleep(60)

# NOTE: more efficient time management method coming sooooooon.
#:)
