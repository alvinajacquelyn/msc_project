import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "002CFAA669F20C72304E25AEAE220B28DD9AA9C7CFDB9205EF9156F03AC252D1"
summ = """
The provided text describes several classes and interfaces related to accessibility and cursor management in Android. These include `AccessibilityRecordCompat`, `AccessibilityRecordCompatIcs`, and `AccessibilityRecordIcsImpl`, which provide compatibility layers for accessing and manipulating accessibility records on different Android versions. The text also mentions `AccessibilityStateChangeListenerBridge` and `AccessibilityStateChangeListenerCompat`, which provide compatibility layers for accessing the accessibility state of the device. Additionally, the text describes custom classes and interfaces for working with cursors and edge effects, such as `CursorFilter`, `CursorFilterClient`, and `EdgeEffectCompat`. The text also mentions the `DataSetObserver` class, which is used to observe changes to a `CursorAdapter`'s data, and the `SimpleCursorAdapter` class, which extends the `ResourceCursorAdapter` class and adds the ability to bind data from a `Cursor` to a `View`. The text describes several Java classes and their functions, including:

* RatioDrawable: a custom drawable class used to adjust the size of an image in an ImageView based on the aspect ratio of the image.
* WebViewClient: a Java class that extends the `WebViewClient` class and provides a custom implementation for loading web pages in a `WebView`.
* Document: a Java class that represents an XML document using the DOM (Document Object Model) API.
* EfficientAdapter: a custom adapter class used to display a list of albums in an Android app.
* anim: a static final class with a series of static final fields that represent different animation styles.
* array: a static final class with two static final int variables that represent the gamepan_array and image_size.
* starBase: a Java class that extends the `starBase` class and implements the `OnSearchResult` interface.
* TypeDeclaration: a Java class that extends the `TypeDeclaration` class from the `org.eclipse.jdt.core.dom` package and is used to represent a type declaration in the Java programming language.
* AdlibManager: a Java class that extends the `FragmentActivity` class and is used to manage ads in an Android app.

The code defines several classes, including a "BoardList" class with several fields and a constructor, a "bool" class with three static final fields, a "BuildConfig" class with a static final boolean field, and a "ChartGroup" class that extends "AdlibActivity" and implements the "AbsListView.OnScrollListener" interface. The "ChartGroup" class has several instance variables and methods, including "onCreate", "makea", "setData2", and "getView". The code also uses the "AQuery" library to make HTTP requests and parse JSON data. Additionally, the code defines a "color" class with static final fields representing different colors, and a "dimen" class with public static final int variables representing various dimensions used in the app.
"""

#cauly
groundtruth = """Cauly is an advertisement library that is bundled with certain Android applications. Acts as an unwanted interruption to normal activities performed by the device"""


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

