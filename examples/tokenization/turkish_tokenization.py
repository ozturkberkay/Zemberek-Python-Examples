"""
Zemberek: Turkish Tokenization Example
Java Code Example: https://bit.ly/2PsLOkj
"""
from jpype import JClass, JString

TurkishTokenizer: JClass = JClass('zemberek.tokenization.TurkishTokenizer')
TokenIterator: JClass = JClass(
    'zemberek.tokenization.TurkishTokenizer.TokenIterator'
)
Token: JClass = JClass('zemberek.tokenization.Token')


def run(sentence: str) -> None:
    """
    Turkish sentence tokenization example.

    Args:
        sentence (str): Sentence to tokenize.
    """
    tokenizer: TurkishTokenizer = TurkishTokenizer.DEFAULT

    print('\nToken Iterator Example:\n')

    token_iterator: TokenIterator = tokenizer.getTokenIterator(
        JString(sentence)
    )

    for token in token_iterator:
        print(
            f'Token = {token}'
            f'\n | Content = {token.content}'
            f'\n | Normalized = {token.normalized}'
            f'\n | Type = {token.type}'
            f'\n | Start = {token.start}'
            f'\n | End = {token.end}\n'
        )

    print('Default Tokenization Example:\n')

    tokenizer: TurkishTokenizer = TurkishTokenizer.DEFAULT

    for i, token in enumerate(tokenizer.tokenizeToStrings(JString(sentence))):
        print(f' | Token String {i} = {token}')

    print('\nCustom Tokenization With Ignored Types Example:\n')

    tokenizer: TurkishTokenizer = (
        TurkishTokenizer.builder()
        .ignoreTypes(
            Token.Type.Punctuation, Token.Type.NewLine, Token.Type.SpaceTab
        )
        .build()
    )
    for i, token in enumerate(tokenizer.tokenize(JString(sentence))):
        print(f' | Token {i} = {token}')
