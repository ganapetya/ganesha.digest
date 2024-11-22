from transformers import MBartForConditionalGeneration, MBart50Tokenizer

class GaneshTranslator:
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name).to("cuda")
    tokenizer = MBart50Tokenizer.from_pretrained(model_name)

    def __init__(self, sl: str, tl: str):
        self.sl = sl
        self.tl = tl
        self.tokenizer.src_lang = sl

    def translate(self, sentence: str) -> str:
        encoded_input = self.tokenizer(sentence, return_tensors="pt").to("cuda")
        generated_tokens = self.model.generate(
            **encoded_input, 
            forced_bos_token_id=self.tokenizer.lang_code_to_id[self.tl]
        )
        return self.tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

