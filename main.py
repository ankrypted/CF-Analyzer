import urllib2
import json
import sys

# print sys.argv[0]
S = sys.argv[1]
temp = json.load(urllib2.urlopen("https://codeforces.com/api/user.rating?handle="+S))
for item in temp["result"]:
	print item["handle"], "participated in following Contests :-\n"
	break
cnt = 1
for	items in temp["result"]:
	print cnt,")", items["contestName"], ": "
	print "Rank Obtained: ", items["rank"], ","
	print "Old Rating: ", items["oldRating"], ","
	print "New Rating: ", items["newRating"], ","
	print "Development: ", items["newRating"] - items["oldRating"], "."
	cnt += 1