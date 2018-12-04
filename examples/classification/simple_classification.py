# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Simple Classification Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/classification
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/classification/SimpleClassification.java
# fastText Documentation: https://fasttext.cc/docs/en/support.html

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Importing required Java classes
FastTextClassifier = jp.JClass('zemberek.classification.FastTextClassifier')
TurkishTokenizer = jp.JClass('zemberek.tokenization.TurkishTokenizer')
Paths = jp.JClass('java.nio.file.Paths')

# Using the text classifier with quantized model
# Make sure you generated a quantized model using:
# examples/classification/train_classifier.py
classifier = FastTextClassifier.load(Paths.get('../../data/classification/news-title-category-set.model.q'))

# The dummy data to work on
s = 'Beşiktaş berabere kaldı.'

# Processing the data before preediction
processed = ' '.join(TurkishTokenizer.DEFAULT.tokenizeToStrings(s)).lower()

# Predicting the 3 most likely labels
results = classifier.predict(processed, 3)

# Printing the results...
for i, result in enumerate(results):
    print('Item %d: %s' % (i+1, result.item))
    print('Score %d: %f\n' % (i+1, result.score))

# Shut down the JVM
jp.shutdownJVM()
