import os
from bs4 import BeautifulSoup

def extract_a_tags_text(directory_path, output_file):
    html_files = [f for f in os.listdir(directory_path) if f.endswith('.html')]
    
    iter = 0
    with open(output_file, 'w') as file:
        for html_file in html_files:
            if iter == 7000:
                break
            iter += 1
            file_path = os.path.join(directory_path, html_file)
            
            with open(file_path, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')
                
                a_tags = soup.find_all('a')
                for tag in a_tags:
                    file.write(tag.get_text() + '\n')

directory_path = './big_data/NotPhish/'
output_file = 'extracted_a_tags.txt'
extract_a_tags_text(directory_path, output_file)
