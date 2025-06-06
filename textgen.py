from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to generate text
def generate_text(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    attention_mask = input_ids.ne(tokenizer.pad_token_id).long()

    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id,  
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)

prompt = str(input("Enter the prompt:\n"))
max_len = int(input("Enter maximum limit of words:\n"))
generated_text = generate_text(prompt, max_length=max_len)
print("\nGenerated Text:\n", generated_text)
