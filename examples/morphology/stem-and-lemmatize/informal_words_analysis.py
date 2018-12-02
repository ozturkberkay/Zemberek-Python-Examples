# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Informal Turkish Words Analysis
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology#informal-turkish-words-analysis
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/morphology/AnalyzeAndConvertInformalWords.java

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

# Import required Java classes
TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
RootLexicon = jp.JClass('zemberek.morphology.lexicon.RootLexicon')
InformalAnalysisConverter = jp.JClass('zemberek.morphology.analysis.InformalAnalysisConverter')

# Instantiating the morphology class with the default RootLexicon
# Using the informal analysis and ignoring diacritics
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology#diacritics-ignored-analysis
morphology = TurkishMorphology.builder().setLexicon(RootLexicon.DEFAULT).ignoreDiacriticsInAnalysis().useInformalAnalysis().build()

# InformalAnalysisConverter generates formal surface form of an informal word analysis
converter = InformalAnalysisConverter(morphology.getWordGenerator())

# Dummy words to work on
tests = morphology.analyzeAndDisambiguate('ekmege yag surdum').bestAnalysis()

# Printing the analysis results:

print('\nROOT:')
for test in tests:
    print(test.getLemmas()[0])

print('\nROOT + INFINITIVE:')
for test in tests:
    print(test.item.lemma)

print('\nFORMAL SURFACE:')
for test in tests:
    print(converter.convert(test.surfaceForm(), test).surface)

# Shutting down the JVM
jp.shutdownJVM()