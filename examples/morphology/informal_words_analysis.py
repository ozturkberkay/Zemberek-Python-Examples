"""
Zemberek: Informal Turkish Words Analysis
Documentation: https://bit.ly/2WpvvXg
Java Code Example: https://bit.ly/2MUvOG9
"""

from os.path import join

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
    RootLexicon: JClass = JClass('zemberek.morphology.lexicon.RootLexicon')
    InformalAnalysisConverter: JClass = JClass(
        'zemberek.morphology.analysis.InformalAnalysisConverter'
    )

    morphology: TurkishMorphology = (
        TurkishMorphology.builder().setLexicon(
            RootLexicon.getDefault()
        ).ignoreDiacriticsInAnalysis().useInformalAnalysis().build()
    )

    analyses: java.util.ArrayList = (
        morphology.analyzeAndDisambiguate('okuycam diyo').bestAnalysis()
    )

    print('\nAnalysis:\n')

    for analysis in analyses:
        print(f'{str(analysis.surfaceForm())}-{analysis}')

    print('\nConverting formal surface form:\n')

    converter: InformalAnalysisConverter = (
        InformalAnalysisConverter(morphology.getWordGenerator())
    )

    for analysis in analyses:
        print(str(converter.convert(analysis.surfaceForm(), analysis)))

    shutdownJVM()
