"""
Zemberek: Sentence Boundary Detection Example
Documentation: https://bit.ly/2JopMvt
Java Code Example: https://bit.ly/2PrG7Dw
"""

from os.path import join

from jpype import JClass, getDefaultJVMPath, shutdownJVM, startJVM

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishSentenceExtractor: JClass = JClass(
        'zemberek.tokenization.TurkishSentenceExtractor'
    )

    extractor: TurkishSentenceExtractor = TurkishSentenceExtractor.DEFAULT

    sentences = extractor.fromParagraph((
        'Prof. Dr. Veli Davul açıklama yaptı.'
        'Kimse %6.5 lik enflasyon oranını beğenmemiş!'
        'Oysa maçta ikinci olmuştuk... Değil mi?'
    ))

    for i, word in enumerate(sentences):
        print(f'Sentence {i+1}: {word}')

    shutdownJVM()
