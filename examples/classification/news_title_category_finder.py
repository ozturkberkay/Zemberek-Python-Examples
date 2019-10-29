"""
Zemberek: News Title Category Finder Example
Documentation: https://bit.ly/2BNKPmP
Original Java Example: https://bit.ly/32TUtQU
fastText Documentation: https://bit.ly/31YVBS8
"""

from collections import Counter
from os.path import isfile, join
from typing import List, Optional

from jpype import JClass, JString, shutdownJVM

from classification_example_base import ClassificationExampleBase

EvaluateClassifier: JClass = JClass(
    'zemberek.apps.fasttext.EvaluateClassifier'
)
TrainClassifier: JClass = JClass(
    'zemberek.apps.fasttext.TrainClassifier'
)


class NewsTitleCategoryFinder(ClassificationExampleBase):

    @classmethod
    def __read(cls, path: str) -> List[str]:
        with open(path, 'r', encoding='utf-8') as lines:
            return [line for line in lines]

    @classmethod
    def data_info(cls, path: str) -> List[str]:
        lines = cls.__read(path)
        print(f'Total Lines: {len(lines)}')
        for item in Counter(
            [line[0:line.find(' ')] for line in lines]
        ).most_common():
            print(f'({item[1]})\t{item[0]}')
        return lines

    @classmethod
    def evaluate(
        cls,
        test_size: int,
        path: Optional[str] = None,
        lines: Optional[List[str]] = None
    ):
        if lines is None:
            if path is None:
                raise ValueError('You should provide a path!')
            lines = cls.__read(path)
        if test_size <= 0 or test_size > len(lines):
            raise ValueError(
                '\'test_size\' must be bigger than'
                ' 0 and less than the dataset size!'
            )
        train_path: str = f'{path}.train'
        test_path: str = f'{path}.test'
        with open(train_path, 'w', encoding='utf-8') as f:
            for line in lines[test_size:len(lines)]:
                f.write(line)
        with open(test_path, 'w', encoding='utf-8') as f:
            for line in lines[0:test_size]:
                f.write(line)
        model_path: str = f'{path}.model'
        if not isfile(model_path):
            TrainClassifier().execute(
                JString('-i'),
                JString(train_path),
                JString('-o'),
                JString(model_path),
                JString('--learningRate'),
                JString('0.1'),
                JString('--epochCount'),
                JString('70'),
                JString('--dimension'),
                JString('100'),
                JString('--wordNGrams'),
                JString('2')
            )
        print('Testing...')
        cls.test(test_path, f'{path}.predictions', model_path)

    @classmethod
    def test(cls, test_path: str, predictions_path: str, model_path: str):
        EvaluateClassifier().execute(
            JString('-i'),
            JString(test_path),
            JString('-m'),
            JString(model_path),
            JString('-o'),
            JString(predictions_path),
            JString('-k'),
            JString('1')
        )


if __name__ == '__main__':

    data_path = join(
        '..',
        '..',
        'data',
        'classification',
        'news-title-category-set'
    )

    print('\nEvaluation with raw data:\n')

    lines = NewsTitleCategoryFinder.data_info(data_path)
    NewsTitleCategoryFinder.evaluate(1000, data_path, lines)

    print('\nEvaluation with tokenized-lowercase data:\n')

    tokenized_path = f'{data_path}.tokenized'
    if not isfile(tokenized_path):
        NewsTitleCategoryFinder.generate_set_tokenized(lines, tokenized_path)
    NewsTitleCategoryFinder.evaluate(1000, path=tokenized_path)

    print('\nEvaluation with lemma-lowercase data:\n')

    lemma_path = f'{data_path}.lemmas'
    if not isfile(lemma_path):
        NewsTitleCategoryFinder.generate_set_with_lemmas(lines, lemma_path)
    NewsTitleCategoryFinder.evaluate(1000, path=lemma_path)

    print('\nEvaluation with Stem-Ending-lowercase data:\n')

    split_path = f'{data_path}.split'
    if not isfile(split_path):
        NewsTitleCategoryFinder.generate_set_with_split(lines, split_path)
    NewsTitleCategoryFinder.evaluate(1000, path=split_path)

    shutdownJVM()
