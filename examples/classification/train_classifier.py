"""
Zemberek: Train Classifier Example
Documentation: https://bit.ly/2PtzNLB
fastText Documentation: https://bit.ly/2JtMP80
"""

from subprocess import call

if __name__ == '__main__':

    call([
        'java',
        '-jar',
        '../../bin/zemberek-full.jar',
        'TrainClassifier',
        '-i',
        '../../data/classification/news-title-category-set',
        '-o',
        '../../data/classification/news-title-category-set.model',
        '--learningRate',
        '0.1',
        '--epochCount',
        '50',
        '--applyQuantization',
        '--cutOff',
        '15000'
    ])
