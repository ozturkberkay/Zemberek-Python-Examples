# Zemberek Python Examples
> Zemberek Turkish NLP examples written in Python using the JPype package.

:exclamation: **Requires Zemberek 0.16! 0.17 update with new features and fixes are coming soon!**

 Zemberek is a Java-based, natural language processing (NLP) tool, created for the Turkish language. This repository contains a bunch of Python implementations of the [official Zemberek examples](https://github.com/ahmetaa/zemberek-nlp/tree/master/examples/src/main/java/zemberek/examples) for learning purposes. 
 
## Installation

 1. Install the JPype package:

    ```console
    pip install JPype1
    ```

 2. Download all the data and the **version 0.16** distribution of Zemberek from [the official Zemberek Drive folder](https://drive.google.com/drive/folders/0B9TrB39LQKZWSjNKdVcwWUxxUm8?usp=sharing) and put the files in the corresponding folders:
    
        .
        +-- bin
        |   +-- zemberek-full.jar
        +-- data
        |   +-- classification
        |       +-- news-title-category-set
        |       +-- news-title-category-set.lemmas
        |       +-- news-title-category-set.tokenized
        |   +-- dictionaries
        |   +-- lm
        |       +-- lm.2gram.slm
        |   +-- ner
        |   +-- normalization
        |       +-- ascii-map
        |       +-- lookup-from-graph
        |       +-- split
        +-- examples
        .gitignore
        LICENSE
        README.md

## Usage

| Folder | Description |
| ----------- | ----------- |
| classification | fastText examples |
| core | core functionalities |
| morphology | morphology analysis, stemming, lemmatization, ambiguity resolution, informal words analysis, adding dictionaries, word generation, finding POS tags... |
| named-entitiy-recognition | on hold |
| normalization | document correction, noisy text normalization, spell checking |
| tokenization | sentence boundary detection, turkish tokenization |

`cd` to the folder you want and run the script you want using `python the_example_you_want.py`. Everything is documented and ready to go.

## Changelog

* 0.0.1
    * Classification, morphology, normalization and tokenization examples are added. NER examples are on hold until I acquire a Turkish NER dataset.

## Meta

Berkay Öztürk – info@berkayozturk.net

Distributed under the GNU General Public License v3.0 license. See ``LICENSE`` for more information.
[https://github.com/ozturkberkay/Zemberek-Python-Examples](https://github.com/ozturkberkay/Zemberek-Python-Examples)
