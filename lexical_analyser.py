from numpy import string_
import spacy
from spacy.matcher import PhraseMatcher
#To apply the trained pipeline, we load it. 
#This will assign to nlp an object of type Language containing all the components and data 
#needed to process the text string, usually called "text". 
nlp = spacy.load("en_core_web_sm")
print ("Which file do you want to analyse?")
reqdoc = string_(input()) 
file_name = reqdoc
introduction_file_text = open(file_name).read()
#we call the nlp object on the text to be analysed, this will return an oject, 
#called doc, that contains all the generated information
doc = nlp(introduction_file_text)



# Choice of the dictionary 
print ("Which dictionary do you want to use?")
dict = string_(input()) 
dictionary_name= dict
dictionary_file_text = open(dictionary_name)
with dictionary_file_text as file:
  lines = [i.strip() for i in file]
lexical_patterns = [nlp.make_doc(text) for text in lines]

# Add the pattern to the matcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
matcher.add("LEXICAL_PATTERNS",lexical_patterns)
matches = matcher(doc)

print("Total matches found:", len(matches))
# Iterate over the matches and print the span text
for match_id, start, end in matches:
    span = doc[start:end]
    print("Match found:",(span.text)+"." ,"Requirement:",(span.sent.text))
