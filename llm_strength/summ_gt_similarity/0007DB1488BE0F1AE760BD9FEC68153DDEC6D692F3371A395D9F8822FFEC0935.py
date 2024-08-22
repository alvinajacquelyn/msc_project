import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "0007DB1488BE0F1AE760BD9FEC68153DDEC6D692F3371A395D9F8822FFEC0935"
summ = """
The provided text describes several Java classes related to fragment management and sharing content with other apps. The main classes are `NotificationCompatImplBase` and `NotificationCompatImplHoneycomb`, which provide basic and advanced implementations of the `getNotification` method for Android 3.0 (Honeycomb) and later versions. The `Op` class represents an operation to be performed on a fragment manager and has several fields, including `cmd`, `enterAnim`, `exitAnim`, `fragment`, `next`, `popEnterAnim`, `popExitAnim`, `prev`, and `removed`. The `SavedState` class implements the `Parcelable` interface and provides a way to store the state of an object in a `Bundle`. The `LoadTask` class extends the `ModernAsyncTask` class and implements the `Runnable` interface, and is used to load data asynchronously in an `AsyncTaskLoader`. The code also defines several classes and interfaces related to compatibility with different versions of Android. These classes and interfaces provide compatibility layers for different versions of the Android framework, allowing developers to write code that works across different versions of the framework. The main classes are "ItemInfo" and "KeyEventCompat", which provide compatibility layers for the "ICSViewCompatImpl" and "KeyEvent" classes, respectively. The "ItemInfo" class has several fields and a default constructor, while the "KeyEventCompat" class has several static methods for normalizing, filtering, and checking key events. The "KeyEventCompatHoneycomb" class provides compatibility methods for earlier versions of Android, while the "KeyEventVersionImpl" interface has methods for handling key events in a specific way, depending on the version of the Android operating system. The code also defines several classes and interfaces related to compatibility layers for the Android framework, including `LayoutParams`, `MenuCompat`, `MenuItemCompat`, and `MenuVersionImpl`. These classes and interfaces provide compatibility layers for different versions of the Android framework, allowing developers to write code that works across different versions of the framework. The `LayoutParams` class provides a compatibility layer for the `ViewPager` widget, while the `MenuCompat` and `MenuItemCompat` classes provide compatibility layers for the `Menu` and `MenuItem` classes, respectively. The `MenuVersionImpl` interface defines two methods, `setShowAsAction` and `setActionView`, which are implemented by different classes depending on the Android version. This Java class provides compatibility methods for working with MotionEvents in Android, with different implementations for pre-Eclair and Eclair versions of the API. The class provides methods for retrieving information about a MotionEvent, such as the pointer index, pointer ID, X coordinate, and Y coordinate. The class also defines an interface for retrieving information about a MotionEvent object. Additionally, the code defines a custom listener for a ViewPager, which is a widget that allows users to flip through pages of content. The listener is called when the user scrolls through the pages, and it updates the text displayed in the PagerTitleStrip widget. The listener also updates the text positions when the user selects a page. The code also defines a custom class loader that extends the default class loader in Java and overrides the loadClass method to first try to load the class using the super class loader, and if that fails, it tries to load the class using the parent class loader. If both attempts fail, it throws a ClassNotFoundException. Finally, the code defines a class named "a" that extends the Android Application class and overrides the "onCreate" method to log a message with the tag "this" and the integer value 0 using the "u.i" method.
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

