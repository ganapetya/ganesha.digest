from transformers import MBartForConditionalGeneration, MBart50Tokenizer

# Load the model and tokenizer
model_name = "facebook/mbart-large-50-many-to-many-mmt"
model = MBartForConditionalGeneration.from_pretrained(model_name).to("cuda")
tokenizer = MBart50Tokenizer.from_pretrained(model_name)

# Example: Translate from Ukr to Eng
tokenizer.src_lang = "uk_UA"

input_text1 = "За словами Путіна, засоби протиповітряної оборони нібито не здатні перехопити цю ракету"
input_text2 = "Російський диктатор Володимир Путін заявив, що під час ранкової атаки по Дніпру Росія застосувала ракету середньої дальності \"Орєшнік\"."
input_text3 = "Про це він заявив у своєму зверненні 21 листопада."
input_text4 = "За словами Путіна, \"Орєшнік\" нібито вразив один із найбільших промислових комплексів у Дніпрі, який виробляє \"ракетну техніку\" та іншу зброю"
input_text5 = "Це була нібито \"відповідь Росії\" на удари України по об'єктах у Курській та Брянській областях \"ракетами ATACMS\" 19 та 21 листопада."
input_text6 = "Російський диктатор заявив, що Росія розробляє ракети середньої та меншої дальності як так званий захід у відповідь на плани США розгорнути аналогічні ракети в Європі та Азійсько-Тихоокеанському регіоні."

arr = [input_text1, input_text2, input_text3, input_text4, input_text5, input_text6]

for x in arr:
    encoded_input = tokenizer(x, return_tensors="pt").to("cuda")
    generated_tokens = model.generate(**encoded_input, forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"])
    output_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    print(output_text)
