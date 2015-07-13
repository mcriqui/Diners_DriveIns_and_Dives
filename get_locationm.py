import csv
import time
from geopy.geocoders import GoogleV3
import json

geolocator = GoogleV3()


clean_file = open('final_with_location.csv', 'w')
writer = csv.writer(clean_file)

with open('new_and_imporoved.csv', 'r') as original_file:
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
        review_count = episodes[index][7]
        try:
            address, (latitude, longitude) = geolocator.geocode(city, state)
        except:
            address = 'Unknown Error'
            longitude = 'Unknown Error'
            latitude = 'Unknown Error'
        print address, latitude, longitude
        writer.writerow((season, title, restaurant, city, state, business_id, rating, review_count, address, latitude, longitude))
        time.sleep(.25)

clean_file.close()
