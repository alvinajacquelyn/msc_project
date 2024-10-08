import transformers
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import pandas as pd
# importing module
from pandas import *
import csv
# reading CSV file

x = "000FEED1F11E6C2BD606A1E0D1DFE7C110A98A275145FD5BBFE302C76078E826"
summ = """
The provided text describes several Java classes and interfaces related to Android development, including `FragmentManagerState`, `FragmentState`, `FragmentTag`, `FragmentTransaction`, `InboxStyle`, `InstantiationException`, `IntentBuilder`, `IntentReader`, `LoaderCallbacks`, `LoaderInfo`, `LoaderManager`, `LoaderManagerImpl`, `NavUtils`, `NavUtilsImpl`, `NotificationCompat`, `NotificationCompatImpl`, `OnBackStackChangedListener`, `Op`, `SavedState`, `ShareCompat`, `ShareCompatICS`, `ShareCompatImpl`, `ShareCompatImplBase`, `ShareCompatImplICS`, `ShareCompatImplJB`, `ShareCompatJB`, `Style`, `TabInfo`, `TaskStackBuilder`, `TaskStackBuilderHoneycomb`, `TaskStackBuilderImpl`, `TaskStackBuilderImplBase`, `TaskStackBuilderImplHoneycomb`, `TaskStackBuilderImplJellybean`, `TaskStackBuilderJellybean`, `AsyncTaskLoader`, `AsyncTaskResult`, `BroadcastRecord`, `ContextCompat`, `ContextCompatHoneycomb`, `ContextCompatJellybean`, `IntentCompat`, `IntentCompatHoneycomb`, `IntentCompatIcsMr1`, `IntentCompatImpl`, `LoadTask`, `Loader`, `OnLoadCompleteListener`, `ReceiverRecord`, `WorkerRunnable`, `BaseViewConfigurationVersionImpl`, `EclairMotionEventVersionImpl`, `FroyoViewConfigurationVersionImpl`, `GBViewCompatImpl`, `GestureDetectorCompatImpl`, `TypeDeclaration`. These classes and interfaces provide various functionality for Android development, such as logging, caching, and accessibility. The code defines several classes and interfaces related to Android development, including `buildShortClassTag`, `LogWriter`, `LongSparseArray`, `LruCache`, `SparseArrayCompat`, `TimeUtils`, `AccessibilityDelegateBridge`, `AccessibilityDelegateBridgeJellyBean`, and `AccessibilityDelegateCompat`. These classes and interfaces provide compatibility layers for various Android classes, including `ViewCompat`, `KeyEventCompat`, and `VelocityTrackerCompat`, and are designed to work on different versions of the Android platform, including Honeycomb, Jelly Bean, and Android 11. The code uses a strategy pattern to choose the appropriate implementation based on the platform version, and provides methods for normalizing, filtering, and checking the modifiers of key events, as well as methods for setting and getting the label for a view. Additionally, the code provides compatibility methods for the `VelocityTracker` class, which is used to track the movement of a pointer on the screen. This code provides compatibility layers for different Android versions, including key events, menu items, and motion events. It also defines an interface for retrieving information about a `MenuItem` and several classes and interfaces related to the Android ViewPager widget. The code provides methods and fields for customizing the appearance of the tabs and titles, as well as a custom transformation method for capitalizing the first letter of each word in the text. This code provides compatibility layers for various methods in the Android SDK, including the `PagerTitleStripImplIcs` class, the `PageTransformer` interface, the `SavedState` class, the `SimpleOnPageChangeListener` class, and the `VelocityTrackerCompat` class. These classes and interfaces are designed to work on different versions of Android, and they use the `Build.VERSION.SDK_INT` field to determine which implementation to use. The code also provides compatibility methods for various Android versions, including Honeycomb, Ice Cream Sandwich, Jelly Bean, and later, using classes such as `ViewCompatHC`, `ViewCompatICS`, `ViewCompatJB`, and `ViewCompatJellybeanMr1`. This code provides a compatibility layer for the AccessibilityManager API introduced in Android 4.0 (Ice Cream Sandwich) and later versions. It defines a class called AccessibilityManagerCompat that provides a way to access and manipulate the accessibility information of a node in the Android accessibility tree. The class has several static methods that wrap the corresponding methods in the AccessibilityManager API, but with a different signature that is more suitable for use in Android 3.0 (Honeycomb) and earlier versions. The class also defines an abstract class called AccessibilityStateChangeListenerCompat, which is used to wrap the AccessibilityStateChangeListener interface in the AccessibilityManager API. The class also defines several static variables and methods that are used to determine the version of the Android operating system that the device is running and to provide compatibility for the AccessibilityManager API. Overall, this code provides a convenient way to work with accessibility information in Android, and it can be used to improve the accessibility of your app on Android versions 4.0 and later.
"""

#feiwo
groundtruth = """Feiwo is an advertisement library that is bundled with certain Android applications. It is an aggressive adware for Android mobile devices, which posts to its servers the victim's phone number, IMEI and list of installed applications. This is a typically unwanted SDK and should generally be removed from devices. Additionally, the adware implements several techniques to complexify its analysis. It is a malicious adware for Android devices that sends the victim’s phone number, IMEI, and list of installed apps to its servers. This is a common unwanted SDK that should be removed from devices. Furthermore, the adware employs several techniques to complicate its analysis."""



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

