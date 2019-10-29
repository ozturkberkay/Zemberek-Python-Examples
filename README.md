# Zemberek Python Examples

> Zemberek Turkish NLP examples written in Python using the JPype package.

Zemberek is a Java-based natural language processing (NLP) tool created for the Turkish language. This repository contains a bunch of Python implementations of the [official Zemberek examples](https://github.com/ahmetaa/zemberek-nlp/tree/master/examples/src/main/java/zemberek/examples) for learning purposes.

## Requirements

1.  Python 3.6+
2.  JPype1 0.7.0

## Getting Started

1.  Install the JPype package.

    For `pip` users:

    ```console
    pip install JPype1
    ```

    For `conda` users:

    ```console
    conda install -c conda-forge jpype
    ```

    You can also clone my environment:

    ```console
    # Pip
    pip install -r requirements.txt

    # Conda
    conda env create -f environment.yml
    ```

2.  Download all the data and version `0.17.1` of Zemberek distribution from [the official Zemberek Drive folder](https://drive.google.com/drive/folders/0B9TrB39LQKZWSjNKdVcwWUxxUm8?usp=sharing) and put the files in the corresponding folders:

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

1. `cd` to the directory of your desired example.
2. Run the example via `python`.

## Table of Contents

| Folder                    | Description                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| classification            | fastText examples                                                                                                                                                                 |
| core                      | histogram                                                                                                                                                                         |
| morphology                | stemming, lemmatization, diacritics analysis, POS tag analysis, morphological analysis, word generation, sentence disambiguation, informal word analysis, adding dictionary items |
| named-entitiy-recognition | on hold                                                                                                                                                                           |
| normalization             | document correction, noisy text normalization, spell checking                                                                                                                     |
| tokenization              | sentence boundary detection, turkish tokenization                                                                                                                                 |

## Known Bugs

-   During the model training, fastText will print errors. It still works, just ignore them. If you run the code the second time, model training will be skipped and the console output will be clean of errors.

## Changelog

-   29.10.2019
    -   Zemberek 0.17.1 update.
    -   JPype 0.7.0 update.
    -   Code style changes.
    -   Bug-fixes.
    -   License is now the same with Zemberek (Apache v2.0).
-   01.12.2018
    -   Classification, morphology, normalization and tokenization examples.
