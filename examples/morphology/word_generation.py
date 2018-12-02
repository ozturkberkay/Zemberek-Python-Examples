# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Word Generation Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology#word-generation
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/morphology/GenerateWords.java

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import the required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')

# Root form of the word
word = 'armut'

# Possessive and case suffix combinations will 
# be used for generating inflections of the word
number = ['A3sg', 'A3pl']
possessives = ['P1sg', 'P2sg', 'P3sg']
cases = ['Dat', 'Loc', 'Abl']

# Disabling the cache and building using the word as the lexicon itself
morphology = TurkishMorphology.builder().setLexicon(word).disableCache().build()

# Getting the dictionary item
dictionary_item = morphology.getLexicon().getMatchingItems(word).get(0)

# Iterating the Result class instance to to access
# the generated word and the analysis
for numberM in number:
    for possessiveM in possessives:
        for caseM in cases:
            results = morphology.getWordGenerator().generate(dictionary_item, numberM, possessiveM, caseM)
            for result in results:
                print('Surface Form: %s' % result.surface)
                print('Analysis: %s\n' % result.analysis)

# Shutting down the JVM
jp.shutdownJVM()