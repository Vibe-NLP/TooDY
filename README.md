# TooDY
The folder contains the TooDY code (lexical and syntactic analysers), the dictionaries, and requirement documents to experiment with it


Before performing any analysis we apply the trained pipeline
First we load it: 
nlp = spacy.load('en\_core\_web\_sm')
This will assign to nlp an object of type Language containing all the components and data needed to process the text string, usually called "text". 
Then, we call the nlp object on a text, this will return an oject, usually called doc, that contains all the generated information 
doc = nlp('text to be processed')


The lexical analyser consists of the following steps: 
-Importing the necessary packages.
-Loading the trained pipeline and applying it to the text.
-Pattern creation from a dictionary: The dictionary to be used is loaded, then converted into a doc object using 'nlp.makedoc' to create the lexical pattern. 
-Matcher creation: The matcher object is instantiated; the pattern is added. 
-Application: The matcher object is called with the doc object as argument.
-Printing the results: The number of matches found is printed and then, for each match found, the word identified by the matcher within the text via the pattern, and the requirement containing the identified word.



The spaCy methods that will be used during Syntactic Analysis are:
-doc.sents: identifies individual phrases within a text to which the language model has been applied.
-token.pos: returns the POS tag of the token
-token.morph: shows the morphology of the token, i.e. the meaning that can be attributed to a word depending on where it is placed within the discourse. For example in "I eat an apple" the application of token.morph to the first  token returns:  Case=Nom|Number=Sing|Person=1|PronType=Prs
-token.dep\_: shows the dependency label assigned to the token.
-token.lemma\_: shows the token's lemma.
-token.children: identifies the link between a parent  and a child token.
-token.head: returns the father of the token.
