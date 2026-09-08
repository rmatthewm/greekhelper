# generate_wordbase.py -- Raul Matthew Mosley 2026
#
# Loads the words and definitions from a txt and converts them to a csv.

import re
from pypdf import PdfReader
from word_entry import WordEntry

# Regular Expressions for the types of lines we care about
category_re = re.compile(r'\[.+\]\s+\([0-9]+.+\)')
definition_re = re.compile(r'.+\s=\s[0-9]+')

def parse_pdf():
    # reader = PdfReader('greek_words_lester.pdf')
    # n_pages = len(reader.pages)
    # page = reader.pages[0]
    # text = page.extract_text()
    with open('greek_words.txt', 'r') as f:
        text = f.read()

    word_entries = []
    pos = None

    text_lines = text.split('\n')
    for line in text_lines[:40]:
        # If this line is a grammatical category heading
        if category_re.fullmatch(line):
            # Get the part of speech category name
            pos = re.search(r'\[([A-Z]+)\s*.*\]', line).group(1)
            print('category: ', pos)

        # If this line is a word definition
        elif definition_re.fullmatch(line):
            if pos is None:
                raise RuntimeError('Found word definition before part of speech category was given.')

            match = re.search(r'\s*([^a-zA-Z()\s]+(?:\s+\(*[^a-z()A-Z\s]+\)*)*)\s*[a-zA-Z()\s,;.]', line)
            word = match.group(1)

            match = re.search(r'[^a-zA-Z]+[^a-zA-Z()]([a-zA-Z();,.]+(?:\s*[a-zA-Z();,.]+)*)', line)
            definition = match.group(1)

            match = re.search(r'[^0-9]+([0-9]+)', line)
            occurs = int(match.group(1))

            entry = WordEntry(word, definition.split('; '), pos, occurs)
            word_entries.append(entry)
            print(entry)



def main():
    parse_pdf()

if __name__ == '__main__':
    main()