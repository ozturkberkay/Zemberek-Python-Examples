# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Ambiguity Resolution Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology#ambiguity-resolution
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/morphology/DisambiguateSentences.java

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
Paths = jp.JClass('java.nio.file.Paths')

# Instantiating the morphology class with the default RootLexicon
morphology = TurkishMorphology.createWithDefaults()

# Dummy sentence to work on
sentence = 'Yarın kar yağacak'

# Analyzing the dummy sentence. The returning WordAnalysis 
# object which can include zero or more SingleAnalysis objects
analysis = morphology.analyzeSentence(sentence)

# Resolving the ambiguity
results = morphology.disambiguate(sentence, analysis).bestAnalysis()

# Printing the results
for i, result in enumerate(results):
    print('Analysis %d: %s' % (i+1, result.formatLong()))
    print('Stems %d: %s' % (i+1, ' '.join(result.getStems())))
    print('Lemmas %d: %s\n' % (i+1, ' '.join(result.getLemmas())))

# Shutting down the JVM
jp.shutdownJVM()