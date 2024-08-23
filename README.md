# Are LLMs Able to Identify Malicious Code? 

This repository contains scripts for exploring the use of Large Language Models (LLMs) in malware analysis in my MSc thesis. The focus is on comparing different prompts, and evaluating the capabilities of LLMs in identifying and understanding malware.


## Folder Descriptions
- **preprocessing**: Tools for preparing and cleaning data for analysis.
    - **request_from_url.py**: download APK files from the Androzoo dataset.
    - **get_dex.py**: unzip APK files and extract the .dex files or any other specified file types.
    - 
-  **run_prompts**: This directory contains scripts that iterate over every class within a malware sample, running each prompt through CodeLLama for analysis. The prompts are organized into the following categories:
    - **standard**: Holds standard prompts.
    - **definition**: Contains prompts focused on defining malware objective.
    - **reasoning**: Includes prompts aimed at chain of thought reasoning.
    - **summarise**: Prompt to ask the LLM to summarise the class of code.
- **prompt_comparison**: This folder is organized to run the SummEval metrics (coherence, consistency, relevance, fluency) on the outputs generated after executing different prompts. The structure includes:
    - **standard**
    - **definition**
    - **reasoning**
- **adding_fcg**: This folder is designed for adding Function Call Graphs (FCG) with the corresponding prompts
    - **python_s0_fcg**: Python scripts to automate the process of adding FCGs to the S0 prompt.
    - **python_s1_fcg**:: Python scripts to automate the process of adding FCGs to the S1 prompt.
    - **python_d1_fcg**: Python scripts to automate the process of adding FCGs to the D1 prompt.
- **llm_strength**: This folder is dedicated to evaluating the capability of CodeLlama in summarizing code and detecting suspicious or malicious behavior. 
    - **summ_gt_similarity**: Python scripts that handle the comparison of final summary summaries against ground truth descriptions.
    - **summ_llmasjudge_coherence**: Python scripts to evaluate coherence score of the final summary.
    - **summ_llmasjudge_consistency**: Python scripts to assess consistency score of the final summary.
    - **summ_llmasjudge_fluency**: Python scripts for fluency score of the final summary.
    - **summ_llmasjudge_relevance**: Python scripts to evaluate the relevance score of the final summary.
    - **summ_llmasjudge_summarise**: Python script to recursively summarise individual summaries for each class into a single, final summary .
- **python_misc**:
