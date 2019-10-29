"""
Zemberek: Change Stem Example
Documentation: https://bit.ly/2WmPDsW
Java Code Example: https://bit.ly/32W6tkH
"""

from os.path import join

from jpype import (JClass, JString, getDefaultJVMPath, java, shutdownJVM,
                   startJVM)

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    DictionaryItem: JClass = JClass(
        'zemberek.morphology.lexicon.DictionaryItem'
    )
    WordAnalysis: JClass = JClass('zemberek.morphology.analysis.WordAnalysis')

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    new_stem: DictionaryItem = (
        morphology.getLexicon().getMatchingItems('kalem').get(0)
    )

    word: str = 'simidime'

    print(f'\nWord: {word}')

    results: WordAnalysis = morphology.analyze(JString(word))

    for result in results:
        generated: java.util.ArrayList = (
            morphology.getWordGenerator().generate(
                new_stem, result.getMorphemes()
            )
        )
        for word in generated:
            print(
                f'\nInput Analysis: {str(result.formatLong())}'
                f'\nAfter Stem Change, Word: {str(word.surface)}'
                '\nAfter Stem Change, Analysis:'
                f'{str(word.analysis.formatLong())}'
            )

    shutdownJVM()
