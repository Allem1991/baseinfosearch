import os
import re
from collections import defaultdict
from pprint import pprint

import en_core_web_md
from copy import deepcopy

from Levenshtein import distance

if __name__ == '__main__':

    nlp = en_core_web_md.load()

    for i, file in enumerate(os.listdir('save_pages')):
        words = set()
        text = open('save_pages/' + file, encoding= 'utf-8').read()
        for word in re.findall("[A-Za-z]+", text):
            if len(word) > 5:
                words.add(word.lower())

        with open(f"terms/tokens_{i}.txt", "w") as f:
            for word in words:
                f.write(word.strip().lower() + "\n")

        lemmas = defaultdict(set)
        for word in words:
            doc = nlp(word)
            if doc[0].lemma_ != word:
                lemmas[doc[0].lemma_].add(word)

        with open(f"terms/lemmas_{i}.txt", "w") as f:
            for key in lemmas.keys():
                f.write(f"{key}: {' '.join(lemmas[key])}\n")
