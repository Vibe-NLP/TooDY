from numpy import string_
import spacy
from spacy import displacy
from spacy.symbols import  VERB, agent,auxpass
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
verbs = []
sentences=[]
conjunction=[]
# optional, uncomment to display the syntactic relations, rendering on the browser: http://localhost:5000/
#displacy.serve(doc, style='dep')

for sent in doc.sents:
    for token in sent:
        if token.text.lower() in ("provide","modified","available","supplied","availability"):
            if token.head.pos_ in ("VERB"):
                for possible_advmod1 in token.head.children:
                    if possible_advmod1.text.lower() in ("when","where","if") and possible_advmod1.dep_ in ("advmod","mark"):
                        conjunction.append(possible_advmod1.text)
                        sentences.append(sent.text)
                        verbs.append(token.text)
            else:
                for possible_advmod in token.children:
                    if possible_advmod.text.lower() in ("when","where","if") and possible_advmod.dep_ in ("advmod","mark"):
                            conjunction.append(possible_advmod.text)
                            sentences.append(sent.text)
                            verbs.append(token.text)

print("Total matches found:", len(conjunction))#len(verbs)

for match_verbs,match_conjunction, match_sentences  in zip(verbs,conjunction,sentences,):
    print("Match found:",match_conjunction,match_verbs,".","Requirement:", match_sentences)
