# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Finding POS Tag Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/morphology/FindPOS.java

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import the required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')

# Instantiating the morphology class with the default RootLexicon
morphology = TurkishMorphology.createWithDefaults()

# A dummy sentence to work on
sentence = 'Keşke yarın hava güzel olsa'

# Analyzing and disambiguating the sentence
analysis = morphology.analyzeAndDisambiguate(sentence).bestAnalysis()

# A list to store primary POS tags
pos = []

# Printing the results...
for i, a in enumerate(analysis):
    print('Analysis %d: %s' % (i+1, a))
    print('Primary POS %d: %s' % (i+1, a.getPos()))
    print('Primary POS (Short Form) %d: %s\n' % (i+1, a.getPos().shortForm))
    pos.append(a.getLemmas()[0] + '-' + a.getPos().shortForm)

# Printing each word with the corresponding primary POS tag...
print('Sentence: ' + ' '.join(pos))

# Shutting down the JVM
jp.shutdownJVM()