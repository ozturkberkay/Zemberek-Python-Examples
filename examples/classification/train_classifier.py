# -*- coding: utf-8 -*-

import subprocess
                                                   
## Zemberek: Train Classifier Example
# Documentation: https://github.com/ahmetaa/zemberek-nlp/tree/master/classification#training
# fastText Documentation: https://fasttext.cc/docs/en/support.html

# Training with quantization enabled. To disable quantization,
# Remove arguments: --applyQuantization --cutOff 15000
subprocess.call([   
                    'java', '-jar', '../../bin/zemberek-full.jar', 
                    'TrainClassifier', '-i', '../../data/classification/news-title-category-set', 
                    '-o', '../../data/classification/news-title-category-set.model', 
                    '--learningRate', '0.1', '--epochCount', '50', 
                    '--applyQuantization', '--cutOff', '15000' # <- Quantization
                ])