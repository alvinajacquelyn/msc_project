import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0007DB1488BE0F1AE760BD9FEC68153DDEC6D692F3371A395D9F8822FFEC0935"
data = read_csv(f"output_table/{x}.csv")

# converting column data to list
summ = data['summ'].tolist()
d3 = data['d3'].dropna().tolist()
# # printing list data
# print(listcode)

# Load the tokenizer and model
model_name = "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
)



for y in range(len(d3)):
    system = "Assign a coherence score for d3 on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the coherence criteria. Coherence refers to the collective quality of all sentences. Align this dimension with the DUC quality question of structure and coherence whereby d3 should be well-structured and well-organized. d3 should not just be a heap of related information, but should build from sentence to a coherent body of information about a topic."
    user = ("[Start summary]\n"+str(summ[y])+"\n[End summary]\n\n"+"[Start d3]\n"+str(d3[y])+"\n[End d3]\n\n"+
            "Output the coherence score for d3 on a scale of 1 to 5 (i.e., /5).")
    
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


    with open(f"llmasjudge_d3/{x}_d3_coherence.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])