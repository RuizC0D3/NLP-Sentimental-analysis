 # -*- coding: utf-8 -*-
"""
D4V1D TEST
"""

import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import tweepy
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener claves desde las variables de entorno
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Autenticación con la API de X (Twitter)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Prueba: Obtener tu usuario de X
user = api.verify_credentials()
print(f"Autenticado como: {user.screen_name}")