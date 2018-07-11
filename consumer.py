from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('the_topic')

for msg in consumer:
	decoded_msg = msg.value.decode("utf-8")
	print(decoded_msg)
