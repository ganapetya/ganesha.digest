import json
from kafka import KafkaConsumer
from article_page import ArticlePage  # Import the ArticlePage class
from ganesh_translator import GaneshTranslator
from soup import clean
from summary import MBart50Summarizer
from nltk.tokenize import sent_tokenize
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
    summarizer = MBart50Summarizer()
    
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
            cleaned_txt = translator.translate(clean(parag))
            sentences = regroup_sentences(cleaned_txt, 1)
            par_summary = ""
            for group in sentences:
                par_summary += summarizer.summarize(group, source_lang="he_IL", max_length=60, min_length=30)
            print("paragraph:\n")
            print(cleaned_txt)
            print("summary:\n")
            print(par_summary)
               

def regroup_sentences(text, group_size=2):
    # Split text into individual sentences
    sentences = sent_tokenize(text)
    
    # Group sentences into chunks of the specified size
    grouped_sentences = [
        " ".join(sentences[i:i + group_size])
        for i in range(0, len(sentences), group_size)
    ]
    
    return grouped_sentences


if __name__ == '__main__':
    consume_messages()

