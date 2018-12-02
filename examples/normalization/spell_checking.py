# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Tokenization Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/normalization#turkish-spell-checker
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/normalization/BasicWordSpellingCheckAndSuggestion.java

# Turkish Spell Checker Limitations:
	# It only may correct for 1 insertion, 1 deletion, 1 substitution and 1 transposition errors.
	# It ranks the results with an internal unigram language model.
	# There is no deasciifier.
	# It does not correct numbers, dates and times.
	# There may be junk results.
	# For shorter words, there will be a lot of suggestions (sometimes >50 ).
	# Suggestion function is not so fast (Around 500-1000 words/second).

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
TurkishSpellChecker = jp.JClass('zemberek.normalization.TurkishSpellChecker')

# Instantiate the morphology class with the default RootLexicon
morph = TurkishMorphology.createWithDefaults()

# Instantiate the spell checker class using the morphology instance
spell = TurkishSpellChecker(morph)

# Dummy words to work on
words = ['Ankar\'aya', 'bugn', 'gidyorum']

# Do basic spell checking and print the results
print('\nSPELL CHECK:\n')
for word in words:
	print('%s -> Correct' % (word) if spell.check(word) else '%s -> Wrong' % (word))

# Suggest corrected words
print('\nWORD SUGGESTIONS:\n')
for word in words:

	# Print the suggestions if they exist
	if spell.suggestForWord(word):
		print('%s -> ' % (word) + ', '.join(spell.suggestForWord(word)))

	else:
		print('No suggestions found for the word -> %s' % (word))

# Create a new sentance using the suggested words
print('\nFIXED SENTENCE:\n')
for i, word in enumerate(words):

	# If the word is mispelled and there are suggestions, 
	# replace the word with the first suggestion
	if spell.suggestForWord(word):
		if not spell.check(word):
			words[i] = spell.suggestForWord(word)[0]

# Create and print the fixed sentence
print(' '.join(words))

# Shut down the JVM
jp.shutdownJVM()