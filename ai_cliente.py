from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

def gerar_frase_motivacional(tema: str = "motivation") -> str:
    prompt = f"Motivational quote about {tema} in one sentence:"
    
    # tokenizar com attention_mask
    encoding = tokenizer(prompt, return_tensors="pt")
    input_ids = encoding.input_ids
    attention_mask = encoding.attention_mask
    
    # gerar saída
    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=40,
        do_sample=True,
        temperature=0.9,
        top_p=0.95,
        top_k=50,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # decodificar
    frase = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return frase.strip()

