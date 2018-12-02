# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Standard Morphology Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology#stemming-and-lemmatization-example
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/morphology/StemmingAndLemmatization.java
# Dictionary Wiki: https://github.com/ahmetaa/zemberek-nlp/wiki/Text-Dictionary-Rules

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
RootLexicon = jp.JClass('zemberek.morphology.lexicon.RootLexicon')
Paths = jp.JClass('java.nio.file.Paths')

# Instantiating the morphology class with the default RootLexicon
morphology = TurkishMorphology.createWithDefaults()

# OR, you can instantiate the morphology class using a different lexicon
# In the example below, we are starting with the default root lexicon and adding ours as an addition
# lexicon = RootLexicon.builder().setLexicon(RootLexicon.DEFAULT).addTextDictionaries(Paths.get('../../../data/dictionaries/lexicon.txt')).build()
# morphology = TurkishMorphology.create(lexicon)
# Please refer to the official Wiki to correctly create a custom dictionary!

# Dummy word to work on
word = 'kitabımızsa'

# Analyzing the word
results = morphology.analyze(word).analysisResults

# Printing the morphology analysis results
for i, result in enumerate(results):
    print('Analysis %d: %s' % (i+1, result.formatLong()))
    print('Stems %d: %s' % (i+1, ', '.join(result.getStems())))
    print('Lemmas %d: %s\n' % (i+1, ', '.join(result.getLemmas())))

# Printing the root of the word
root = results[0].getLemmas()[0] if results else None
print('Root: %s' %  root)

# Shutting down the JVM
jp.shutdownJVM()