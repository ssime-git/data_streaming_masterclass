"""
Producer function
"""
# Libraries
import json
import time
import random
from tqdm import tqdm
from kafka import KafkaProducer

# Path to the data & VM
FILE_PATH = "./data/large_tweets.json"
IP_VM = "54.155.132.78"

# instantiate the kafka producer
kafkaProducer = KafkaProducer(bootstrap_servers=f"{IP_VM}:9093") # VM IP Address "54.77.61.22:9093"

# Open and close the file
with open(FILE_PATH, 'r') as file:
    tweets = json.load(file)

# computing the numer of tweets
n_tweets = len(tweets)

# Loop over the file
for i in tqdm(range(1, 3000)):
    time.sleep(.5)
    kafkaProducer.send(
        topic="Twitter",
        value=json.dumps(tweets[random.randint(0, n_tweets)-1]).encode("utf-8")
    )

# Envoi des messages en instantanné
kafkaProducer.flush()