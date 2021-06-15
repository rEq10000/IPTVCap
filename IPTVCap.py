import datetime
import os
import time

os.system("title IPTVCap - Images Downloaded: 0")

iptvlink = "linkhere"
curvalue = 0
while True:
	day = datetime.datetime.now().strftime('-%Y-%m-%d %H.%M.%S')

	channel = "channelnamehere"

	os.system('ffmpeg -i "' + iptvlink + '" -vf fps=1/1 -frames:v 1 "' + channel + day + '.jpg' + '"')
	curvalue = 1 + curvalue
	os.system("title IPTVCap - Images Downloaded: 0")
	time.sleep(60)