"""
Zemberek: Finding POS Tag Example
Documentation: https://bit.ly/32WCfyi
Java Code Example: https://bit.ly/2Nn7hse
"""

from os.path import join
from typing import List

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

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    sentence: str = 'Keşke yarın hava güzel olsa'

    analysis: java.util.ArrayList = (
        morphology.analyzeAndDisambiguate(sentence).bestAnalysis()
    )

    pos: List[str] = []

    for i, analysis in enumerate(analysis, start=1):
        print(
            f'\nAnalysis {i}: {analysis}',
            f'\nPrimary POS {i}: {analysis.getPos()}'
            f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}'
        )
        pos.append(
            f'{str(analysis.getLemmas()[0])}'
            f'-{analysis.getPos().shortForm}'
        )

    print(f'\nFull sentence with POS tags: {" ".join(pos)}')

    shutdownJVM()
