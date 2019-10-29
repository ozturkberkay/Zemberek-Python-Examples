"""
Zemberek: Simple Classification Example
Documentation: https://bit.ly/2BNKPmP
Java Code Example: https://bit.ly/2JsoO1i
fastText Documentation: https://bit.ly/31YVBS8
"""

from os.path import isfile, join
from subprocess import call

from jpype import JClass, getDefaultJVMPath, java, shutdownJVM, startJVM

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    FastTextClassifier: JClass = JClass(
        'zemberek.classification.FastTextClassifier'
    )
    TurkishTokenizer: JClass = JClass(
        'zemberek.tokenization.TurkishTokenizer'
    )
    ScoredItem: JClass = JClass(
        'zemberek.core.ScoredItem'
    )
    Paths: JClass = JClass(
        'java.nio.file.Paths'
    )

    path: str = join('..', '..', 'data', 'classification')

    if not isfile(join(path, 'news-title-category-set.model')):

        print('Could not find a model. Training a new one...')

        if not isfile(join(path, 'news-title-category-set')):
            raise FileNotFoundError(
                'Could not train a model!'
                ' Please include news-title-category-set!'
            )

        call([
            'java',
            '-jar', '../../bin/zemberek-full.jar',
            'TrainClassifier',
            '-i', '../../data/classification/news-title-category-set',
            '-o', '../../data/classification/news-title-category-set.model',
            '--learningRate', '0.1',
            '--epochCount', '50',
            '--applyQuantization',
            '--cutOff', '15000'
        ])

    classifier: FastTextClassifier = FastTextClassifier.load(
        Paths.get(
            join(
                '..', '..', 'data', 'classification',
                'news-title-category-set.model'
            )
        )
    )

    sentence: str = 'Beşiktaş berabere kaldı.'

    processed: str = ' '.join([
        str(token)
        for token in TurkishTokenizer.DEFAULT.tokenizeToStrings(sentence)
    ]).lower()

    results: java.util.ArrayList = classifier.predict(processed, 3)

    for i, result in enumerate(results):
        print(
            f'\nItem {i + 1}: {result.item}',
            f'\nScore {i + 1}: {result.score}'
        )

    shutdownJVM()
