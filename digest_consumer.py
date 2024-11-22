import json
from kafka import KafkaConsumer
from article_page import ArticlePage  # Import the ArticlePage class
from ganesh_translator import GaneshTranslator
from soup import clean

# Kafka Consumer
def consume_messages():
    # Create Kafka consumer
    consumer = KafkaConsumer(
        'ingest-events',                 # Replace with your Kafka topic
        bootstrap_servers='localhost:9092', # Replace with your Kafka broker
        group_id='digest-consumer-2',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')), # Deserialize JSON
        auto_offset_reset='earliest'       # Start reading from the earliest message
    )

    translator = GaneshTranslator('en_XX','he_IL') 
    
    print("Consuming messages...")

    # Process messages
    for message in consumer:
        # Deserialize JSON to ArticlePage object
        data = message.value
        article = ArticlePage(
            title=data.get('title'),
            paragraphs=data.get('paragraphs', [])
        )

        # Process the ArticlePage object
        print(article.to_content())

        print(translator.translate(clean(article.title)))
        for parag in article.paragraphs:
            print(translator.translate(clean(parag)))



if __name__ == '__main__':
    consume_messages()

