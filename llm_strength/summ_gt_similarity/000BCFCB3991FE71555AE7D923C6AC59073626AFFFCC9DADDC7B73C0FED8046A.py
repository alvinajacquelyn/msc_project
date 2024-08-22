import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "000BCFCB3991FE71555AE7D923C6AC59073626AFFFCC9DADDC7B73C0FED8046A"
summ = """
This text describes several Java classes and interfaces, including "config", "configure", "myazcover", "progressbase", "RtspInfo", "utility", "A", and "AppWallManager". Each class has its own set of methods and fields, and they are used for various purposes such as configuration, file management, ad display, and app management. The classes use various design patterns, such as the Singleton pattern and the Handler class, to achieve their goals. Additionally, this code defines several classes in Java, including `B`, `C`, `C0001a`, `C0002b`, `C0003c`, `C0005e`, `C0006f`, `C0007g`, and `C0009i`. Each class has its own set of methods and fields, and they are used for various purposes such as working with JSON data, managing download tasks, and implementing encryption and decryption. The classes also have constructors and methods that take parameters and return values. This code defines several classes and interfaces in Java, including a class named "n" for generating a file path, a class named "o" with a private constructor and a static method for creating a new instance, an interface named "p" with a single method named "a" that takes two parameters, a class named "q" that implements the Runnable interface and has a public constructor that takes a Context, a String, a String, and a String, a class named "RunnableC0004d" that implements the Runnable interface and has a private field called "a" that is an instance of the AppWallManager class, a class named "s" for installing and launching Android apps, a class named "t" with a private constructor and a static method for returning a list of installed packages on the device, and a class named "u" that contains various static methods for retrieving information about the device, such as the manufacturer, model, IMEI, and screen resolution. This code defines several classes and interfaces for working with images, including a class named "v" that contains static methods for working with images, a custom "Handler" class named "w" that extends the Android "Handler" class, and an interface named "y" with no methods. The code also defines a class named "x" that implements the "Runnable" interface and a class named "a" that implements the "Runnable" interface and throws an "UnsupportedOperationException" with the message "Method not decompiled: com.feiwoone.banner.a.run():void". The code is a part of a class that extends "BroadcastReceiver" and is responsible for handling incoming broadcast intents, including checking for a connectivity change and updating the install count for all packages if the device is connected to the internet. This code defines several classes that implement various interfaces and handle different events. The classes include:

* "e" and "f" classes that implement the "OnClickListener" interface and handle button click events.
* "g" class that implements an interface named "l" from the "com.feiwoone.banner.e" package and handles location changes.
* "h" class that extends the "TimerTask" class and sends an empty message to a "Handler" object.
* "i" class that implements the "d" interface from the "com.feiwoone.banner.e" package and sets the background drawable of an "ImageView" object.
* "j" class that extends the "TimerTask" class and sends an empty message to a "Handler" object.
* "k" class that implements the "LocationListener" interface and handles location changes, provider disabled, and enabled events.
* "l" class that implements the "Runnable" interface and synchronizes on an object of type "k" and calls the "a" method on the "k" object with the AdBanner and Handler objects as arguments.

The text also describes a static method named "a" that takes a "Context" object as a parameter and returns an integer value based on the device's network connectivity.
"""

#dowgin
groundtruth = """Dowgin is an advertisement library that is bundled with certain Android applications. It is a malicious advertising module that is distributed and bundled with other (usually legitimate) programmes. The advertising module is used to display advertising content while also silently gathering and forwarding information from the device. Dowgin provides users with advertising content. If the user is unaware of the module’s presence or objects to the nature of the advertising materials displayed, this behaviour may be considered unwanted. The module may also silently leak or harvest sensitive device information such as the device’s International Mobile Equipment Identity (IMEI) number, location, contacts, and so on."""


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

