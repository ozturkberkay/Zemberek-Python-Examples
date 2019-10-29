
"""
Zemberek: Disambiguating Sentences Example
Documentation: https://bit.ly/36mO5Uu
Java Code Example: https://bit.ly/31UfDwI
"""

from os.path import join

from jpype import JClass, getDefaultJVMPath, java, shutdownJVM, startJVM

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    Paths: JClass = JClass('java.nio.file.Paths')

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    sentence: str = 'Bol baharatlı bir yemek yaptıralım.'

    print(f'Sentence = {sentence}')

    analysis: java.util.ArrayList = morphology.analyzeSentence(sentence)

    results: java.util.ArrayList = (
        morphology.disambiguate(sentence, analysis).bestAnalysis()
    )

    for i, result in enumerate(results, start=1):
        print(
            f'\nAnalysis {i}: {str(result.formatLong())}'
            f'\nStems {i}:'
            f'{", ".join([str(stem) for stem in result.getStems()])}'
            f'\nLemmas {i}:'
            f'{", ".join([str(stem) for stem in result.getLemmas()])}'
        )

    shutdownJVM()
