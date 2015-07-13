# encoding: utf-8
import csv
import time
from yelpapi import YelpAPI

yelp_api = YelpAPI('V4oXt-CDFMUXzPerVYXWnA', 'omnmWvy6KQNOSt1o9qD0YwMtKiQ', '_WuvOb1mMpmTdhuh9LwvyY_RQzsiLt3B', 'yAbsrRApeXzSIO_KK1dbDzbw0oA')

clean_file = open('new_and_imporoved.csv', 'w')
writer = csv.writer(clean_file)

with open('Final_csv.csv', 'r') as original_file:
    episodes = original_file.read().split('\n')
    for index, episode in enumerate(episodes):
        episodes[index] = episodes[index].split(',')
        season = episodes[index][0]
        title = episodes[index][1]
        restaurant = episodes[index][2]
        city = episodes[index][3]
        state = episodes[index][4]
        business_id = episodes[index][5]
        rating = episodes[index][6]
        response = yelp_api.business_query(id=business_id)
        if 'is_claimed' in response.keys():
            review_count = response['review_count']
            print restaurant, review_count
        elif 'error' in response.keys():
            review_count = 'Error'
        else:
            review_count = 'Error'
        writer.writerow((season, title, restaurant, city, state, business_id, rating, review_count))
        time.sleep(.5)

clean_file.close()
