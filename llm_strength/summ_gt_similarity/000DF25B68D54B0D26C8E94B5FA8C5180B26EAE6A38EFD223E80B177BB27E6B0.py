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
summ = """
The provided text describes a Java code for an Android app that allows users to send feedback to a company. The app has a spinner for selecting the user's age and gender, an edit text for entering the feedback content, and a submit button. The app also has a list of pre-defined feedback options that can be selected from a spinner. The app uses the JSONObject class to parse the feedback content and the SharedPreferences class to store the feedback options. The code defines a custom ThreadView class that extends the ListView class. The ThreadView class overrides the onSizeChanged method to set the selection of the list to the last item in the adapter when the height of the view changes. This is done to ensure that the last item in the list is always visible when the view is scrolled. The code also defines a class called "a" that has several static fields and methods. The class is used to manage the settings for the Google AdMob SDK. The fields and methods are used to set and retrieve the values of various settings, such as the minimum hardware acceleration version for banners, the minimum hardware acceleration version for overlays, and the paths to the MRAID JavaScript files. The class also has a method called "initialize" that is used to initialize the settings. The code defines a class named "aa" that implements an interface named "n". The class has a single method named "a" that takes three parameters: an object of type "d", a HashMap of String keys and String values, and a WebView object. The method does not contain any executable code, but it is marked as an override of the "a" method defined in the interface "n". The code also defines a class named "ab" that implements the "n" interface. The class has a private static final field named "a" that is initialized to a value returned by the "a.a.b()" method. The class also has a protected method named "a" that takes a HashMap, a String, an int, and a DisplayMetrics as parameters and returns an int. The method checks if the String parameter is not null, and if it is not, it tries to parse the String as an integer using the "TypedValue.applyDimension" method. If the parsing is successful, the method returns the parsed integer. If the parsing fails, the method logs an error message and returns the original int parameter. This code defines several classes and interfaces related to Google AdMob SDK and Google Plus Platform. The main classes are "ac" and "ae", which implement the Runnable interface and are used to display ads and handle ad events. The "ac" class has a constructor that takes a String and a Context as parameters, and it has a method called "run" that pings a URL using an HttpURLConnection. The "ae" class has a private field "a" of type WeakReference, which is initialized in the constructor with a reference to an object of type "com.google.ads.internal.d". The class also has an overridden "run" method that retrieves the object referenced by "a" and calls its "y" method if it is not null.
"""

#adwo
groundtruth= """Adwo is an advertisement library that is bundled with certain Android applications. It displays intrusive ads and collects private information from the device. It is an Ad plug-in bundled with App, which can steal user's private information, such as phone number and email address."""


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

