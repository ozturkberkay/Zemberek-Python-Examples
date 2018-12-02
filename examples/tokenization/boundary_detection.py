# -*- coding: utf-8 -*-

## Zemberek: Sentence Boundary Detection Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/tokenization#sentence-boundary-detection
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/tokenization/SentenceBoundaryDetection.java

import jpype as jp

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), 'ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import required Java classes
TurkishSentenceExtractor = jp.JClass('zemberek.tokenization.TurkishSentenceExtractor')

# Singleton instance with the default behavior
extractor = TurkishSentenceExtractor.DEFAULT

# A dummy paragraph to work on.
paragraph = 'Prof. Dr. Veli Davul açıklama yaptı. Kimse %6.5\'lik enflasyon oranını beğenmemiş!'

# Extracting the sentences from the paragraph into a list
sentences = extractor.fromParagraph(paragraph)

# Looping through the sentences...
for i, word in enumerate(sentences):
    print('Sentence %d: %s' % (i+1, word))

# Shutting down the JVM
jp.shutdownJVM()