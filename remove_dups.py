def remove_duplicates(filename):
    unique_lines = set() 
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            unique_lines.add(line.strip())

    with open(filename, 'w', encoding='utf-8') as file:
        for line in unique_lines:
            file.write(line + '\n') 

file_name = 'filtered_a_tags.txt'

remove_duplicates(file_name)
print("Duplicates have been removed from the file.")
