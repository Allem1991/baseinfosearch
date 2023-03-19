import os
import re
from collections import defaultdict

import en_core_web_md


def read_index_file() -> dict:
    result = {}
    with open("index.txt") as f:
        for line in f:
            filename, link = line.split(" - ")
            result[filename] = link

    return link


nlp = en_core_web_md.load()

inverted_index = defaultdict(set)
for file in os.listdir('save_pages'):
    text = open("save_pages/" + file, encoding= 'utf-8').read()
    for word in re.findall("[A-Za-z]+", text):
        if len(word) > 5:
            doc = nlp(word)
            lemma = doc[0].lemma_
            inverted_index[lemma].add(file.split(".")[0])

with open("inverted_index.txt", "w") as w:
    for lemma in inverted_index.keys():
        w.write(lemma + f" {' '.join(inverted_index[lemma])}\n")
