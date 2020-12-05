"""
Zemberek: Sentence Boundary Detection Example
Documentation: https://bit.ly/2JopMvt
Java Code Example: https://bit.ly/2PrG7Dw
"""

from jpype import JClass

TurkishSentenceExtractor: JClass = JClass(
    'zemberek.tokenization.TurkishSentenceExtractor'
)


def run(paragraph: str) -> None:
    """
    Sentence boundary detection example.

    Args:
        paragraph (str): Paragraph to detect sentence boundaries.
    """

    extractor: TurkishSentenceExtractor = TurkishSentenceExtractor.DEFAULT

    sentences = extractor.fromParagraph(paragraph)

    for i, word in enumerate(sentences):
        print(f'Sentence {i+1}: {word}')
