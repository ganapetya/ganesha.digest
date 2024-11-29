from transformers import pipeline
class SimpleSummary:


  def __init__(self):
    # Choose a supported summarization model (e.g., T5)
    model_name = "t5-base"

    # Create the summarization pipeline within the constructor
    self.summarizer = pipeline("summarization", model=model_name, device=0, max_length=15)  # Use self.summarizer

  def summarize(self, text: str) -> str:
    return self.summarizer(text)
