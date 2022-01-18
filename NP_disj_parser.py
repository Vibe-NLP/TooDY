import spacy
from spacy.symbols import NOUN, cc
from spacy import displacy
from numpy import string_
#To apply the trained pipeline, we load it. 
#This will assign to nlp an object of type Language containing all the components and data 
#needed to process the text string. 
nlp = spacy.load("en_core_web_sm")
print ("Which file do you want to analyse?")
reqdoc = string_(input()) 
file_name = reqdoc
introduction_file_text = open(file_name).read()
#we call the nlp object on the text to be analysed, this will return an oject, 
#called doc, that contains all the generated information
doc = nlp(introduction_file_text)
#optional, uncomment to display the syntactic relations
#spacy.displacy.serve(doc, style='dep')

sentences=[]
conjunction=[]

for sent in doc.sents:
        for token in sent:
               if token.text.lower() in ("or","and/or","and\or") and token.dep_=="cc":
                       if token.head.pos_ in("NOUN","ADP"):
                        conjunction.append(token.text)
                        sentences.append(sent.text)
print("Total matches found:", len(conjunction))

for match_conjunction, match_sentences  in zip(conjunction,sentences):
    print("Match found:",match_conjunction,".","Requirement:", match_sentences)
