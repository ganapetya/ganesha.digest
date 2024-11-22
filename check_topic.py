from kafka import KafkaAdminClient
from kafka import KafkaConsumer

client = KafkaAdminClient(bootstrap_servers="localhost:9092")
topic_metadata = client.describe_topics(['ingest-events'])

from kafka import KafkaConsumer, TopicPartition

# Initialize KafkaConsumer
consumer = KafkaConsumer(
    bootstrap_servers="localhost:9092",
    group_id="my-group-id"
)

topic = "ingest-events"
partitions = [0]  # Replace with your partition IDs

# Create TopicPartition objects
topic_partitions = [TopicPartition(topic, p) for p in partitions]

# Assign the consumer to these partitions
consumer.assign(topic_partitions)

# Fetch end offsets
end_offsets = consumer.end_offsets(topic_partitions)

# Print the offsets
for tp, offset in end_offsets.items():
    print(f"End offset for partition {tp.partition} in topic '{tp.topic}': {offset}")
client.close()

