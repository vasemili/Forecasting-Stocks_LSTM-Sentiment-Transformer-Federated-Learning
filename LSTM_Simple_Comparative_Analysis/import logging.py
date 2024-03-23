import logging
import uuid

from producer import KafkaJsonProducer
import json

import os

os.environ['Kafka_host'] = "url:9902"
os.environ['Cluster_key'] = 'key_num'
os.environ['Cluster_secret'] = 'secret'

class DataClass:
    def __init__(self) -> None:
        self.message = 'Emilio Vasquez'

class JsonProducer:
    def __init__(self):
        self.json_producer = KafkaJsonProducer(producer_client_id = 'python-sample')
    
    def produce_json_message(self, msg):
        test_message = msg
        return self.json_producer.send(topic_name = 'example', key = str(uuid.uuid4()), value = test_message)

data = DataClass()
Json_producer = JsonProducer()
Json_producer.produce_json_message(data)