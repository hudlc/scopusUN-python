import bibtexparser
import requests


bibtex_str = requests.get('https://digitallibrary.un.org/search?ln=en&p=ipcc&f=&rm=&sf=&so=d&rg=200&c=Resource+Type&c=UN+Bodies&c=&of=btex&fti=0&fti=0')


library = bibtexparser.parse_string(bibtex_str.text) # or bibtexparser.parse_file("my_file.bib")

# print(f"Parsed {len(library.blocks)} blocks, including:"
#   f"\n\t{len(library.entries)} entries"
#     f"\n\t{len(library.comments)} comments"
#     f"\n\t{len(library.strings)} strings and"
#     f"\n\t{len(library.preambles)} preambles")





# numberOfEntrie = len(library.entries)

for entry in library.entries:
    if entry.fields[0].key == 'author':
        print (entry.fields[0].value)
    if entry.fields[1].key == 'author':
        print(entry.fields [1].value)
