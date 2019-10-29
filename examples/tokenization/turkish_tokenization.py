"""
Zemberek: Turkish Tokenization Example
Java Code Example: https://bit.ly/2PsLOkj
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

    TurkishTokenizer: JClass = JClass('zemberek.tokenization.TurkishTokenizer')
    Token: JClass = JClass('zemberek.tokenization.Token')

    tokenizer: TurkishTokenizer = TurkishTokenizer.DEFAULT

    print('\nToken Iterator Example:\n')

    inp: str = 'İstanbul\'a, merhaba!'
    print(f'Input = {inp}')
    token_iterator = tokenizer.getTokenIterator(JString(inp))
    for token in token_iterator:
        print((
            f'Token = {token}'
            f'\n | Content = {token.content}'
            f'\n | Normalized = {token.normalized}'
            f'\n | Type = {token.type}'
            f'\n | Start = {token.start}'
            f'\n | End = {token.end}\n'
        ))

    print('Default Tokenization Example:\n')

    tokenizer: TurkishTokenizer = TurkishTokenizer.DEFAULT
    inp: str = 'İstanbul\'a, merhaba!'
    print(f'Input = {inp}')
    for i, token in enumerate(tokenizer.tokenizeToStrings(
        JString('İstanbul\'a, merhaba!')
    )):
        print(f' | Token String {i} = {token}')

    print('\nCustom Tokenization Example:\n')

    tokenizer: TurkishTokenizer = TurkishTokenizer.builder().ignoreTypes(
        Token.Type.Punctuation,
        Token.Type.NewLine,
        Token.Type.SpaceTab
    ).build()
    inp: str = 'Saat, 12:00'
    print(f'Input = {inp}')
    for i, token in enumerate(tokenizer.tokenize(JString(inp))):
        print(f' | Token {i} = {token}')

    shutdownJVM()
