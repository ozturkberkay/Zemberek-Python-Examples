"""
Zemberek: Train Classifier Example
Documentation: https://bit.ly/2PtzNLB
fastText Documentation: https://bit.ly/2JtMP80
"""

import subprocess
from pathlib import Path
from typing import List

from examples import JAVA_PATH, ZEMBEREK_PATH, DATA_PATH

__all__: List[str] = ['run']


def run():
    """
    Trains the news classifier model.
    """

    news_path: Path = DATA_PATH.joinpath(
        'classification', 'news-title-category-set'
    )

    subprocess.run(
        [
            JAVA_PATH,
            '-jar',
            ZEMBEREK_PATH,
            'TrainClassifier',
            '-i',
            news_path,
            '-o',
            news_path.with_suffix('.model'),
            '--learningRate',
            '0.1',
            '--epochCount',
            '50',
            '--applyQuantization',
            '--cutOff',
            '15000',
        ],
        check=True,
    )
