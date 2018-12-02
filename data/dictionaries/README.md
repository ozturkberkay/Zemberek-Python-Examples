# Zemberek Dictionary Data
> You can utilize [the official wiki](https://github.com/ahmetaa/zemberek-nlp/wiki/Text-Dictionary-Rules) to create your own lexicon and save it in this folder.

## Usage

1. Create your dictionary inside this folder. Read [the wiki](https://github.com/ahmetaa/zemberek-nlp/wiki/Text-Dictionary-Rules) before proceeding!

2. Create a `TurkishMorphology` object using your custom dictionary. The example below can be found in: `examples\morphology\stem-and-lemmatize\standard-morphology.py`

    ```python
    lexicon = RootLexicon.builder().setLexicon(RootLexicon.DEFAULT).addTextDictionaries(Paths.get('../../../data/dictionaries/lexicon.txt')).build()
    morphology = TurkishMorphology.create(lexicon)
    ```
