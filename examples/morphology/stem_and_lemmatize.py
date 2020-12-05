"""
Zemberek: Stemming and Lemmatization Example
Documentation: https://bit.ly/2WvtQzv
Java Code Example: https://bit.ly/2Wm71hj
"""
from typing import List
from jpype import JClass, JString

__all__: List[str] = ['run']

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
WordAnalysis: JClass = JClass('zemberek.morphology.analysis.WordAnalysis')


def run(word: str) -> None:
    """
    Stemming and lemmatization example.

    Args:
        word (str): Word to apply stemming and lemmatization.
    """

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    print('\nResults:')

    results: WordAnalysis = morphology.analyze(JString(word))

    for result in results:
        print(
            f'{str(result.formatLong())}'
            f'\n\tStems ='
            f' {", ".join([str(result) for result in result.getStems()])}'
            f'\n\tLemmas ='
            f' {", ".join([str(result) for result in result.getLemmas()])}'
        )
