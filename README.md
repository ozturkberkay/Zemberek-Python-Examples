# Zemberek Python Examples

> Zemberek Turkish NLP examples written in Python using the JPype package.

Zemberek is a Java-based natural language processing (NLP) tool created for the Turkish language. This repository contains the Python implementations of the [official Zemberek examples](https://github.com/ahmetaa/zemberek-nlp/tree/master/examples/src/main/java/zemberek/examples) for learning purposes.

## Table of Contents

| Folder                    | Description                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| classification            | fastText examples                                                                                                                                                                 |
| core                      | histogram                                                                                                                                                                         |
| morphology                | stemming, lemmatization, diacritics analysis, POS tag analysis, morphological analysis, word generation, sentence disambiguation, informal word analysis, adding dictionary items |
| named-entitiy-recognition | on hold                                                                                                                                                                           |
| normalization             | document correction, noisy text normalization, spell checking                                                                                                                     |
| tokenization              | sentence boundary detection, turkish tokenization                                                                                                                                 |
  
## Requirements

1.  Python 3.6+

## Getting Started

1. Clone this library and `cd` into it.
    ```shell
    $ git clone https://github.com/ozturkberkay/Zemberek-Python-Examples.git
    $ cd Zemberek-Python-Examples
    ```

2.  Install the required packages. Using `virtualenv` is highly encouraged!

    ```shell
    $ python -m pip install --upgrade pip virtualenv
    $ python -m virtualenv .env
    $ # Windows: .env\Scripts\activate
    $ source .env/bin/activate
    $ python -m pip install -r requirements.txt
    ```

3. Download the required Zemberek files:

    ```shell
    $ python -m downloader 
    ```

    Optionally, you can manually download all the data and version `0.17.1` of Zemberek distribution from [the official Zemberek Drive folder](https://drive.google.com/drive/folders/0B9TrB39LQKZWSjNKdVcwWUxxUm8?usp=sharing) and put the files in the corresponding folders:

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

## Usage

1. Run `python -m main category.example args`.

    ```shell
    $ python -m main classification.simple_classification "Fenerbahçe bu maçı galibiyet ile sonlandırdı."
    ...

        News classification example. Trains a new model if there is no model
        available.

        Args:
            sentence (str): Sentence to classify.
        
    Sentence: Fenerbahçe bu maçı galibiyet ile sonlandırdı.

    Item 1: __label__spor 
    Score 1: -0.009194993413984776

    Item 2: __label__magazin 
    Score 2: -6.12613582611084

    Item 3: __label__kültür_sanat 
    Score 3: -6.226541996002197
    ```

## Known Bugs

-   During the model training, `fastText` will print errors. It still works, just ignore them.

## Changelog

-   2020-12-05
    -   Automatic downloader for Zemberek files.
    -   Simple CLI entry-point to run the examples with custom data. 
    -   JPype1 v1.2.0 upgrade. This should fix some memory leak issues.
    -   Code quality improvements.
    -   Fixes for broken links.
-   2019-10-29
    -   Zemberek v0.17.1 upgrade.
    -   JPype1 v0.7.0 upgrade.
    -   Code style changes.
    -   Bug-fixes.
    -   License is now the same with Zemberek (Apache v2.0).
-   2018-12-01
    -   Classification, morphology, normalization and tokenization examples.
