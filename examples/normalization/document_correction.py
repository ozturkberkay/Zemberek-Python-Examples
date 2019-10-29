"""
Zemberek: Document Correction Example
Documentation: https://bit.ly/31PThMZ
Java Code Example: https://bit.ly/2oohWKT
"""

from os.path import join
from typing import List

from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishSpellChecker: JClass = JClass(
        'zemberek.normalization.TurkishSpellChecker'
    )
    TurkishTokenizer: JClass = JClass('zemberek.tokenization.TurkishTokenizer')
    TurkishLexer: JClass = JClass('zemberek.tokenization.antlr.TurkishLexer')
    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    Token: JClass = JClass('zemberek.tokenization.Token')

    tokenizer: TurkishTokenizer = TurkishTokenizer.ALL
    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()
    spell_checker: TurkishSpellChecker = TurkishSpellChecker(morphology)

    with open(
        join('..', '..', 'data', 'normalization', 'document.txt'),
        'r',
        encoding='utf-8'
    ) as document_file:
        document = document_file.read()

    tokens = tokenizer.tokenize(JString(document))

    corrected_tokens: List[str] = []

    for token in tokens:
        text: JString = token.content
        if (
            token.type != Token.Type.NewLine
            and token.type != Token.Type.SpaceTab
            and token.type != Token.Type.Punctuation
            and token.type != Token.Type.RomanNumeral
            and token.type != Token.Type.UnknownWord
            and token.type != Token.Type.Unknown
            and not spell_checker.check(text)
        ):
            suggestions: List[JString] = list(
                spell_checker.suggestForWord(token.content)
            )
            if suggestions:
                suggestion: str = str(suggestions[0])
                print(f'Correction: {token.content} -> {suggestion}.')
                corrected_tokens.append(suggestion)
                continue
        corrected_tokens.append(str(token.content))

    print('\nCorrected Document:\n', ' '.join(corrected_tokens))

    shutdownJVM()
