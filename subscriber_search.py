# Import the modules
import requests
import json

key = "AIzaSyD0Cl6YtiqkDsEzQvhXG6J-0zerEkFQbUY"

def search(key):

	q = raw_input("Search: ")

	api = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=%s&maxResults=20&key=%s" % (q, key)

	r = requests.get(api)
	r.text

	# Convert it to a Python dictionary
	data = json.loads(r.text)

	# Loop through the result. 
	for item in data['items']:

	    print "Subscriber Count: %s" % (item['snippet']['title'])

search(key)