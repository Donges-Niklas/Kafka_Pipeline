from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('the_topic')

for msg in consumer:
	decoded_msg = msg.value.decode("utf-8")
	print(decoded_msg)



















































# Sandbox Code

"""
import csv
 
with open('persons.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for msg in consumer:
    	va = msg.value
    	vad = va.decode("utf-8")
    	print(vad)
    	spamwriter.writerow(vad)

"""





