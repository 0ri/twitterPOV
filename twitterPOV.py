#!/usr/bin/python

import sys
import twitter

api = twitter.Api(consumer_key='your_key_here',
                  consumer_secret='your_secret_here',
                  access_token_key='your_token',
                  access_token_secret='your_token_secret')

#Twitter handle of the person you want to set as your point-of-view
sname = raw_input("Enter the Twitter handle: ")

#Get all the userIDs that they follow
userids = api.GetFriendIDs(screen_name=sname)

print sname + " follows " + str(len(userids)) + " people."

#turn into a string for CreateListMembers
results = [str(i) for i in userids]

#Create a new private twitter list named after the screen name
listName = api.CreateList(name=sname, mode="private", description="twitter from %s's point-of-view" % sname) 

print "Created a new private twitter list called " + sname

#Break into chunks of 10 due to Twitter rate-limiting 
#Also max out at 500 since lists are limited to that length
if len(results) < 500:
	for i in xrange(0, len(results), 10):
		print "adding " + str(i+10)
		api.CreateListsMember(list_id=str(listName.id), user_id=results[i:i+10])
else:
	print "Twitter lists capped, so limiting to the first 500"
	for i in xrange(0, 500, 10):
		print "adding " + str(i+10)
		api.CreateListsMember(list_id=str(listName.id), user_id=results[i:i+10])

print "Created your new list here: http://twitter.com" + listName.uri
