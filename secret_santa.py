from googlevoice import Voice
from googlevoice.util import input
import string
import random

def send(person1, person2, voice,outfile):
	message = "%s your secret snowflake target is %s" % (person1[0], person2[0])
	outfile.write("%s,%s,%s\n" % (person1[0],person2[0],person1[1]))
	voice.send_sms(person1[1],message)

def checkGroupings(people,enemies):
	for i in xrange(0, len(people)):
		grouping="%s:%s" % (people[i],people[i-1])
		reverse="%s:%s" % (people[i-1],people[i])
		if grouping in enemies or reverse in enemies:
			return False
	return True

credentials = map(string.strip,open('credentials.txt','r').readlines())
voice = Voice()
voice.login(credentials[0],credentials[1])

people = open('people.txt','r').readlines()
people = map(string.strip, people)
people = map(string.split, people, [',']*len(people))
outfile = open('targets.txt','w')

enemies = set(map(string.strip,open('enemies.txt','r').readlines()))
random.shuffle(people)
while(not checkGroupings(people,enemies)):
	random.shuffle(people)	
for i in xrange(0,len(people)):
	send(people[i],people[i-1],voice,outfile)

outfile.close()
