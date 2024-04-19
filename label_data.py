import openai
import csv
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_type = "openai"



template = """"
                You are an efficient data labeler for machine learning systems, 
                You will be provided with the text that is associated with an <a> tag.
                Your task is to determine whether or not the text associated is non-descriptive for accessibility purposes.
                If the text is non-descriptive, you should only return "1" otherwise return "0".
            """

def process_and_write_tags(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        csvfile.seek(0, 2)
        if csvfile.tell() == 0:
            writer.writerow(['Text', 'Label'])
        
        for line in lines:
            line = line.strip()
            if line:
                response = openai.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": template},
                        {"role": "user", "content": line}
                    ]
                )
                label = response.choices[0].message.content.strip()
                if label == "1":
                    var = input(f"Line: {line} | Label: {label} | Press 'y' to confirm: ")
                    if var == 'y':
                        writer.writerow([line, label])
                        print(f"Line: {line} | Label: {label}")
                    else:
                        continue

process_and_write_tags('filtered_a_tags.txt', 'results.csv')