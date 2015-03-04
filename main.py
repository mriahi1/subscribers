# Import the modules
import requests
import json

# Make it a bit prettier..
print "-" * 30
print "This will show the Most Popular Videos on YouTube"
print "-" * 30

# Get the feed
key = "AIzaSyD0Cl6YtiqkDsEzQvhXG6J-0zerEkFQbUY"
channel = "UC6nSFpj9HTCZ5t-N3Rm3-HA&"


def sub_count(key, channelID):
  
  api = "https://www.googleapis.com/youtube/v3/"
  api += "channels?part=statistics&id=%s&key=%s" % (channelID, key)

  r = requests.get(api)
  r.text

  # Convert it to a Python dictionary
  data = json.loads(r.text)

  # Loop through the result. 
  for item in data['items']:
      print "Subscriber Count: %s" % (item['statistics']['subscriberCount'])

def search(key):

  q = raw_input("Search: ")
  api = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=%s&maxResults=20&key=%s" % (q, key)
  r = requests.get(api)
  r.text

  # Convert it to a Python dictionary
  data = json.loads(r.text)

  # Loop through the result. 
  for item in data['items']:
      results =  "results: %s" % (item['snippet']['title'])
      print results

  choice = int(raw_input("which one do you want a subscriber count for (1-5): "))

  return data['items'][choice - 1]['snippet']['channelId']
#search(key)

channelID = search(key)

sub_count(key, channelID)









