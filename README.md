# TooDY
The TooDY code tool and requirement documents to experiment with it
To apply the trained pipeline, we load it: 

nlp = spacy.load('en\_core\_web\_sm')

This will assign to nlp an object of type Language containing all the components and data needed to process the text string, usually called "text". 
Then, we call the nlp object on a text, this will return an oject, usually called doc, that contains all the generated information 

doc = nlp('text to be processed')


The lexical analyser consists of the following steps: 
Importing the necessary packages.
Loading the trained pipeline and applying it to the text.
Pattern creation from a dictionary: The dictionary to be used is loaded, then converted into a doc object using 'nlp.makedoc' to create the lexical pattern. 
Matcher creation: The matcher object is instantiated; the pattern is added. 
Application: The matcher object is called with the doc object as argument.
Printing the results: The number of matches found is printed and then, for each match found, the word identified by the matcher within the text via the pattern, and the requirement containing the identified word.

The result will be the identification of all the requirements that contain the words in the dictionary. 


