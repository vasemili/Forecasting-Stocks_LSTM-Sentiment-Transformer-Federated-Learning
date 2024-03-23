from consumer import KafkaStringConsumer
from flask.streaming.string.string_message_processor import StringRecordProcessor

bootstrap_server = 'server_url'
consumer = KafkaStringConsumer(bootstrap_servers=bootstrap_server)

def consume_string_message():
    string_consumer = KafkaStringConsumer(consumer_group_id='dotnet')
    string_consumer.consume_message(topic_name='Java-example',
                                   dlq_topic='Java-example.dlq',
                                   processor=StringRecordProcessor())

# Call the consume_string_message() function to start consuming messages
consume_string_message()
