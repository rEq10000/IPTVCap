import datetime
import os
import time

os.system("title IPTVCap")

iptvlink = "linkhere"

while True:
	day = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')

	channel = "channelnamehere"

	os.system('ffmpeg.exe -i "' + iptvlink + '" -vf fps=1/1 -frames:v 1 -c copy"' + channel + day + '.jpg' + '"')

	time.sleep(60)