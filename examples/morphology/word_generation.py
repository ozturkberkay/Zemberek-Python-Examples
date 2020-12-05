"""
Zemberek: Word Generation Example
Documentation: https://bit.ly/2otE6LW
Java Code Example: https://bit.ly/32TWKvb
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


def _generate_nouns(root_word: str) -> None:
    """
    Generates inflections of the given root word using possessive and case
    suffix combinations.

    Args:
        root_word (str): Root word to generate inflections from.
    """

    print('\nGenerating nouns.\n')

    number: List[JString] = [JString('A3sg'), JString('A3pl')]
    possessives: List[JString] = [
        JString('P1sg'),
        JString('P2sg'),
        JString('P3sg'),
    ]
    cases: List[JString] = [JString('Dat'), JString('Loc'), JString('Abl')]

    morphology: TurkishMorphology = (
        TurkishMorphology.builder()
        .setLexicon(root_word)
        .disableCache()
        .build()
    )

    item: DictionaryItem = (
        morphology.getLexicon().getMatchingItems(root_word).get(0)
    )

    for number_m in number:
        for possessive_m in possessives:
            for case_m in cases:
                for result in morphology.getWordGenerator().generate(
                    item, number_m, possessive_m, case_m
                ):
                    print(str(result.surface))


def _generate_verbs(infinitive: str, stem: str) -> None:
    """
    Generates words from a given stem.

    Args:
        infinitive (str): Infinitive form of the verb to create the lexicon.
        stem (str): Stem to generate words for.
    """

    print('\nGenerating verbs.\n')

    positive_negatives: List[JString] = [JString(''), JString('Neg')]
    times: List[JString] = [
        'Imp',
        'Aor',
        'Past',
        'Prog1',
        'Prog2',
        'Narr',
        'Fut',
    ]
    people: List[JString] = ['A1sg', 'A2sg', 'A3sg', 'A1pl', 'A2pl', 'A3pl']

    morphology = (
        TurkishMorphology.builder()
        .setLexicon(infinitive)
        .disableCache()
        .build()
    )

    for pos_neg in positive_negatives:
        for time in times:
            for person in people:
                seq: java.util.ArrayList = java.util.ArrayList()
                if pos_neg:
                    seq.add(JString(pos_neg))
                if time:
                    seq.add(JString(time))
                if person:
                    seq.add(JString(person))
                results = list(
                    morphology.getWordGenerator().generate(JString(stem), seq)
                )
                if not results:
                    print(
                        f'Cannot generate Stem = ["{stem}"]'
                        f'\n | Morphemes = {[str(morph) for morph in seq]}'
                    )
                    continue
                print(' '.join(str(result.surface) for result in results))


def run(noun_root_word: str, verb_infinitive: str, verb_stem: str) -> None:
    """
    Generate nouns and verbs.

    Args:
        noun_root_word (str): Root word to generate inflections from.
        verb_infinitive (str): Infinitive form of the verb to create the
            lexicon for verb generation.
        verb_stem (str): Stem to generate verbs for.
    """
    _generate_nouns(noun_root_word)
    _generate_verbs(verb_infinitive, verb_stem)
