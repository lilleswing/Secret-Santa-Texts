from googlevoice import Voice
from googlevoice.util import input
import string
import random
import time

#  Sleep so we don't overload Google Voice
sleep_time = 5

class Person():
    def __init__(self, name, number):
        self.name = name
        self.number = number


def send(giver, reciever, voice,outfile):
    log_message = "%s,%s,%s" % (giver.name, reciever.name, giver.number)
    message = "%s your secret snowflake target is %s" % (giver.name, reciever.name)
    outfile.write("%s\n" % log_message)
    time.sleep(sleep_time)
    voice.send_sms(giver.number ,message)

def checkGroupings(people, enemies):
	for i in xrange(0, len(people)):
		grouping="%s:%s" % (people[i],people[i-1])
		reverse="%s:%s" % (people[i-1],people[i])
		if grouping in enemies or reverse in enemies:
			return False
	return True

def parse_people(filename):
    people = [x.strip().split(',') for x in open(filename,'r').readlines() ]
    people = [ Person(x[0], x[1]) for x in people]
    return people

def get_voice(filename):
    credentials = map(string.strip, open(filename,'r').readlines())
    voice = Voice()
    return voice
    voice.login(credentials[0], credentials[1])
    return voice

def parse_enemies(filename):
    enemies = set(map(string.strip, open(filename,'r').readlines()))
    return enemies

def get_ordering(people, enemies):
    random.shuffle(people)
    while(not checkGroupings(people, enemies)):
        random.shuffle(people)
    return people

def send_messages(people, voice, outfile):
    for i in xrange(0,len(people)):
        send(people[i],people[i-1],voice,outfile)
    outfile.close()

if __name__ == "__main__":
    people = parse_people("people.txt")
    enemies = parse_enemies("enemies.txt")
    voice = get_voice("credentials.txt")
    outfile = open('targets.txt','w')

    people = get_ordering(people, enemies)
    send_messages(people, voice, outfile)
