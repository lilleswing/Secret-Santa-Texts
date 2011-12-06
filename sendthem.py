from googlevoice import Voice
from googlevoice.util import input
import time
import string

def send(person1, person2, number,voice):
	message = "%s your secret snowflake target is %s" % (person1, person2)
	#print message
	voice.send_sms(number,message)

credentials = map(string.strip,open('credentials.txt','r').readlines())
voice = Voice()
voice.login(credentials[0],credentials[1])

people = open('targets.txt','r').readlines()
people = map(string.strip, people)
people = map(string.split, people, [',']*len(people))

for person in people:
	send(person[0],person[1],person[2],voice)
	time.sleep(5)
		

