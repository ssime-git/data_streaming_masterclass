# consumer kafka
from kafka import KafkaConsumer
import json


# Librairie de l'analyse de sentiments
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Adresse IP de la VM
IP_VM = "54.155.132.78"


# instantiation du modèle
sentiment_analyzer = SentimentIntensityAnalyzer()

# instantiation du consumer
kafka_consumer = KafkaConsumer(
    "Twitter",
    bootstrap_servers=f"{IP_VM}:9092",
    auto_offset_reset="earliest"
)


for message in kafka_consumer:
    # view of the data being consumed
    print(message.value[:20], end="")

    # getting the messages
    dict_ = json.loads(message.value)

    # sentiment analysis
    score = sentiment_analyzer.polarity_scores(dict_["text"])["compound"]
    # col.insert_one(dict_)

    # writing in a file
    with open("sentiment_scores.txt", "a") as file:
        file.write(str(score) + "\n")