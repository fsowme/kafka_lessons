from confluent_kafka.admin import NewTopic, AdminClient

admin = AdminClient({'bootstrap.servers': 'localhost:9095'})

replicated_topic = NewTopic(
    topic="replicated_topic_qwessss",
    num_partitions=5,
    replication_factor=2
)

try:
    res = admin.create_topics(new_topics=[replicated_topic], validate_only=False)
    for topic, r in res.items():
        r.result()
    print("Topic created successfully")
except Exception as error:
    print(error)
