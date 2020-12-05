"""
Zemberek: Finding POS Tag Example
Documentation: https://bit.ly/32WCfyi
Java Code Example: https://bit.ly/2Nn7hse
"""
from typing import List

from jpype import JClass, java

__all__: List[str] = ['run']

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')


def run(sentence: str):
    """
    POS tag detection example.

    Args:
        sentence (str): Sentence to find POS tags on.
    """

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    analysis: java.util.ArrayList = morphology.analyzeAndDisambiguate(
        sentence
    ).bestAnalysis()

    pos: List[str] = []

    for i, analysis in enumerate(analysis, start=1):
        print(
            f'\nAnalysis {i}: {analysis}',
            f'\nPrimary POS {i}: {analysis.getPos()}'
            f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}',
        )
        pos.append(
            f'{str(analysis.getLemmas()[0])}-{analysis.getPos().shortForm}'
        )

    print(f'\nFull sentence with POS tags: {" ".join(pos)}')
