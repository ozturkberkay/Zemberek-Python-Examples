"""
Zemberek: Tokenization Example
Documentation: https://bit.ly/2pYWVqC
Java Code Example: https://bit.ly/31Ux0xJ
"""
from typing import List

from jpype import JClass, JString, java

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
TurkishSpellChecker: JClass = JClass(
    'zemberek.normalization.TurkishSpellChecker'
)


def run(sentence: str) -> None:
    """
    Spell checking example.

    Args:
        sentence (str): Sentence to check for spelling errors.
    """

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    spell_checker: TurkishSpellChecker = TurkishSpellChecker(morphology)

    words: List[str] = sentence.split(' ')
    fixed_words: List[str] = []

    for word in words:
        if not spell_checker.check(JString(word)):
            print(f'Spelling error: {word}')
            suggestions: java.util.ArrayList = spell_checker.suggestForWord(
                JString(word)
            )
            if suggestions:
                print(f'\nSuggestions for "{word}":')
                for suggestion in suggestions:
                    print(f' | {suggestion}')
                fixed_words.append(str(suggestions[0]))
                continue
            else:
                print(f'No suggestions found for "{word}".')
        fixed_words.append(word)

    print('\nFixed sentence:', ' '.join(fixed_words))
