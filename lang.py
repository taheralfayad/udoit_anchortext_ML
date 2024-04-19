from langdetect import detect, LangDetectException

def filter_lines_by_language(input_file, output_file):
    allowed_languages = ['en', 'es'] 

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    filtered_lines = []

    for line in lines:
        try:
            lang = detect(line)
            if lang in allowed_languages:
                filtered_lines.append(line)
        except LangDetectException:
            continue

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in filtered_lines:
            file.write(line)

input_file = 'cleaned_a_tags.txt'
output_file = 'filtered_a_tags.txt'
filter_lines_by_language(input_file, output_file)
