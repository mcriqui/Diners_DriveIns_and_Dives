import csv
import time
from yelpapi import YelpAPI

yelp_api = YelpAPI('V4oXt-CDFMUXzPerVYXWnA', 'omnmWvy6KQNOSt1o9qD0YwMtKiQ', '_WuvOb1mMpmTdhuh9LwvyY_RQzsiLt3B', 'yAbsrRApeXzSIO_KK1dbDzbw0oA')

rating_list = open('try_againrating_list.csv', 'w')
writer = csv.writer(rating_list)
business_id_list = []
rating_list = []

with open('new_clean_master_list.csv', 'r') as original_csv_file:
    episodes = original_csv_file.read().split('\n')
    for index, episode in enumerate(episodes):
        episodes[index] = episodes[index].split(',')
        business_id = episodes[index][5]
        try:
            response = yelp_api.business_query(id=business_id)
            rating_list.append(response['rating'])
            print business_id, response['rating']
        except KeyError:
            rating_business_id_list.append(business_id)
            rating_list.append('KeyError')
            print "{0} Key Error".format(biz_id)
    time.sleep(.5)

# for business_id, rating in zip(business_id_list, rating_list):
#     writer.writerow((business_id, rating))


# while True:
#     print "This prints once every 5 seconds."
#     time.sleep(5)
