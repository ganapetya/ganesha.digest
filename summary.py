from transformers import MBartForConditionalGeneration, MBart50Tokenizer
from torch.cuda.amp import autocast
class MBart50Summarizer:
    def __init__(self, model_name: str = "facebook/mbart-large-50-many-to-many-mmt", device: str = "cuda"):
        """
        Initializes the MBart50 summarizer.

        Args:
            model_name (str): The Hugging Face model to use for summarization.
            device (str): The device to use, "cuda" or "cpu".
        """
        self.device = device
        self.model = MBartForConditionalGeneration.from_pretrained(model_name).to(self.device)

        self.tokenizer = MBart50Tokenizer.from_pretrained(model_name)

    def summarize(self, text: str, source_lang: str, max_length: int = 100, min_length: int = 30) -> str:
        """
        Summarizes the given text.

        Args:
            text (str): The input text to summarize.
            source_lang (str): Source language code (e.g., "en_XX").
            max_length (int): Maximum length of the summary.
            min_length (int): Minimum length of the summary.

        Returns:
            str: The summarized text.
        """
        # Set source language
        self.tokenizer.src_lang = source_lang

        # Tokenize the input text
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True).to(self.device)

        # Generate the summary
        # here used autocast to manage memory, could be deleted
        with autocast():
            summary_ids = self.model.generate(
                **inputs,
                max_length=max_length,
                min_length=min_length,
                forced_bos_token_id=self.tokenizer.lang_code_to_id[source_lang]
            )

        # Decode the summary
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)


    #if __name__ == "__main__":
    # Example usage
    #summarizer = MBart50Summarizer()

    # Sample input text (replace with your own)
    #input_text = """
    #Artificial intelligence (AI) refers to the simulation of human intelligence in machines 
    #that are programmed to think like humans and mimic their actions. The term may also be 
    #applied to any machine that exhibits traits associated with a human mind such as learning 
    #and problem-solving. AI is an interdisciplinary science with multiple approaches, but advancements 
    #in machine learning and deep learning are creating a paradigm shift in virtually every sector of the 
    #tech industry.
    #"""

    # Summarize the text
    #summary = summarizer.summarize(input_text, source_lang="en_XX", max_length=60, min_length=30)
    #print("Summary:")
    #print(summary)

