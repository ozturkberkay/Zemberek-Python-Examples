"""
Zemberek: Stemming and Lemmatization Example
Documentation: https://bit.ly/2WvtQzv
Java Code Example: https://bit.ly/2Wm71hj
"""

from os.path import join

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
    WordAnalysis: JClass = JClass('zemberek.morphology.analysis.WordAnalysis')

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    word: str = 'kutucuğumuz'

    print(f'\nWord: {word}\n\nResults:')

    results: WordAnalysis = morphology.analyze(JString(word))

    for result in results:
        print(
            f'{str(result.formatLong())}'
            f'\n\tStems ='
            f' {", ".join([str(result) for result in result.getStems()])}'
            f'\n\tLemmas ='
            f' {", ".join([str(result) for result in result.getLemmas()])}'
        )

    shutdownJVM()
