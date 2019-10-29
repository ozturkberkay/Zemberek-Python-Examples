"""
Zemberek: Word Generation Example
Documentation: https://bit.ly/2otE6LW
Java Code Example: https://bit.ly/32TWKvb
"""

from os.path import join
from typing import List

from jpype import (JClass, JString, getDefaultJVMPath, java, shutdownJVM,
                   startJVM)

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    print('\nGenerating nouns.\n')

    number: List[JString] = [JString('A3sg'), JString('A3pl')]
    possessives: List[JString] = [
        JString('P1sg'), JString('P2sg'), JString('P3sg')
    ]
    cases: List[JString] = [JString('Dat'), JString('Loc'), JString('Abl')]

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')

    morphology: TurkishMorphology = (
        TurkishMorphology.builder().setLexicon('armut').disableCache().build()
    )

    item = morphology.getLexicon().getMatchingItems('armut').get(0)

    for number_m in number:
        for possessive_m in possessives:
            for case_m in cases:
                for result in morphology.getWordGenerator().generate(
                    item, number_m, possessive_m, case_m
                ):
                    print(str(result.surface))

    print('\nGenerating verbs.\n')

    positive_negatives: List[JString] = [JString(''), JString('Neg')]
    times: List[JString] = [
        'Imp', 'Aor', 'Past', 'Prog1', 'Prog2', 'Narr', 'Fut'
    ]
    people: List[JString] = [
        'A1sg', 'A2sg', 'A3sg', 'A1pl', 'A2pl', 'A3pl'
    ]

    morphology: TurkishMorphology = (
        TurkishMorphology.builder().setLexicon('okumak').disableCache().build()
    )

    stem: str = 'oku'

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
                results = list(morphology.getWordGenerator().generate(
                    JString(stem),
                    seq
                ))
                if not results:
                    print((
                        f'Cannot generate Stem = ["{stem}"]'
                        f'\n | Morphemes = {[str(morph) for morph in seq]}'
                    ))
                    continue
                print(' '.join(str(result.surface) for result in results))

    shutdownJVM()
