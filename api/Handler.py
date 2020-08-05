#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:40:17 2020

@author: augustinjose
"""


from flask import Flask, Response, jsonify, render_template, request, redirect, url_for
import tweepy as tw
import requests
from base64 import b64encode

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


import os
import random
consumer_key = str(os.getenv("CONSUMER_KEY"))
consumer_secret = str(os.getenv("CONSUMER_SECRET"))
key = str(os.getenv("ACCESS_KEY"))
secret = str(os.getenv("ACCESS_SECRET"))
username = str(os.getenv("USERNAME"))

app = Flask(__name__)


def OAuth():
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    return api

def TweetInfo(target):
    conn = OAuth()
    for status in tw.Cursor(conn.user_timeline, id=target).items(1):
        pass
    return [status.text, status.entities, status.created_at]
    
def loadImageB64(url):
    resposne = requests.get(url)
    return b64encode(resposne.content).decode("ascii")

def makeTweet():
    details = TweetInfo(username)
    time = details[2]
    tweet = details[0]
    hashtag = details[1]["hashtags"]
    hashtags = []
    for i in hashtag:
        hashtags.append("#"+str(i["text"]))
    user_mention = details[1]["user_mentions"]
    user_mentions = []
    for j in user_mention:
        user_mentions.append("@"+str(j["screen_name"]))
    
    for i in hashtags:
        tweet = tweet.replace(i, "<span>"+str(i)+"</span>")
    for i in user_mentions:
        tweet = tweet.replace(i, "<span>"+str(i)+"</span>")
        
    top = loadImageB64("https://raw.githubusercontent.com/AugustinJose1221/ReadmeBot/master/api/templates/top.png")
    bottom = loadImageB64("https://raw.githubusercontent.com/AugustinJose1221/ReadmeBot/master/api/templates/bottom.png")
    return render_template("tweet.html.j2", top=top, bottom=bottom, tweettext=tweet, date_time=time)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    
    svg=makeTweet()
    resp = Response(svg, mimetype="image/svg+xml")
    resp.headers["Cache-Control"] = "s-maxage=1"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
