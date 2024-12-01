from confluent_kafka.admin import NewTopic, AdminClient

admin = AdminClient({'bootstrap.servers': 'localhost:9095'})

replicated_topic = NewTopic(
    topic="replicated_topic_qwe",
    num_partitions=5,
    replication_factor=2
)

try:
    admin.create_topics([replicated_topic])
    print("Topic created successfully")
except Exception as error:
    print(error)
