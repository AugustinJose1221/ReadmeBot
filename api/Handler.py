#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:40:17 2020

@author: augustinjose
"""


from flask import Flask, Response, jsonify, render_template, request, redirect, url_for
import tweepy as tw

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
    return status.id
    
        
def makeTweet():
    ID = TweetInfo(username)
    link = "<a href=\"https://twitter.com/"+username+"/status/"+str(ID)+"\"></a>"
    #print(link)
    return link #render_template("test.html", link=link)
    
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("test.html", link=makeTweet())

if __name__ == "__main__":
    app.run(debug=True)
