"""
Zemberek: Word Analysis Example
Documentation: https://bit.ly/2MTmfr1
Java Code Example: https://bit.ly/2MV2Hmj
"""
from typing import List

from jpype import JClass, JString

__all__: List[str] = ['run']

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
AnalysisFormatters: JClass = JClass(
    'zemberek.morphology.analysis.AnalysisFormatters'
)
WordAnalysis: JClass = JClass('zemberek.morphology.analysis.WordAnalysis')


def run(word: str) -> None:
    """
    Word analysis example.

    Args:
        word (str):
    """

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    results: WordAnalysis = morphology.analyze(JString(word))

    for result in results:
        print(
            f'\nLexical and Surface: {str(result.formatLong())}'
            f'\nOnly Lexical: {str(result.formatLexical())}'
            '\nOflazer Style:'
            f'{str(AnalysisFormatters.OFLAZER_STYLE.format(result))}'
        )
