import json
from kafka import KafkaConsumer
from article_page import ArticlePage  # Import the ArticlePage class
from ganesh_translator import GaneshTranslator
from soup import clean
import torch
from simple_summary import SimpleSummary
# from summary import MBart50Summarizer
from nltk.tokenize import sent_tokenize
import nltk
nltk.data.path.append('/home/peter/work/ganapati/ganesha.digest/tokens')
nltk.download('punkt_tab', download_dir='/home/peter/work/ganapati/ganesha.digest/tokens')


# Kafka Consumer
def consume_messages():
    # Create Kafka consumer
    consumer = KafkaConsumer(
        'ingest-events',                 # Replace with your Kafka topic
        bootstrap_servers='localhost:9092', # Replace with your Kafka broker
        group_id='digest-consumer-3',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')), # Deserialize JSON
        auto_offset_reset='earliest'       # Start reading from the earliest message
    )

    translator = GaneshTranslator('en_XX','ru_RU') 
    #summarizer = MBart50Summarizer()
    summarizer = SimpleSummary()
    print("Consuming messages...")

    # Process messages
    for message in consumer:
        # Deserialize JSON to ArticlePage object
        data = message.value
        article = ArticlePage(
            title=data.get('title'),
            paragraphs=data.get('paragraphs', [])
        )

        torch.cuda.empty_cache()  

        print(clean(article.title))

        print(translator.translate(clean(article.title)))

        allText = ""
        for parag in article.paragraphs:
            allText+=clean(parag)
        
        sentences = regroup_sentences(allText, group_size=3)

        print("Regroupped sentences...")

        torch.cuda.empty_cache()       

        print("Process sentences...") 
        
        for parag in sentences:
            try:
                torch.cuda.empty_cache() 
                cleaned_par = clean(parag)

                print("PR " + parag)
                print("")
                torch.cuda.empty_cache()
                #print("PRT " + translator.translate(cleaned_par))
                #print("")
                word_count = len(cleaned_par.split())
                parag_summary = ""
                if word_count > 15 :
                    parag_summary = summarizer.summarize(text=cleaned_par)[0]['summary_text']
                else:
                    parag_summary = cleaned_par
                #print("PS " + parag_summary)
                print(f"PS {parag_summary}")

                print("")
                print("PST " + translator.translate(parag_summary))
                print("")
                
            except RuntimeError as e:
                print(f"RuntimeError at iteration: {e}")
                print("")
            finally:
                torch.cuda.empty_cache()

        
       # allText = ""
       # for parag in article.paragraphs:
       #     allText+=parag
       # 
       # 
       # torch.cuda.empty_cache()
       # 
       # cleaned_text = clean(allText)
       # print("TEXT " + cleaned_text)
       # print("TRANS " + translator.translate(cleaned_text))
       # text_summary = ""
       # word_count = len(cleaned_text.split())
       # if word_count > 100 :
       #     text_summary = summarizer.summarize(text=cleaned_text)[0]
       # else:
       #     text_summary = cleaned_par
       # print("SUMMARY " + parag_summary)
       # print("STRANS " + translator.translate(parag_summary))


          




        
        #print(all_translated_article)
                

            


               

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

