# Zemberek Dictionary Data

> You can utilize [the official wiki](https://github.com/ahmetaa/zemberek-nlp/wiki/Text-Dictionary-Rules) to create your own lexicon and save it in this folder. Or use `zemberek_downloader.py` to automatically download the files.

## Usage

1. Create your dictionary inside this folder. Read [the related wiki article](https://github.com/ahmetaa/zemberek-nlp/wiki/Text-Dictionary-Rules) for more information.

2. Create a `TurkishMorphology` object using your custom dictionary Read [the related wiki article](https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology#creating-turkishmorphology-object) for more information.

    ```python
    lexicon = RootLexicon.builder().addDefaultLexicon().addTextDictionaries(Paths.get('PATH')).build()
    morphology = TurkishMorphology.create(lexicon)
    ```
