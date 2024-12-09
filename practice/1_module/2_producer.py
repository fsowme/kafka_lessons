from confluent_kafka import Producer

CONF = {
    'bootstrap.servers': 'localhost:9094',
}

producer = Producer(CONF)

producer.produce(
    topic='some-topic', key='key-1', value='message-1'
)
producer.flush()
