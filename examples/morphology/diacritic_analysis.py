"""
Zemberek: Diacritic Analysis Example
Documentation: https://bit.ly/2PsyRHk
Java Code Example: https://bit.ly/2Jx7zfk
"""

from os.path import join

from jpype import JClass, getDefaultJVMPath, shutdownJVM, startJVM

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    RootLexicon: JClass = JClass('zemberek.morphology.lexicon.RootLexicon')

    morphology: TurkishMorphology = (
        TurkishMorphology.builder().ignoreDiacriticsInAnalysis().setLexicon(
            RootLexicon.getDefault()
        ).build()
    )

    word: str = 'kisi'

    print(f'\nWord: {word}\n\nAnalysis:')

    for analysis in morphology.analyze(word):
        print(analysis)

    shutdownJVM()
