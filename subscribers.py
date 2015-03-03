import os
import gdata.youtube
import gdata.youtube.service
import time


def GetUserUrl (username):

    yt_service = gdata.youtube.service.YouTubeService()
    uri = 'https://gdata.youtube.com/feeds/api/users/%s/subscriptions?max-results=50&start-index=1' % username
    subscription_feed = yt_service.GetYouTubeSubscriptionFeed(uri)
    T1 = GetUserSub(subscription_feed)
    final = 0
    j = 1
    total = 0
    while j<800:
      j = j + 50
      sj = str(j)
      uri = 'https://gdata.youtube.com/feeds/api/users/%s/subscriptions?max-results=50&start-index=' % username+sj
      subscription_feed = yt_service.GetYouTubeSubscriptionFeed(uri)
      T2 = GetUserSub(subscription_feed)
      total = total + T2

    final = total + T1
    usersub.writelines([str(username),',',str(final),'\n'])

def GetUserSub (subscription_feed):

  i = 0
  for entry in subscription_feed.entry:
    i = i +1
  return i

usersub = open ('usersubscribtions.csv','w')
users=[]
userlist = open("user_ids_noduplicates1.txt","r")
text1 = userlist.readlines()

for l in text1:
        users.append(l.strip().split()[0])
x = 0
while (x<len(users)):

 try:
    GetUserUrl(users[x])
    time.sleep(0.4)
    x = x+1
 except:
    usersub.writelines([str(users[x]),'\n'])
    x = x+1
    pass

usersub.close()