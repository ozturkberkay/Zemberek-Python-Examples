# Zemberek Dictionary Data

> You can utilize [the official wiki](https://github.com/ahmetaa/zemberek-nlp/wiki/Text-Dictionary-Rules) to create your own lexicon and save it in this folder.

## Usage

1. Create your dictionary inside this folder. Read [the wiki](https://github.com/ahmetaa/zemberek-nlp/wiki/Text-Dictionary-Rules) before proceeding!

2. Create a `TurkishMorphology` object using your custom dictionary Read [the wiki](https://github.com/ahmetaa/zemberek-nlp/tree/master/morphology#creating-turkishmorphology-object) before proceeding!

    ```python
    lexicon = RootLexicon.builder().addDefaultLexicon().addTextDictionaries(Paths.get('PATH')).build()
    morphology = TurkishMorphology.create(lexicon)
    ```
