from kafka import KafkaClient, KafkaProducer, KafkaConsumer
import csv
import json


client = KafkaClient("localhost:9092")

producer = KafkaProducer(bootstrap_servers='localhost:9092')

with open("train.csv") as file:
	reader = csv.reader(file)
	for row in reader:
		producer.send('the_topic', json.dumps(row).encode('utf-8'))





