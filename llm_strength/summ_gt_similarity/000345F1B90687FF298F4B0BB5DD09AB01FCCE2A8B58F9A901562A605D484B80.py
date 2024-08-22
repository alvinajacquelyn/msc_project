import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "000345F1B90687FF298F4B0BB5DD09AB01FCCE2A8B58F9A901562A605D484B80"
summ = """
The provided text describes several classes and interfaces in Java, including:

* A class named "a" that extends the Android Application class and overrides the "onCreate" method to log a message.
* A custom class loader that extends the default class loader and overrides the `loadClass` method.
* A class called "u" in Java with several static fields and methods, including a native method "di" that takes a "Context" object and an "int" as arguments.
* A class "a" has several static methods for handling events related to an Android activity, including "b" and "c", which are called when the activity is created or receives an intent, respectively.
* An interface named "af" with a single method "a" that takes a single argument of type "com.buyang.redc.b.a".
* A class named "ae" that extends `Handler` and has a final field named "a" of type `ad`. The `handleMessage` method extracts the `tag` and `string` values from the `Message` object's `data` field and calls the `notifyDataSetChanged` method on the `a` field if the `string` value is not null and the `context` object is not null or the `com.buyang.redc.i.d.a` method returns null or the `i` value is not -1.
* A custom view called "ag" that extends LinearLayout. It has several private fields and methods, as well as a constructor that initializes the view's layout and adds several child views. The view also has several static methods for accessing the child views.
* A Java class that listens for certain intents and performs actions based on the intent's action and data. The class is named "b" and has a private static field "mContext" that is set to the context of the class. The class also has a public static method "a" that takes a context and an intent as parameters and performs the necessary actions based on the intent's action and data.
* A class named "CPack" that provides a singleton instance of the class, which can be accessed through the "doGetIns" method. The class has a private constructor that takes a Context and two Strings as parameters, and it has a private field "i" that is an instance of the class "i". The class also has two methods: "exit" and "showC", which take different parameters and perform different actions.
* A class named "Crece" that extends "BroadcastReceiver" and implements "c" interface. It overrides the "onReceive" method to handle an "Intent" object.
* A class named "f" that implements "Runnable" interface. It has a constructor that takes a "d" object and an integer as parameters, and it has a "run()" method that performs a series of operations on the "d" object.
* A class named "g" that implements "b" interface from "com.buyang.redc.a" package. It has a final field named "a" of type "d", and a constructor that takes a single argument of type "d". The class also implements two methods from the interface "b": "a" and "a".
* A class named "h" that has four fields: "a" of type "int", "b" of type "com.buyang.redc.b.a[]", "f24c" of type "int", and "d" of type "d". The class has a constructor that takes four parameters: "dVar", "i", "aVarArr". The class also has two methods: "a" and "a".
* A class named "i" that contains various methods and fields for managing an application's context and performing various tasks.
* A class named "j" that extends the Android "CountDownTimer" class and has a constructor that takes a "k" object and two long values. The "onFinish" method is overridden to call the "a" method on the "k" object, and the "onTick" method is left empty.
* A class named "l" that extends the Android "CountDownTimer" class and has a constructor that takes a "k" object and two long values. The "onFinish" method is overridden to call the "a" method on the "k" object, and the "onTick" method is left empty.
* A class named "m" that extends the "Thread" class and has two instance variables: "a" and "b". The constructor takes two arguments: "k" and "Context", and the "run" method is overridden to create a new instance of the "n" class and schedule it to run every second using the "Timer" class. The code defines several classes, including `n`, `o`, `q`, and `r`. The `n` class is a subclass of `TimerTask` and has a constructor that takes a `k` object and a `Context` object as parameters. The `run()` method of the class creates a new `Handler` object and posts a new `o` object to it. The `o` class is a nested class within `n` and implements the `Runnable` interface. It has a constructor that takes a single argument of type `n` and assigns it to a field named `a`. The `a` method of the class performs some operations on the `h` class and the `WindowManager` class. The `run` method of the class calls the `a` method.

The `q` class is a subclass of `Runnable` and has a constructor that takes a `p` object as a parameter. It has a private method named `a` that returns a string. The `run` method of the class creates a new `com.buyang.redc.b.d` object and sets its `b` and `d` properties. It then calls the `a` method to get a string, and it uses the `post` method of the `Handler` object to post a new `r` object to the handler.

The `r` class is a subclass of `Runnable` and has two fields: `a` and `b`, which are both of type `com.buyang.redc.b.a[]`. The constructor takes two arguments: a `q` object and an array of `com.buyang.redc.b.a` objects. The `run()` method is defined, which performs the following actions:

1. If the `a` field is null, it sets the `i` field to the `a.b` field and checks if it is equal to 0. If it is, it calls the `c()` method on the `afVar3` object.
2. It sets the `afVar2` object to the `afVar3` object.
3. It calls the `b()` method on the `afVar2` object.
4. It returns.
5. If the `a` field is not null, it calls the `a()` method on the `afVar` object, passing in the `a` field.
6. It calls the `a()` method on the `p` object, passing in the `a` field and the length of the `a` field.
7. It loops through the `a` field and adds each element to the `list` field of the `b` field. It also sets the `y` field of each element to 1.
8. It calls the `b()` method on the `activity` field, passing in each element of the `a` field.

The code also defines three classes: `x`, `y`, and `z`. `x` is a class that implements the `Runnable` interface and has two fields: `a` of type `String` and `b` of type `w`. The constructor takes two arguments: `wVar` of type `w` and `str` of type `String`. The `run()` method overrides the `run()` method of the `Runnable` interface and calls the `a()` method of the `b` field with the value of the `a` field as an argument. `y` is a class that extends `Handler` and has a final field named `a` of type `w`, and a constructor that takes a `w` object as an argument. The `handleMessage` method is overridden to handle messages of type `Message`. The method extracts data from the message's `Bundle` and checks if the data matches certain conditions. If the data matches, it calls a method on the `a` field to perform some action based on the data. `z` is a class that extends `Handler` and has a field named `a` of type `w`, and a constructor that takes a `w` object as a parameter. The `handleMessage` method is overridden to handle messages of type `Message`. The method extracts the data from the message's `Bundle` and checks if the data contains a string with a specific tag. If the tag is found, the method checks if the string is a valid URL. If it is, the method creates a new `l` object and calls its `a` method with the URL as a parameter. If the tag is not found, the method does nothing.

Overall, the code defines several classes that implement the `f` interface and provide a way to work with different types of data in a consistent and organized manner.</s>  The provided text describes a Java class that defines several custom classes and interfaces for Android development. The class extends the `TypeDeclaration` class from the `org.eclipse.jdt.core.dom` package and defines several custom views and interfaces, including `ag`, `ai`, `aj`, `ak`, `al`, `am`, `an`, `ao`, `ap`, and `aq`. These classes and interfaces are used to create custom views and interfaces for Android development, including a `GridView` class called `ag` that overrides the `onMeasure` method, a `Runnable` interface called `ai` that performs actions on a `ah` instance, and a `TimerTask` class called `aj` that posts a `Runnable` object to a `Handler` object. The code also defines several methods, including "a" and "b" in "f", and "onClick" in "aa". The class is used to manage notifications and their associated data, with methods for creating, updating, and deleting notifications
"""

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

