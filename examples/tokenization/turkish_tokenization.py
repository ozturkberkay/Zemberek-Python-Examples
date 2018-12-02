# -*- coding: utf-8 -*-

import jpype as jp

## Zemberek: Tokenization Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/tokenization
# Java Code Example: https://github.com/ahmetaa/zemberek-nlp/blob/master/examples/src/main/java/zemberek/examples/tokenization/TurkishTokenizationExample.java

# Relative path to Zemberek .jar
ZEMBEREK_PATH = '../../bin/zemberek-full.jar'

# Start the JVM
jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (ZEMBEREK_PATH))

# Import required Java classes
TurkishTokenizer = jp.JClass('zemberek.tokenization.TurkishTokenizer')
TurkishLexer = jp.JClass('zemberek.tokenization.antlr.TurkishLexer')

# There are static instances provided for common use:
    # DEFAULT tokenizer ignores most white spaces (space, tab, line feed and carriage return).
    # ALL tokenizer tokenizes everything.
tokenizer = TurkishTokenizer.DEFAULT

# A dummy data to work on
dummy = "Prof. Dr. Veli Davul açıklama yaptı. Kimse %6.5'lik enflasyon oranını beğenmemiş!"

# Creating the TokenIterator instance
tokenIterator = tokenizer.getTokenIterator(dummy)

print('\n####### Basic Tokenization Using The Token Iterator #######\n')

# Iterating through the tokens using the TokenIterator instance
while (tokenIterator.hasNext()):

    # Setting the current token
    token = tokenIterator.token
    
    # Printing the token information
    print('Token = ' + str(token.getText()) 
        + ' | Type (Raw) = ' + str(token.getType()) 
        + ' | Type (Lexer) = ' + TurkishLexer.VOCABULARY.getDisplayName(token.getType()) 
        + ' | Start Index = ' + str(token.getStartIndex()) 
        + ' | Ending Index = ' + str(token.getStopIndex())
    )

################################################################################

# Available token types:
    #    Abbreviation = 1; SpaceTab = 2; NewLine = 3; Time = 4; Date = 5; PercentNumeral = 6; Number = 7; URL = 8;
    #    Email = 9; HashTag = 10; Mention = 11; MetaTag = 12; Emoticon = 13; RomanNumeral = 14; AbbreviationWithDots = 15;
    #    Word = 16; WordAlphanumerical = 17; WordWithSymbol = 18; Punctuation = 19; UnknownWord = 20; Unknown = 21;

# Ignoring unwanted types
tokenizer = TurkishTokenizer.builder().ignoreTypes(TurkishLexer.Punctuation, TurkishLexer.NewLine, 
TurkishLexer.SpaceTab, TurkishLexer.Time, TurkishLexer.Date, TurkishLexer.URL, TurkishLexer.Mention, 
TurkishLexer.HashTag, TurkishLexer.Email, TurkishLexer.WordWithSymbol, TurkishLexer.Number, 
TurkishLexer.PercentNumeral, TurkishLexer.MetaTag, TurkishLexer.RomanNumeral, TurkishLexer.Unknown).build()

# A dummy data to work on
dummy = "Prof. Dr. #VeliDavul IV @Istanbul 12.01.2017 12:00 açıklama yaptı. Kimse %6.5'lik enflasyon oranını beğenmemiş! :) veli@davul.com !!??=^+(/(&"

# Tokenize the dummy data
tokens = tokenizer.tokenize(dummy)

print('\n####### Ignoring Unwanted Types #######\n')

# Iterating through the tokens
for token in tokens:

    # Printing the token information
    print('Token = ' + str(token.getText()) 
        + ' | Type (Raw) = ' + str(token.getType()) 
        + ' | Type (Name) = ' + TurkishLexer.VOCABULARY.getDisplayName(token.getType()) 
        + ' | Start Index = ' + str(token.getStartIndex()) 
        + ' | Ending Index = ' + str(token.getStopIndex())
    )

# Shutting down the JVM
jp.shutdownJVM()