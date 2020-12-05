"""
Zemberek: Change Stem Example
Documentation: https://bit.ly/2WmPDsW
Java Code Example: https://bit.ly/39Jnp49
"""
from typing import List

from jpype import (
    JClass,
    JString,
    java,
)

__all__: List[str] = ['run']

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
DictionaryItem: JClass = JClass('zemberek.morphology.lexicon.DictionaryItem')
WordAnalysis: JClass = JClass('zemberek.morphology.analysis.WordAnalysis')


def run(
    source_word: str,
    target_word: str,
) -> None:
    """
    Stem change example.

    Args:
        source_word (str): Word to get stem from.
        target_word (str): Word to apply stem change.
    """
    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    new_stem: DictionaryItem = (
        morphology.getLexicon().getMatchingItems(target_word).get(0)
    )

    results: WordAnalysis = morphology.analyze(JString(source_word))

    for result in results:
        generated: java.util.ArrayList = (
            morphology.getWordGenerator().generate(
                new_stem, result.getMorphemes()
            )
        )
        for gen_word in generated:
            print(
                f'\nInput Analysis: {str(result.formatLong())}'
                f'\nAfter Stem Change, Word: {str(gen_word.surface)}'
                '\nAfter Stem Change, Analysis:'
                f'{str(gen_word.analysis.formatLong())}'
            )
