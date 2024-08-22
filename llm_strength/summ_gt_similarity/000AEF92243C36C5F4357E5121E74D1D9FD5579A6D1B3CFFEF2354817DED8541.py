import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "000AEF92243C36C5F4357E5121E74D1D9FD5579A6D1B3CFFEF2354817DED8541"

summ = """
The text describes several Java classes and interfaces used to create and manage notifications on an Android device. The classes and interfaces include:

* AppWallManager: A class that manages the display of an app wall.
* C0000a: A class with methods for working with JSON data.
* C0001b: A class with three static methods.
* C0002c: A class that implements an interface named "p".
* C0004e: A class with a method that takes a byte array and a boolean parameter and returns a string.
* C0005f: A class with several methods and fields related to network information.
* C0006g: A class that implements a download manager.
* C0008i: A class that implements encryption and decryption using the DES algorithm.
* C0009j: A class that extends Thread and is used to download files from a server.
* D: A class with two static methods for generating random strings and checking if a string is null.
* E: A class that implements the DownloadListener interface and does nothing in the onDownloadStart method.
* F: A custom WebChromeClient class that extends the default WebChromeClient class and logs a message to the console when the progress reaches 100%.
* G: A custom WebViewClient class that extends the default WebViewClient class and loads a custom HTML string into the web view when there is an error loading the page.
* H: A class that implements the Runnable interface and calls the finish() method on the a field.
* I: A class that implements the Runnable interface and calls the a() and b() methods on the a field, passing in the ApplicationContext and the String value of the b field.
* J: A class that implements the Runnable interface and calls the C.b() method with the application context, "DP_AW_FILE", the value of the b field, the value of the c field, and the current time in milliseconds. It then calls the n.a() method with the application context, "/adfeiwo/appwall/apk", and the value of the d field. Finally, it calls the s.a() method and the s.a() method with the application context and the value returned by the n.a() method.
* K: A class that implements the Runnable interface and shows a toast message.
* l: A class that implements the Runnable interface and performs various actions, including checking if a field is false and creating an Intent with a specific action and flag.
* m: A class that implements the Runnable interface and creates a new instance of a class and calls a method on it, passing in several parameters.
* n: A class with a static method that returns a String and has a private static field initialized to null.
* o: A class with a private constructor and a static method that returns an instance of the class.
* p: An interface with a single method that takes two parameters.
* q: A class that implements the Runnable interface and has several instance variables and methods.
* RunnableC0003d: A class that implements the Runnable interface and creates a new Intent object and starts the activity using the "startActivity()" method.
* s: A class that provides methods for installing and launching apps on an Android device.

The text also describes an interface named "y" with no methods or properties, and a class named "z" with a static method "a" that calculates the density of the device's screen. The classes are used for various purposes, such as creating and managing notifications, parsing a string as an integer, retrieving a list of installed packages, retrieving information about the device, loading and manipulating images, and handling messages of type `Message`.
"""

#revmob
groundtruth = """RevMob is an advertisement library that is bundled with certain Android applications. It collects the personal information and browser history of the victim and redirects victims to malicious websites. Furthermore, Revmob will display obnoxious ads and exhibit similar behaviour to Airpush"""

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



system = "Begin answer with Yes or No."
user = (
    f"Are there any similarities between the two texts? Each text starts after 'start' and ends before 'end':\n\nThis is first text: (start) {summ} (end)\nThis is second text: (start) {groundtruth} (end)\n"
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


with open(f"summ_gt_similarity/{x}_malicious_sem_sim.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow([tokenizer.decode(output)])

