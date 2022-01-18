from numpy import string_
import spacy
from spacy import displacy
from spacy.symbols import  VERB, agent,auxpass
nlp = spacy.load("en_core_web_sm")
print ("Which file do you want to analyse?")
reqdoc = string_(input()) 
file_name = reqdoc

introduction_file_text = open(file_name).read()
doc = nlp(introduction_file_text)
#optional, uncomment to display the syntactic relations, rendering on the browser: http://localhost:5000/
#spacy.displacy.serve(doc, style='dep')

verbs =[]
count=0
sentences=[]
for sent in doc.sents:
     for token in sent:
          if token.pos == VERB and token.morph.get("VerbForm") == ['Part']:
               for possible_auxpass in token.children:
                    if possible_auxpass.lemma_=="be" and possible_auxpass.dep_ == 'auxpass':
                         for possible_agent in token.children:
                              if   (possible_agent.text == 'by' and  possible_agent.dep_ == 'agent'):
                                   count=1
                         if(count!=1):
                              count=0
                              verbs.append(token)
                              sentences.append(sent)
                         else:
                              count=0

print("Total matches found:", len(verbs))
for match_verbs, match_sentences in zip(verbs, sentences):
    print("Match found:",match_verbs,"." ,"Requirement:", match_sentences)
