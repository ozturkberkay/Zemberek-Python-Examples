"""
Zemberek: Classification Example Base
Documentation: https://bit.ly/2BNKPmP
Original Java Example: https://bit.ly/2Prce6m
fastText Documentation: https://bit.ly/31YVBS8
"""

import re
from pathlib import Path
from typing import List

from jpype import JClass, JString, java

__all__: List[str] = ['ClassificationExampleBase']


TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
SentenceAnalysis: JClass = JClass(
    'zemberek.morphology.analysis.SentenceAnalysis'
)
SentenceWordAnalysis: JClass = JClass(
    'zemberek.morphology.analysis.SentenceWordAnalysis'
)
SingleAnalysis: JClass = JClass('zemberek.morphology.analysis.SingleAnalysis')
TurkishSentenceNormalizer: JClass = JClass(
    'zemberek.normalization.TurkishSentenceNormalizer'
)
TurkishTokenizer: JClass = JClass('zemberek.tokenization.TurkishTokenizer')
Token: JClass = JClass('zemberek.tokenization.Token')
Type: JClass = JClass('zemberek.tokenization.Token.Type')


class ClassificationExampleBase:
    """Exact Python implementation of the original Java code."""

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    @classmethod
    def generate_set_with_lemmas(
        cls, lines: List[str], lemmas_path: Path
    ) -> None:
        with open(lemmas_path, 'w', encoding='utf-8') as lemma_file:
            for line in [
                cls.remove_non_words(
                    cls.replace_words_with_lemma(line)
                ).lower()
                for line in lines
            ]:
                lemma_file.write(f'{line}\n')

    @classmethod
    def generate_set_with_split(
        cls, lines: List[str], split_path: Path
    ) -> None:
        with open(split_path, 'w', encoding='utf-8') as split_file:
            for line in [
                cls.remove_non_words(cls.split_words(line)).lower()
                for line in lines
            ]:
                split_file.write(f'{line}\n')

    @classmethod
    def generate_set_tokenized(
        cls, lines: List[str], tokenized_path: Path
    ) -> None:
        with open(tokenized_path, 'w', encoding='utf-8') as tokens_file:
            for line in [
                cls.remove_non_words(
                    java.lang.String.join(
                        JString(' '),
                        TurkishTokenizer.DEFAULT.tokenizeToStrings(
                            JString(line)
                        ),
                    )
                ).lower()
                for line in lines
            ]:
                tokens_file.write(f'{line}\n')

    @classmethod
    def split_words(cls, sentence: str) -> str:
        tokens: List[str] = sentence.split()
        label: java.lang.String = JString(tokens[0])
        del tokens[0]
        sentence = ' '.join(tokens)

        if len(sentence) == 0:
            return JString(sentence)

        analysis: SentenceAnalysis = cls.morphology.analyzeAndDisambiguate(
            JString(sentence)
        )
        res: java.util.ArrayList = java.util.ArrayList()
        res.add(label)

        for word_analysis in analysis:
            best: SingleAnalysis = word_analysis.getBestAnalysis()
            inp: java.lang.String = word_analysis.getWordAnalysis().getInput()

            if best.isUnknown():
                res.add(inp)
                continue

            lemmas: java.util.ArrayList = best.getLemmas()

            if len(lemmas[0]) < len(inp):
                res.add(lemmas[0])
                res.add(JString('_' + str(inp[len(lemmas[0])])))
            else:
                res.add(lemmas[0])

        return java.lang.String.join(JString(' '), res)

    @classmethod
    def process_ending(cls, inp: str) -> str:
        for pattern, value in {
            r'[ae]': 'A',
            r'[ıiuü]': 'I',
            r'[kğ]': 'K',
            r'[cç]': 'C',
            r'[dt]': 'D',
        }.items():
            inp = re.sub(pattern, value, inp)
        return inp

    @classmethod
    def replace_words_with_lemma(cls, sentence: str) -> str:
        tokens: List[str] = sentence.split()
        label: str = tokens[0]
        del tokens[0]
        sentence = ' '.join(tokens)

        if len(sentence) == 0:
            return sentence

        analysis: SentenceAnalysis = cls.morphology.analyzeAndDisambiguate(
            JString(sentence)
        )
        res: java.util.ArrayList = java.util.ArrayList()
        res.add(JString(label))

        for word_analysis in analysis:
            best: SingleAnalysis = word_analysis.getBestAnalysis()

            if best.isUnknown():
                res.add(word_analysis.getWordAnalysis().getInput())
                continue

            lemmas: java.util.ArrayList = best.getLemmas()
            res.add(lemmas[0])

        return java.lang.String.join(JString(' '), res)

    @classmethod
    def remove_non_words(cls, sentence: JString) -> str:
        if not sentence:
            return ''

        doc_tokens: List[Token] = list(
            TurkishTokenizer.DEFAULT.tokenize(sentence)
        )
        reduced: List[str] = []

        for token in doc_tokens:
            text: str = str(token.getText())

            if text[0] == '_' or '__' in text:
                reduced.append(text)
                continue

            token_type: Token.Type = token.getType()

            if token_type in {
                Token.Type.Mention,
                Token.Type.HashTag,
                Token.Type.URL,
                Token.Type.Punctuation,
                Type.RomanNumeral,
                Token.Type.Time,
                Token.Type.UnknownWord,
                Token.Type.Unknown,
            }:
                continue

            reduced.append(text)

        return ' '.join(reduced)
