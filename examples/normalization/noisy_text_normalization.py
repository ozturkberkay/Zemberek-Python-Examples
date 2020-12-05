"""
## Zemberek: Noisy Text Normalization Example
# Documentation: https://bit.ly/2WkUVVF
# Java Code Example: https://bit.ly/31Qi9Ew
"""
from jpype import JClass, JString

from examples import DATA_PATH

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
TurkishSentenceNormalizer: JClass = JClass(
    'zemberek.normalization.TurkishSentenceNormalizer'
)
Paths: JClass = JClass('java.nio.file.Paths')


def run(text: str) -> None:
    """
    Noisy text normalization example.

    Args:
        text (str): Noisy text to normalize.
    """

    normalizer = TurkishSentenceNormalizer(
        TurkishMorphology.createWithDefaults(),
        Paths.get(str(DATA_PATH.joinpath('normalization'))),
        Paths.get(str(DATA_PATH.joinpath('lm', 'lm.2gram.slm'))),
    )

    print(f'\nNormalized: {normalizer.normalize(JString(text))}')
