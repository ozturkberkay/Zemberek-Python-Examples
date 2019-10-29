"""
## Zemberek: Noisy Text Normalization Example
# Documentation: https://bit.ly/2WkUVVF
# Java Code Example: https://bit.ly/31Qi9Ew
"""

from os.path import join

from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    TurkishSentenceNormalizer: JClass = JClass(
        'zemberek.normalization.TurkishSentenceNormalizer'
    )
    Paths: JClass = JClass('java.nio.file.Paths')

    normalizer = TurkishSentenceNormalizer(
        TurkishMorphology.createWithDefaults(),
        Paths.get(
            join('..', '..', 'data', 'normalization')
        ),
        Paths.get(
            join('..', '..', 'data', 'lm', 'lm.2gram.slm')
        )
    )

    for i, example in enumerate([
        'Yrn okua gidicem',
        'Tmm, yarin havuza giricem ve aksama kadar yaticam :)',
        'ah aynen ya annemde fark ettı siz evinizden cıkmayın diyo',
        'gercek mı bu? Yuh! Artık unutulması bile beklenmiyo',
        'Hayır hayat telaşm olmasa alacam buraları gökdelen dikicem.',
        'yok hocam kesınlıkle oyle birşey yok',
        'herseyi soyle hayatında olmaması gerek bence boyle ınsanların'
    ]):
        print((
            f'\nNoisy {i}: {example}'
            f'\nNormalized {i}: {normalizer.normalize(JString(example))}'
        ))

    shutdownJVM()
