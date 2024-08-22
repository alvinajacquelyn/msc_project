import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "00058E5CA57BA774DFB98B4661095F88E4DAA1A8E7A8D19B81D84D7E42868CFB"
data = read_csv(f"output_table/{x}.csv")

# converting column data to list
summ = data['summ'].tolist()
s0 = data['s0'].dropna().tolist()
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



for y in range(len(s0)):
    system = "Assign a relevance score for s0 on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the relevance criteria."
    user = ("[Start prompt]\n"+"Is this code malicious?"+"\n[End prompt]\n\n"+"[Start s0]\n"+str(s0[y])+"\n[End s0]\n\n"+
    "\nEvaluation criteria:\nRelevance refers to the degree to which s0 directly addresses the prompt. This does not take the factuality of s0 into consideration, but penalizes the presence of redundant information or incomplete answers given the prompt.\nOutput the relevance score for s0 on a scale of 1 to 5."
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


    with open(f"llmasjudge_s0/{x}_s0_relevance.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])
