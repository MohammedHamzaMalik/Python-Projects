"""Simple Python script to set an alarm for a specific time.
   When the alarm goes off, a random youtube video will be opened.
   The possible youtube video URLs are taken from "youtube_alarm_videos.txt"
"""

import datetime
import os
import time
import random
import webbrowser

# If video URL file does not exist, create one
if not os.path.isfile("youtube_alarm_videos.txt"):
	print('Creating "youtube_alarm_videos.txt"...')
	with open("youtube_alarm_videos.txt", "w") as alarm_file:
		alarm_file.write("https://www.youtube.com/watch?v=anM6uIZvx74")

def check_alarm_input(alarm_time):
	"""Checks to see if the user has entered in a valid alarm time"""
	if len(alarm_time) == 1: # [Hour] Format
		if alarm_time[0] < 24 and alarm_time[0] >= 0:
			return True
	if len(alarm_time) == 2: # [Hour:Minute] Format
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0:
			return True
	elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0 and \
		   alarm_time[2] < 60 and alarm_time[2] >= 0:
			return True
	return False

# Get user input for the alarm time
print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
while True:
	alarm_input = input(">> ")
	try: