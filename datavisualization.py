import pygal
from pygal.style import DefaultStyle, BlueStyle, RedBlueStyle
import itertools
import collections
import tweepy
import twitter_info 
import json
import sqlite3
import re

time_data = json.load(open('engagementtest2.json', encoding = "utf-8"))
topic_data = json.load(open('convertcsv.json', encoding = "utf-8"))


newlist = sorted(time_data, key=lambda k: k['engage_rate'], reverse = True)
with open("output.txt", "w") as text_file:
    text_file.write(str(newlist[0:10]))

rates_time_tups = []

for x in time_data:
	y = x["time_hr"], (x["engage_rate"])
	tup = tuple(y)
	rates_time_tups.append(y)


xy_chart = pygal.XY(stroke=False, style = DefaultStyle)
xy_chart.title = 'Engagement Rates v. Time of Day'
xy_chart.add('@umichTECH', rates_time_tups)

xy_chart.render_to_file('scatterplot.svg')




topic_counts = {}
count1 = 0
count2 = 0
count3 = 0
count4 = 0


for x in topic_data:
	if x['code'] == 'Projects and Services':
		count1 = count1 + x['num_favorites'] + x['num_retweets']
	elif x['code'] == 'Campus News':
		count2 = count2 + x['num_favorites'] + x['num_retweets']
	elif x['code'] == "Jobs, Training, & Events":
		count3 = count3 + x['num_favorites'] + x['num_retweets']
	elif x['code'] == 'Safe Computing':
		count4 = count4 + x['num_favorites'] + x['num_retweets']



topic_counts['Projects and Services'] = count1
topic_counts['Campus News'] = count2
topic_counts["Jobs, Training, & Events"] = count3
topic_counts['Safe Computing'] = count4





pie_chart = pygal.Pie(style = DefaultStyle)
pie_chart.title = 'Engagement with UM-ITS Core Topics'
pie_chart.x_title = ''
pie_chart.add('Projects and Services', topic_counts['Projects and Services'])
pie_chart.add('Campus News', topic_counts['Campus News'])
pie_chart.add('Jobs, Training, & Events', topic_counts["Jobs, Training, & Events"])
pie_chart.add('Safe Computing', topic_counts['Safe Computing'])
pie_chart.render_to_file('pie_chart.svg')



tweet_counts = {}
count7 = 0
count8= 0
count9 = 0
count0 = 0


for x in topic_data:
	if x['code'] == 'Projects and Services':
		count7 = count7 + 1
	elif x['code'] == 'Campus News':
		count8 = count8 + 1
	elif x['code'] == "Jobs, Training, & Events":
		count9 = count9 + 1
	elif x['code'] == 'Safe Computing':
		count0 = count0 + 1



tweet_counts['Projects and Services'] = count7
tweet_counts['Campus News'] = count8
tweet_counts["Jobs, Training, & Events"] = count9
tweet_counts['Safe Computing'] = count0

pie_chart2 = pygal.Pie(style = DefaultStyle)
pie_chart2.title = 'Tweets per UM-ITS Core Topic'
pie_chart2.x_title = ''
pie_chart2.add('Projects and Services', tweet_counts['Projects and Services'])
pie_chart2.add('Campus News', tweet_counts['Campus News'])
pie_chart2.add('Jobs, Training, & Events', tweet_counts["Jobs, Training, & Events"])
pie_chart2.add('Safe Computing', tweet_counts['Safe Computing'])
pie_chart2.render_to_file('pie_chart2.svg')