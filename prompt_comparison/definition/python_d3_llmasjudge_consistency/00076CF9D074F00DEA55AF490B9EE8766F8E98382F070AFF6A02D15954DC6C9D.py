import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "00076CF9D074F00DEA55AF490B9EE8766F8E98382F070AFF6A02D15954DC6C9D"
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
    system = "Assign a consistency score for d3 on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the consistency criteria.  "
    user = ("[Start context]\n"+str(summ[y])+"\n[End context]\n\n"+"[Start d3]\n"+str(d3[y])+"\n[End d3]\n\n"+
    "Evaluation criteria:\nConsistency refers to the factual alignment between of d3 against the context. If any claims are made in d3 that cannot be deduced from context (i.e., hallucinations), then these will be penalized.\nOutput the consistency score for d3 on a scale of 1 to 5 (i.e., /5)."
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


    with open(f"llmasjudge_d3/{x}_d3_consistency.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])