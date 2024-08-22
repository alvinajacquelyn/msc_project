import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0013121BFDC7CC7E21401F95144EF56AF783F20477748E488725A1CFF68BB2B7"
summ = """
The provided text describes several Java classes and interfaces used in an Android app to display a banner ad. These classes and interfaces include `k` that implements the `g` interface, `l` that extends the `ShapeDrawable.ShaderFactory` class, and `n` that implements the `Runnable` interface. These classes and interfaces are used to manage shared preferences, implement interfaces, display progress bars, and interact with the AppBrain SDK. The code also defines several inner classes, including a `b` class that represents a `ProgressBar` and an `e` class that represents an `ImageView`. The code also defines several static fields and methods, including a `a` method that returns a `Drawable` object and a `b` method that returns a `Drawable` object. This code defines several classes and interfaces, including "u" and "v", which are used to send data to a server and display a message to the user when an ad is clicked, respectively. The "u" class has a nested enum called "a" that represents the different sizes of images available on Google Photos, and a static method called "a" that takes a string, an integer, and an instance of the "a" enum as input and returns a string that represents the URL of the image with the specified size. The "v" class has a static method named "a" that takes two parameters: "i" and "str", and it returns a string based on the value of "i" and the language code "str". The "y" class implements the "View.OnClickListener" interface and has a constructor that takes an instance of "x" as a parameter, and it has an "onClick" method that is called when the view is clicked. The "onClick" method performs a series of actions, including calling the "a" method on the "x" instance, setting a string variable to the value of the "d" field of the "x" instance, and calling the "a" method on the "x" instance again. The "onClick" method also finishes the activity. The "z" class implements the "ViewTreeObserver.OnGlobalLayoutListener" interface and has two fields: "a" of type "Button" and "b" of type "x". The constructor takes two arguments: "xVar" of type "x" and "button" of type "Button". The "onGlobalLayout" method is defined, which gets called when the global layout of the view tree changes. The method first creates a new "Rect" object and then checks if the "Button" is visible in the current view tree. If it is, the method calls the "a" method of "x" with the center X and Y coordinates of the "Button" as arguments.
"""

groundtruth = """Airpush is a very aggresive Ad - Network. It is an Android app that contains a third-party advertising component which displays advertising content in the device's notification panel. The module may also silently gather and forward details from the device. The third-party advertising component in Airpush programs displays advertising content in the device's notification panel. This behavior may be considered unwanted if the user is unaware of the presence of the module, objects to the nature of the advertising materials displayed, or finds the manner of the advertising display intrusive. The module may also silently leak or harvest sensitive details from the device, such as its International Mobile Equipment Identity (IMEI) number, location, contacts, etc."""



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

