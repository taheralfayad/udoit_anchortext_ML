def clean_whitespace(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines if line.strip()]

    with open(output_file, 'w') as file:
        for line in cleaned_lines:
            file.write(line + '\n')

input_file = 'extracted_a_tags.txt' 
output_file = 'cleaned_a_tags.txt'
clean_whitespace(input_file, output_file)
