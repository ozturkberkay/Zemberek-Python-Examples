"""
Zemberek: Diacritic Analysis Example
Documentation: https://bit.ly/2PsyRHk
Java Code Example: https://bit.ly/2Jx7zfk
"""
from typing import List

from jpype import JClass

__all__: List[str] = ['run']

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
RootLexicon: JClass = JClass('zemberek.morphology.lexicon.RootLexicon')


def run(word: str) -> None:
    """
    Diacritic analysis example.

    Args:
        word (str): Word to apply diacritic analysis.
    """

    morphology: TurkishMorphology = (
        TurkishMorphology.builder()
        .ignoreDiacriticsInAnalysis()
        .setLexicon(RootLexicon.getDefault())
        .build()
    )

    print('\nAnalysis:')

    for analysis in morphology.analyze(word):
        print(analysis)
