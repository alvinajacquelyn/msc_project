import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "000DF25B68D54B0D26C8E94B5FA8C5180B26EAE6A38EFD223E80B177BB27E6B0"
data = read_csv(f"output_table/{x}.csv")

# converting column data to list
summ = data['summ'].tolist()
s1 = data['s1'].dropna().tolist()
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



for y in range(len(s1)):
    system = "Assign a consistency score for s1 on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the consistency criteria.  "
    user = ("[Start context]\n"+str(summ[y])+"\n[End context]\n\n"+"[Start s1]\n"+str(s1[y])+"\n[End s1]\n\n"+
    "Evaluation criteria:\nConsistency refers to the factual alignment between of s1 against the context. If any claims are made in s1 that cannot be deduced from context (i.e., hallucinations), then these will be penalized.\nOutput the consistency score for s1 on a scale of 1 to 5 (i.e., /5)."
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


    with open(f"llmasjudge_s1/{x}_s1_consistency.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])