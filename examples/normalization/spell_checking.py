"""
Zemberek: Tokenization Example
Documentation: https://bit.ly/2pYWVqC
Java Code Example: https://bit.ly/31Ux0xJ
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

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    TurkishSpellChecker: JClass = JClass(
        'zemberek.normalization.TurkishSpellChecker'
    )

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    spell_checker: TurkishSpellChecker = TurkishSpellChecker(morphology)

    words: List[str] = ['Ankar\'yya', 'bugn', 'gidyorum']

    for word in words:
        print(
            f'\n{word}:'
            f' {"Correct" if spell_checker.check(JString(word)) else "Wrong"}'
        )

    for word in words:
        suggestions = spell_checker.suggestForWord(JString(word))
        if suggestions:
            print(f'\nSuggestions for "{word}":')
            for suggestion in suggestions:
                print(f' | {suggestion}')
        else:
            print(f'No suggestions found for "{word}".')

    for i, word in enumerate(words):
        if spell_checker.suggestForWord(JString(word)):
            if not spell_checker.check(JString(word)):
                words[i] = str(spell_checker.suggestForWord(JString(word))[0])

    print('\nFixed sentence:', ' '.join(words))

    shutdownJVM()
