import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0035A5643659FA79FE081675C43476E8BCDD4634E2AB262D152E4FF7A3331BA5"
data = read_csv(f"output_table/{x}.csv")

# converting column data to list
summ = data['summ'].tolist()
d2 = data['d2'].dropna().tolist()
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



for y in range(len(d2)):
    system = "Assign a relevance score for d2 on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the relevance criteria."
    user = ("[Start prompt]\n"+"Is this code malicious?"+"\n[End prompt]\n\n"+"[Start d2]\n"+str(d2[y])+"\n[End d2]\n\n"+
    "\nEvaluation criteria:\nRelevance refers to the degree to which d2 directly addresses the prompt. This does not take the factuality of d2 into consideration, but penalizes the presence of redundant information or incomplete answers given the prompt.\nOutput the relevance score for d2 on a scale of 1 to 5."
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


    with open(f"llmasjudge_d2/{x}_d2_relevance.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])