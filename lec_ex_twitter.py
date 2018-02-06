from requests_oauthlib import OAuth1Session
import lec_secret_data
import json

consumer_key = lec_secret_data.CONSUMER_KEY
consumer_secret = lec_secret_data.CONSUMER_SECRET
access_token = lec_secret_data.ACCESS_KEY
access_secret = lec_secret_data.ACCESS_SECRET

url = "https://api.twitter.com/1.1/account/verify_credentials.json"
oauth = OAuth1Session(consumer_key, consumer_secret, access_token, access_secret)

baseurl = "https://api.twitter.com/1.1/search/tweets.json"
params = {"q": "super bowl"}
resp = oauth.get(baseurl, params = params)

resp_dict = json.loads(resp.text)

for each_dic in resp_dict["statuses"]:
	print (each_dic["user"]["name"] + ":")
	print(each_dic["text"])
	print ("--------")
