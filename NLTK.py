import nltk

lines = 'Crashed into trees while attempting to land after being shot down by British and French aircraft.'
#lines = 'Caught fire in midair. The pilot leaped from the plane to his death as the plane began to go into a dive.' #'lines is some string of words'
# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
is_verb = lambda pos: pos[:2] == 'VB'
# do the nlp stuff
tokenized = nltk.word_tokenize(lines)
print(nltk.pos_tag(tokenized))

nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)]

print(nouns)
#>>> ['lines', 'string', 'words']
print(verbs)