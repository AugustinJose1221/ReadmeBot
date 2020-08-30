# ReadmeBot
A simple automation to display your most recent tweet in your Github ReadME

# Setup Guide

## Twitter API

* Create a [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access)
* Create a Twitter App
* Generate and copy the key, secret and tokens

## Twitter Cards

* Go to [Twitter Cards](https://publish.twitter.com/#)
* Enter the link to your recent tweet and generate its Twitter Card
* Take a screenshot and crop the top and bottom parts of the Twitter Card
* Go to `api/templates`
* Replace the files `top.png` and `bottom.png` with these new files

## Vercel

* Register on [Vercel](https://vercel.com/)
* Create a project linked to your Github repo
* Add the following System Variable:
  * `CONSUMER_KEY`
  * `CONSUMER_SECRET`
  * `ACCESS_KEY`
  * `ACCESS_SECRET`
  * `USERNAME`
* Deploy
