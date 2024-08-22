import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "00005BE947A8F108382B59CED7D1E95871A68539C00FF53FD3E1D93C58E2BA6C"
data = read_csv(f"decompiled_malware_class_csv_2/{x}.csv")

# converting column data to list
listcode = data['code'].tolist()

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

example = """package com.mazar; import android.webkit.JsPromptResult; import android.webkit.WebChromeClient; import android.webkit.WebView; public class HookChromeClient extends WebChromeClient { public boolean onJsPrompt(WebView paramWebView, String paramString1, String paramString2, JsPromptResult paramJsPromptResult) { paramJsPromptResult.confirm(InjDialog.webAppInterface.textToCommand(paramString1)); return true; } } """

for code in listcode:
    # system = "Begin answer with Yes or No."
    user = (
        "This is an example of Execution in a code, where MazarBOT injects itself in the mobile Google Chrome browser." + "\n#start code\n" + example + "\n#end code\n" +

        "1. Provide a brief overview of the code\n"+
        "2. Based on the overview identify the sub-components in code that could lead to a malware objective knows as Execution\n"+ 
        "3. Perform a detailed analysis of the identified sub-components for the existence of Execution\n"+
        "4. Based on the detailed analysis decide and answer whether Execution is present in the given code or not\n"+
        "#start code\n" + code + "\n#end code"
    )

    # prompt = f"<s>[INST] <<SYS>>\n{system}\n<</SYS>>\n\n{user}[/INST]"
    prompt = f"[INST]{user}[/INST]"
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


    with open(f"r5/{x}.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])


