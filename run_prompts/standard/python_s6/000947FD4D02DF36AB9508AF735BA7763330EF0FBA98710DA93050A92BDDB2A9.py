import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "000947FD4D02DF36AB9508AF735BA7763330EF0FBA98710DA93050A92BDDB2A9"
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
    system = "Begin answer with Yes or No."
    user = (
        "This is an example of Execution in a code, where MazarBOT injects itself in the mobile Google Chrome browser." + "\n#start code\n" + example + "\n#end code" +
        "You are a malware expert who analyses if code contains instances of the malware objective known as Execution. " +
        "Explain in 100 words." + "\n#start code\n" + code + "\n#end code"
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


    with open(f"s6/{x}.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([tokenizer.decode(output)])


