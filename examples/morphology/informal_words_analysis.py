"""
Zemberek: Informal Turkish Words Analysis
Documentation: https://bit.ly/2WpvvXg
Java Code Example: https://bit.ly/2MUvOG9
"""
from typing import List

from jpype import JClass, java

__all__: List[str] = ['run']

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
RootLexicon: JClass = JClass('zemberek.morphology.lexicon.RootLexicon')
InformalAnalysisConverter: JClass = JClass(
    'zemberek.morphology.analysis.InformalAnalysisConverter'
)


def run(sentence: str) -> None:
    """
    Informal words analysis example.

    Args:
        sentence (str): Sentence to search for informal words.
    """

    morphology: TurkishMorphology = (
        TurkishMorphology.builder()
        .setLexicon(RootLexicon.getDefault())
        .ignoreDiacriticsInAnalysis()
        .useInformalAnalysis()
        .build()
    )

    analyses: java.util.ArrayList = morphology.analyzeAndDisambiguate(
        sentence
    ).bestAnalysis()

    print('\nAnalysis:\n')

    for analysis in analyses:
        print(f'{str(analysis.surfaceForm())}-{analysis}')

    print('\nConverting formal surface form:\n')

    converter: InformalAnalysisConverter = InformalAnalysisConverter(
        morphology.getWordGenerator()
    )

    for analysis in analyses:
        print(str(converter.convert(analysis.surfaceForm(), analysis)))
