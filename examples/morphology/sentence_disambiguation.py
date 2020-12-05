"""
Zemberek: Disambiguating Sentences Example
Documentation: https://bit.ly/36mO5Uu
Java Code Example: https://bit.ly/31UfDwI
"""
from typing import List

from jpype import JClass, java

__all__: List[str] = ['run']

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')


def run(sentence: str) -> None:
    """
    Sentence disambiguation example.

    Args:
        sentence (str): Sentence to disambiguate.
    """

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    analysis: java.util.ArrayList = morphology.analyzeSentence(sentence)

    results: java.util.ArrayList = morphology.disambiguate(
        sentence, analysis
    ).bestAnalysis()

    for i, result in enumerate(results, 1):
        print(
            f'\nAnalysis {i}: {str(result.formatLong())}'
            f'\nStems {i}:'
            f'{", ".join([str(stem) for stem in result.getStems()])}'
            f'\nLemmas {i}:'
            f'{", ".join([str(stem) for stem in result.getLemmas()])}'
        )
