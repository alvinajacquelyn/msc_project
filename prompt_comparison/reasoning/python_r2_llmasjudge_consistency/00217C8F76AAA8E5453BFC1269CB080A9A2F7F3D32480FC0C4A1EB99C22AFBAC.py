import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "00217C8F76AAA8E5453BFC1269CB080A9A2F7F3D32480FC0C4A1EB99C22AFBAC"
data = read_csv(f"output_table/{x}.csv")

# converting column data to list
summ = data['summ'].tolist()
r2 = data['r2'].dropna().tolist()
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



for y in range(len(r2)):
    system = "Assign a consistency score for r2 on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the consistency criteria.  "
    user = ("[Start context]\n"+str(summ[y])+"\n[End context]\n\n"+"[Start r2]\n"+str(r2[y])+"\n[End r2]\n\n"+
    "Evaluation criteria:\nConsistency refers to the factual alignment between of r2 against the context. If any claims are made in r2 that cannot be deduced from context (i.e., hallucinations), then these will be penalized.\nOutput the consistency score for r2 on a scale of 1 to 5 (i.e., /5)."
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


    with open(f"llmasjudge_r2/{x}_r2_consistency.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])