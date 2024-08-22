import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
from pandas import read_csv
import csv


# Load the tokenizer and model
model_name = "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
)

system = "Begin answer with Yes or No."

text1 = "You are a malware expert who analyses if code contains instances of the malware objective known as Execution. Begin answer with Yes or No."
text2 = "You are a malware expert. Does this code contain instances of the malware objective known as Execution?"
user = (
        f"This is first text: (start) {text1} (end)\n. This is second text: (start) {text2} (end)\n. Are there any similarities between the two texts? Explain in 100 words."
)

prompt = f"<s>[INST] <<SYS>>\n{system}\n<</SYS>>\n\n{user}[/INST]"
# prompt = f"[INST]{user}[/INST]"
inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to("cuda")

# Generate code with a specified max_length
output = model.generate(
    inputs["input_ids"],
    max_new_tokens=4096,
    do_sample=True,
    temperature=0.1,
    top_p=0.95,
)
output = output[0].to("cpu")
print(tokenizer.decode(output)) 


with open(f"misc/s3_s5_similarity.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow([tokenizer.decode(output)])
