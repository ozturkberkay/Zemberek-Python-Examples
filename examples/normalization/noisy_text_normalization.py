# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Noisy Text Normalization Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/normalization#noisy-text-normalization
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/normalization/NormalizeNoisyText.java

# Method:
    # From clean and noisy corpora, vocabularies are created using morphological analysis.
    # With some heuristics and language models, words that should be split to two are found.
    # From corpora, correct, incorrect and possibly-incorrect sets are created.
    # For pre-processing, deasciifier, split and combine heuristics are applied.
    # Using those sets and large corpora, a noisy to clean word lookup is generated using a modified version of Hassan and Menezes 2013 work [1].
    # For a sentence, for every noisy word, candidates are collected from lookup tables, informal and ascii-matching morphological analysis and spell checker.
    # Most likely correct sequence is found running Viterbi algorithm on candidate words with language model scoring.

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import the required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
TurkishSentenceNormalizer = jp.JClass('zemberek.normalization.TurkishSentenceNormalizer')
Paths = jp.JClass('java.nio.file.Paths')

# List of dummy sentences to work on
examples = [
	'Yrn okua gidicem',
	'Tmm, yarin havuza giricem ve aksama kadar yaticam :)',
	'ah aynen ya annemde fark ettı siz evinizden cıkmayın diyo',
	'gercek mı bu? Yuh! Artık unutulması bile beklenmiyo',
	'Hayır hayat telaşm olmasa alacam buraları gökdelen dikicem.',
	'yok hocam kesınlıkle oyle birşey yok',
	'herseyi soyle hayatında olmaması gerek bence boyle ınsanların falan baskı yapıyosa'
]

# Get the path to the (baseline) lookup files
lookupRoot = Paths.get('../../data/normalization')

# Get the path to the compressed bi-gram language model
lmPath = Paths.get('../../data/lm/lm.2gram.slm')

# Instantiate the morphology class with the default RootLexicon
morphology = TurkishMorphology.createWithDefaults()

# Initialize the TurkishSentenceNormalizer class
normalizer = TurkishSentenceNormalizer(morphology, lookupRoot, lmPath)

# Normalize the sentences and print the results
for i, example in enumerate(examples):
	print('Noisy Sentence %d: %s\nNormalized Sentence %d: %s\n' 
	% (i, example, i, normalizer.normalize(example)))

# Shut down the JVM
jp.shutdownJVM()