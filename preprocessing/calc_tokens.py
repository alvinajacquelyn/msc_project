# import os

# output_dir = 'path/to/decompiled/output'  # Update with your actual path

# # Collect all .java files from the decompiled output
# java_files = []
# for root, dirs, files in os.walk(output_dir):
#     for file in files:
#         if file.endswith(".java"):
#             java_files.append(os.path.join(root, file))

# # Read all Java files and concatenate their contents
# all_java_content = ""
# for java_file in java_files:
#     with open(java_file, 'r') as file:
#         all_java_content += file.read()

# # Calculate the number of tokens
# num_tokens_decompiled = len(all_java_content) / 4  # Rough estimate

# print(f"Estimated number of tokens: {num_tokens_decompiled}")

#---------------------------------------

import os
import statistics

def get_file_sizes(folder_path):
    """Returns a list of file sizes in the given folder."""
    file_sizes = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):  # Ensure it's a file, not a directory
            file_sizes.append(os.path.getsize(file_path))
    print((file_sizes))
    print(len(file_sizes))
    return file_sizes

def calculate_standard_deviation(folder_path):
    """Calculates and returns the standard deviation of file sizes in the given folder."""
    file_sizes = get_file_sizes(folder_path)
    if len(file_sizes) < 2:
        return "Not enough files to calculate standard deviation"
    return int(statistics.stdev(file_sizes)* 0.000001 ), int(statistics.mean(file_sizes) * 0.000001 )

# Example usage
folder_path = "apkk"
std_dev = calculate_standard_deviation(folder_path)
print(f"The standard deviation of file sizes in the folder is: {std_dev}")
#------------------------

# # importing module
# from pandas import *

# # reading CSV file
# data = read_csv("app_msc.csv",  encoding='utf-8-sig')

# # converting column data to list
# apk = data['sha256'].tolist()

# listofurl = []
# for string in apk:
#     temp = "https://androzoo.uni.lu/api/download?apikey=1ef38937bf841c4a90b49d0e756bd4980b56886822cd8f20d6cf18cd449d68c9&sha256="
#     temp+= string
#     listofurl.append(temp)

# print(listofurl)


# # import csv
 

# # importing pandas as pd
# import pandas as pd

	
	

# # dictionary of lists
# dict = {'url': listofurl}
	
# df = pd.DataFrame(dict)
	
# # saving the dataframe
# df.to_csv('app_msc_url.csv')
