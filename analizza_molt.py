import spacy
from spacy.symbols import NOUN, cc
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
file_name = 'C:/Users/Laura/Documents/Articoli/2021spaCy/smartHouse.txt'
introduction_file_text = open(file_name).read()
doc = nlp(introduction_file_text)
#spacy.displacy.serve(doc, style='dep')

sentences=[]
conjunction=[]
count=0

for sent in doc.sents:
        count+=1
        for token in sent:
               # if token.text.lower() in ("or","and/or","and\or","and") and token.dep_=="cc":
               if token.text.lower() in ("or") and token.dep_=="cc":
                       if token.head.pos_ in("NOUN","ADP"):
                        conjunction.append(token.text)
                        sentences.append(sent.text)
print(count)
print("Total matches found:", len(conjunction))

for match_conjunction, match_sentences  in zip(conjunction,sentences):
    print("Match found:",match_conjunction,".","Requirement:", match_sentences)
