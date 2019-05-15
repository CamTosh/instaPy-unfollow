import os
import json
import logging
import argparse
from dotenv import load_dotenv
from instapy import InstaPy

load_dotenv('.env')

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

class Unfollow(object):

	def __init__(self, unfollow):
		self.session = InstaPy(username=USERNAME, password=PASSWORD, headless_browser=True)
		self.usersToUnfollow = self.load(unfollow)
		
	
	def unfollowAccounts(self, chunk):
		usersChunk = self.chunks(self.usersToUnfollow, chunk)

		for users in list(usersChunk):
			self.session.unfollow_users(amount=chunk, customList=(True, users, "all"), sleep_delay=600)


	def load(self, filename):
		try:
			file = open(filename, encoding='utf8')
			data = json.load(file)
			file.close()
			print("Load {} accounts to unfollow".format(len(filename)))
			return data
		except Exception as e:
			print("Can't load data from " + filename + ", error :")
			logging.exception(e)


	def chunks(self, seq, n):
	    return (seq[i:i+n] for i in range(0, len(seq), n))


if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("--unfollow", type=str, required=True, help="Non followers json file")
	ap.add_argument("--chunk", type=int, required=False, help="Number of users in unfollowing session (default: 50)")
	
	args = vars(ap.parse_args())

	if args['chunk'] != None:
		chunkOf = int(args['chunk'])
	else:
		chunkOf = 50

	unfollow = Unfollow(args['unfollow'])
	unfollow.unfollowAccounts(chunkOf)
	
	print("Completed")