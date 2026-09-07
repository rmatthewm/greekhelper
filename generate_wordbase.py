# generate_wordbase.py -- Raul Matthew Mosley 2026
#
# Loads the words and definitions from the pdf and converts them to a csv.

import re
from pypdf import PdfReader

# Regular Expressions for the types of lines we care about
category_re = re.compile(r'\[.+\]\s+\([0-9]+.+\)')
definition_re = re.compile(r'.+\s=\s[0-9]+')

def parse_pdf():
    reader = PdfReader('greek_words_lester.pdf')
    n_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    text_lines = text.split('\n')
    for line in text_lines:
        # If this line is a grammatical category heading
        if category_re.fullmatch(line):
            # Get the category name
            opening = line.index('[') + 1
            closing = line.index(']')
            category = line[opening:closing]
            print('category: ', category)

        # If this line is a word definition
        elif definition_re.fullmatch(line):
            print('definition: ', line)
    


def main():
    parse_pdf()

if __name__ == '__main__':
    main()