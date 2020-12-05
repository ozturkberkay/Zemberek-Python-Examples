"""
Zemberek: Document Correction Example
Documentation: https://bit.ly/31PThMZ
Java Code Example: https://bit.ly/2oohWKT
"""
from typing import List

from jpype import JClass, JString, java

from examples import DATA_PATH

TurkishSpellChecker: JClass = JClass(
    'zemberek.normalization.TurkishSpellChecker'
)
TurkishTokenizer: JClass = JClass('zemberek.tokenization.TurkishTokenizer')
TurkishLexer: JClass = JClass('zemberek.tokenization.antlr.TurkishLexer')
TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
Token: JClass = JClass('zemberek.tokenization.Token')


def run() -> None:
    """
    Document correction example.
    """

    tokenizer: TurkishTokenizer = TurkishTokenizer.ALL
    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()
    spell_checker: TurkishSpellChecker = TurkishSpellChecker(morphology)

    with open(
        DATA_PATH.joinpath('normalization', 'document.txt'),
        'r',
        encoding='utf-8',
    ) as document_file:
        document = document_file.read()

    tokens: java.util.ArrayList = tokenizer.tokenize(JString(document))

    corrected_tokens: List[str] = []

    for token in tokens:
        text: JString = token.content
        if token.type not in {
            Token.Type.NewLine,
            Token.Type.SpaceTab,
            Token.Type.Punctuation,
            Token.Type.RomanNumeral,
            Token.Type.UnknownWord,
            Token.Type.Unknown
        } and not spell_checker.check(text):
            suggestions: List[JString] = list(
                spell_checker.suggestForWord(token.content)
            )
            if suggestions:
                suggestion: str = str(suggestions[0])
                print(f'Correction: {token.content} -> {suggestion}.')
                corrected_tokens.append(suggestion)
                continue
        corrected_tokens.append(str(token.content))

    print('\nCorrected Document:\n', ''.join(corrected_tokens))
