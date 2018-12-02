# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Change Stem Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology
# Java Code Example: https://github.com/ozturkberkay/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/morphology/ChangeStem.java

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')

# Instantiating the morphology class with the default RootLexicon
morphology = TurkishMorphology.createWithDefaults()

newStem = morphology.getLexicon().getMatchingItems('kalem').get(0)

# A dummy word to work on
word = 'kağıdıma'

# Analyze the word
results = morphology.analyze(word)

# Printing the results of the generated word...
for result in results.analysisResults:
    generated = morphology.getWordGenerator().generate(newStem, result.getMorphemes())
    for word in generated:
        print('Input Analysis: %s' % result.formatLong())
        print('After Stem Change, Word: %s' % word.surface)
        print('After Stem Change, Analysis: %s' % word.analysis.formatLong())

# Shutting down the JVM
jp.shutdownJVM()