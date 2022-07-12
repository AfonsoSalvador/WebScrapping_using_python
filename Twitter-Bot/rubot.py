import os 
import tweepy
import time
import random
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
acess_token = os.getenv("acess_token")
acess_token_secret = os.getenv("acess_token_secret")


