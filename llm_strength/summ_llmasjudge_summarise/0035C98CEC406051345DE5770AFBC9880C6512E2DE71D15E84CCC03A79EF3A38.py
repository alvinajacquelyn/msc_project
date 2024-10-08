import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file
from pandas import read_csv

x = "0035C98CEC406051345DE5770AFBC9880C6512E2DE71D15E84CCC03A79EF3A38"
data = read_csv(f"llmasjudge_summarise/{x}_summarise_recursive_sentence.csv")

# Converting column data to list and filtering out NaN values
summ = data['extracted_text'].dropna().tolist()

# Ensure all elements are strings
summ = [str(item) for item in summ]

combined_list = []
temp_string = ''
for i in range(len(summ)):
    temp_string += str(summ[i]) + ' '
    if (i + 1) % 3 == 0:
        combined_list.append(temp_string.strip())
        temp_string = ''

# Add any remaining elements in temp_string if they exist
if temp_string:
    combined_list.append(temp_string.strip())

# Load the tokenizer and model
model_name = "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
)



for combined in combined_list:
    system = "Your task is to generate a summary of the provided text within 100 words, focusing on the overall content and key points. Please avoid including any code in your summary."
    user = "Write a concise summary of the following text, which includes a concatenation of summaries for each class of code. The text starts after 'start' and ends before 'end':\n\n(start)\n"+combined+"\n(end)\n"

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



    with open(f"llmasjudge_summarise_2/{x}_summarise_recursive_sentence.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])