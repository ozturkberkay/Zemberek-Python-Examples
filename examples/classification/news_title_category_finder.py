"""
Zemberek: News Title Category Finder Example
Documentation: https://bit.ly/2BNKPmP
Original Java Example: https://bit.ly/32TUtQU
fastText Documentation: https://bit.ly/31YVBS8
"""

import collections
from pathlib import Path
from typing import List, Optional, cast

from jpype import JClass, JString

from examples import DATA_PATH
from examples.classification.classification_example_base import (
    ClassificationExampleBase,
)

__all__: List[str] = ['NewsTitleCategoryFinder', 'run']

EvaluateClassifier: JClass = JClass(
    'zemberek.apps.fasttext.EvaluateClassifier'
)
TrainClassifier: JClass = JClass('zemberek.apps.fasttext.TrainClassifier')


class NewsTitleCategoryFinder(ClassificationExampleBase):
    """Exact Python implementation of the original Java code."""

    @classmethod
    def _read(cls, path: Path) -> List[str]:
        with open(path, 'r', encoding='utf-8') as lines_file:
            return [line for line in lines_file]

    @classmethod
    def data_info(cls, path: Path) -> List[str]:
        lines = cls._read(path)
        print(f'Total Lines: {len(lines)}')
        for item in collections.Counter(
            [line[0 : line.find(' ')] for line in lines]
        ).most_common():
            print(f'({item[1]})\t{item[0]}')
        return lines

    @classmethod
    def evaluate(
        cls,
        test_size: int,
        path: Optional[Path] = None,
        lines: Optional[List[str]] = None,
    ) -> None:
        if lines is None:
            if path is None:
                raise ValueError('You should provide a path!')
            lines = cls._read(path)

        if test_size <= 0 or test_size > len(lines):
            raise ValueError(
                '\'test_size\' must be bigger than'
                ' 0 and less than the dataset size!'
            )

        train_path: Path = cast(Path, path).with_suffix('.train')
        test_path: Path = cast(Path, path).with_suffix('.test')

        with open(train_path, 'w', encoding='utf-8') as train_file:
            for line in lines[test_size : len(lines)]:
                train_file.write(line)

        with open(test_path, 'w', encoding='utf-8') as test_file:
            for line in lines[0:test_size]:
                test_file.write(line)

        model_path: Path = cast(Path, path).with_suffix('.model')

        if not model_path.is_file():
            TrainClassifier().execute(
                JString('-i'),
                JString(str(train_path)),
                JString('-o'),
                JString(str(model_path)),
                JString('--learningRate'),
                JString('0.1'),
                JString('--epochCount'),
                JString('70'),
                JString('--dimension'),
                JString('100'),
                JString('--wordNGrams'),
                JString('2'),
            )
        print('Testing...')
        cls.test(
            test_path, cast(Path, path).with_suffix('.predictions'), model_path
        )

    @classmethod
    def test(
        cls, test_path: Path, predictions_path: Path, model_path: Path
    ) -> None:
        EvaluateClassifier().execute(
            JString('-i'),
            JString(str(test_path)),
            JString('-m'),
            JString(str(model_path)),
            JString('-o'),
            JString(str(predictions_path)),
            JString('-k'),
            JString('1'),
        )


def run() -> None:
    """News classification model training."""

    data_path: Path = DATA_PATH.joinpath(
        'classification', 'news-title-category-set'
    )

    print('\nEvaluation with raw data:\n')

    lines_: List[str] = NewsTitleCategoryFinder.data_info(data_path)
    NewsTitleCategoryFinder.evaluate(1000, data_path, lines_)

    print('\nEvaluation with tokenized-lowercase data:\n')

    tokenized_path: Path = data_path.with_suffix('.tokenized')
    if not tokenized_path.is_file():
        NewsTitleCategoryFinder.generate_set_tokenized(lines_, tokenized_path)
    NewsTitleCategoryFinder.evaluate(1000, path=tokenized_path)

    print('\nEvaluation with lemma-lowercase data:\n')

    lemma_path: Path = data_path.with_suffix('.lemmas')
    if not lemma_path.is_file():
        NewsTitleCategoryFinder.generate_set_with_lemmas(lines_, lemma_path)
    NewsTitleCategoryFinder.evaluate(1000, path=lemma_path)

    print('\nEvaluation with Stem-Ending-lowercase data:\n')

    split_path: Path = data_path.with_suffix('.split')
    if not split_path.is_file():
        NewsTitleCategoryFinder.generate_set_with_split(lines_, split_path)
    NewsTitleCategoryFinder.evaluate(1000, path=split_path)
