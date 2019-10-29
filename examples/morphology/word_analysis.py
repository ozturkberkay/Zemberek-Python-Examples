"""
Zemberek: Word Analysis Example
Documentation: https://bit.ly/2MTmfr1
Java Code Example: https://bit.ly/2MV2Hmj
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
    AnalysisFormatters: JClass = JClass(
        'zemberek.morphology.analysis.AnalysisFormatters'
    )
    WordAnalysis: JClass = JClass('zemberek.morphology.analysis.WordAnalysis')

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    word: str = 'kalemi'

    print(f'\nWord: {word}')

    results: WordAnalysis = morphology.analyze(JString(word))

    for result in results:
        print(
            f'\nLexical and Surface: {str(result.formatLong())}'
            f'\nOnly Lexical: {str(result.formatLexical())}'
            '\nOflazer Style:'
            f'{str(AnalysisFormatters.OFLAZER_STYLE.format(result))}'
        )

    shutdownJVM()
