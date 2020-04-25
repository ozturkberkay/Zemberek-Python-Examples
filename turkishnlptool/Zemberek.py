import os
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM
import re
from .utils import *

class Zemberek:
    def __init__(self,*args):
        if len(args)>0:
            JAVAPATH = args[0]
        else:
            JAVAPATH = getDefaultJVMPath()
        print(f'JAVA PATH: {JAVAPATH}')
        self.MAINFOLDER = os.path.dirname(os.path.realpath(__file__))
        self.ZEMBEREK_PATH = os.path.join(self.MAINFOLDER,"zemberek-full.jar")
        startJVM(JAVAPATH,'-ea',f'-Djava.class.path={self.ZEMBEREK_PATH}',convertStrings=False)
        self.verbose = False
        #
        self.TurkishMorphology = JClass('zemberek.morphology.TurkishMorphology')
        self.DictionaryItem = JClass('zemberek.morphology.lexicon.DictionaryItem')
        self.RootAttribute = JClass('zemberek.core.turkish.RootAttribute')
        self.PrimaryPos = JClass('zemberek.core.turkish.PrimaryPos')
        self.SecondaryPos = JClass('zemberek.core.turkish.SecondaryPos')
        self.WordAnalysis = JClass('zemberek.morphology.analysis.WordAnalysis')
        self.AnalysisFormatters = JClass('zemberek.morphology.analysis.AnalysisFormatters')
        self.RootLexicon = JClass('zemberek.morphology.lexicon.RootLexicon')
        self.InformalAnalysisConverter = JClass('zemberek.morphology.analysis.InformalAnalysisConverter')
        self.TurkishSentenceExtractor = JClass('zemberek.tokenization.TurkishSentenceExtractor')
        self.TurkishTokenizer = JClass('zemberek.tokenization.TurkishTokenizer')
        self.Token = JClass('zemberek.tokenization.Token')
        self.TurkishSpellChecker = JClass('zemberek.normalization.TurkishSpellChecker')
        self.TurkishSentenceNormalizer = JClass('zemberek.normalization.TurkishSentenceNormalizer')
        self.PrimaryPos = JClass('zemberek.core.turkish.PrimaryPos')
        self.SecondaryPos = JClass('zemberek.core.turkish.SecondaryPos')
        # Derived ones
        self.DefaultMorphology = self.TurkishMorphology.createWithDefaults() # Default Morphology..
        self.InformalMorphology = self.TurkishMorphology.builder().setLexicon(self.RootLexicon.getDefault()).ignoreDiacriticsInAnalysis().useInformalAnalysis().build()

        stopwordfile = os.path.join(self.MAINFOLDER,"turkish_stopwords.txt")
        with open(stopwordfile, 'r',encoding = 'utf-8') as f :
            StopWordsRead = f.readlines()
            self.StopWords = list(map(removeNewLine,StopWordsRead))
        f.close()

    def __del__(self):
        shutdownJVM()

    def isStopWord(self,word) :
        '''Is the given word is a stop word?'''
        isstop = (word in self.StopWords) or word in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        return isstop

    def addNoun(self,noun_dict):
        '''This function allows to add a new noun to dictionary.'''
        dct = list(map(JString,noun_dict)) + [self.PrimaryPos.Noun, self.SecondaryPos.ProperNoun]
        new_items = self.DictionaryItem(*dct)
        self.DefaultMorphology.invalidateCache()
        self.DefaultMorphology.getMorphotactics().getStemTransitions().addDictionaryItem(new_items)

    def addVerb(self,noun_dict):
        '''This function allows to add a new verb to dictionary.'''
        dict = list(map(JString,noun_dict)) + [self.PrimaryPos.Verb, self.SecondaryPos.None_]
        new_items = self.DictionaryItem(*dict)
        self.DefaultMorphology.invalidateCache()
        self.DefaultMorphology.getMorphotactics().getStemTransitions().addDictionaryItem(new_items)

    def analyze(self,word):
        '''This function analyzes the given word.'''
        results = self.DefaultMorphology.analyze(JString(word))
        if self.verbose:
            for result in results :
                print(
                    f'\nLexical and Surface: {str(result.formatLong())}'
                    f'\nOnly Lexical: {str(result.formatLexical())}'
                    '\nOflazer Style:'
                    f'{str(self.AnalysisFormatters.OFLAZER_STYLE.format(result))}'
                )
        return results, str(results)

    def stemLemma(self,word):
        '''This function stems and lemmatizes the given word.'''
        results = self.DefaultMorphology.analyze(JString(word))
        stems = []
        lemmas = []

        for result in results :
            stems.append([str(stem) for stem in result.getStems()])
            lemmas.append([str(stem) for stem in result.getLemmas()])
            if self.verbose:
                print(
                    f'{str(result.formatLong())}',
                    f'\n\tStems =', ' '.join(stems[-1]),
                    f'\n\tLemmas =', ' '.join(lemmas[-1]) )
        return stems, lemmas

    def sentenceDisambugation(self,sentence):
        '''This function analyzes given a sentence.'''
        stems = []
        lemmas = []
        if bool(sentence):
            analysis = self.DefaultMorphology.analyzeSentence(sentence)
            results = self.DefaultMorphology.disambiguate(sentence, analysis).bestAnalysis()
        else:
            return stems,lemmas

        for i, result in enumerate(results, start=1) :
            stems.append([str(stem) for stem in result.getStems()])
            lemmas.append([str(stem) for stem in result.getLemmas()])
            if self.verbose:
                print(
                    f'\nAnalysis {i}: {str(result.formatLong())}'
                    f'\n\tStems =', ' '.join(stems[-1]),
                    f'\n\tLemmas =', ' '.join(lemmas[-1]) )

        return stems, lemmas

    def informalWordAnalysis(self,sentence):
        '''This function analyzees informal words'''
        analyses = self.InformalMorphology.analyzeAndDisambiguate(sentence).bestAnalysis() # : java.util.ArrayList

        print('\nAnalysis:\n')
        for analysis in analyses :
            print(f'{str(analysis.surfaceForm())}-{analysis}')

        print('\nConverting formal surface form:\n')

        converter = self.InformalAnalysisConverter(self.InformalMorphology.getWordGenerator())

        if self.verbose:
            for analysis in analyses :
                print(str(converter.convert(analysis.surfaceForm(), analysis)))

        return list(map(str, analyses))

    def findPOS(self,sentence):
        '''This function finds parts of speech in a given sentence.'''
        analysis = self.DefaultMorphology.analyzeAndDisambiguate(sentence).bestAnalysis()
        pos = []

        for i, analysis in enumerate(analysis, start=1) :
            if self.verbose:
                print(
                    f'\nAnalysis {i}: {analysis}',
                    f'\nPrimary POS {i}: {analysis.getPos()}'
                    f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}')

            pos.append(
                f'{str(analysis.getLemmas()[0])}'
                f'-{analysis.getPos().shortForm}'
            )

        if self.verbose:
            print(f'\nFull sentence with POS tags: {" ".join(pos)}')

        return pos

    def sentenceBoundary(self,paragraph):
        '''This function detects bounds of a sentence.'''
        sentences = self.TurkishSentenceExtractor.DEFAULT.fromParagraph(paragraph)
        if self.verbose:
            for i, sent in enumerate(sentences) :
                print(f'Sentence {i + 1}: {sent}')

        return list(map(str,sentences)) # Return lists

    def sentenceTokenization(self,sentence):
        '''This function tokenizes a simple sentence.'''
        token_iterator = self.TurkishTokenizer.DEFAULT.tokenizeToStrings(JString(sentence))

        if self.verbose:
            print('\nToken Iterator Example:\n')
            for i, token in enumerate(token_iterator) :
                print(f'Token {i} = {token}')

        return list(map(str,token_iterator))

     # Normalization functions.

    def correctDocument(self,document):
        '''This function corrects misspelled words in a document.'''
        spell_checker = self.TurkishSpellChecker(self.DefaultMorphology)
        tokens = self.TurkishTokenizer.ALL.tokenize(JString(document))

        corrected_tokens = []

        for token in tokens :
            text = token.content
            if (
                    token.type != self.Token.Type.NewLine
                    and token.type != self.Token.Type.SpaceTab
                    and token.type != self.Token.Type.Punctuation
                    and token.type != self.Token.Type.RomanNumeral
                    and token.type != self.Token.Type.UnknownWord
                    and token.type != self.Token.Type.Unknown
                    and not spell_checker.check(text)
            ) :
                suggestions = list(spell_checker.suggestForWord(token.content))
                if suggestions :
                    suggestion: str = str(suggestions[0])
                    print(f'Correction: {token.content} -> {suggestion}.')
                    corrected_tokens.append(suggestion)
                    continue
            corrected_tokens.append(str(token.content))

        correctedDoc = ' '.join(corrected_tokens)
        if self.verbose:
            print('\nCorrected Document:\n', correctedDoc)

        return correctedDoc

    def normalizeDocument(self,document):
        '''This function normalizes a given document.'''
        Paths: JClass = JClass('java.nio.file.Paths')
        path1 = Paths.get(os.path.join('.', 'req_data'))
        path2 = Paths.get(os.path.join('.', 'req_data', 'lm.2gram.slm'))
        normalizer = self.TurkishSentenceNormalizer(self.TurkishMorphology.createWithDefaults(),path1,path2)

        normalizedDoc = normalizer.normalize(JString(document))
        if self.verbose:
            print(f'\nNoisy : {document}')
            print(f'\nNormalized : {normalizedDoc}' )

        return str(normalizedDoc)

    def NER(self,sentence):
        '''This function performs Named Entity Recognition for a sentence.'''
        # Use pre-trained model.
        pass

    def analyze2(self,word,add_swt=True):
        '''
        Extract possible subword combinations from a word.
        add_swt: Add additive sub-words starting with ##
        '''
        analysis_all, _ = self.analyze(word)
        #if len(analysis_all) == 0:
        #    return [[word]]
        allanalysis = []
        for analysis_single in analysis_all:
            stranal = str(analysis_single)
            strng = re.sub('\[\S+:\S+\] ','',stranal)
            parts = re.split('[|\+]', strng)
            isNotFirst = False
            partanalysis = []
            for part in parts:
                if ':' in part:
                    root = re.split(':',part)[0]
                    if isNotFirst and not add_swt:
                        break
                    elif isNotFirst:
                        root = '##' + root
                    else:
                        isNotFirst = True # Remaining parts are not first..
                    partanalysis.append(root)
            allanalysis.append(partanalysis)
        return allanalysis

    def uniqueSubWords(self,word):
        '''This function returns all possible subwords of given word as a SET.'''
        analyzed = self.analyze2(word)
        subwords = [subword for analyze_x in analyzed for subword in analyze_x]
        return set(subwords)

    def normalizeMultipleSentences(self, paragraph):
        # Remove newline chaacters from the document
        paraflat = removeNewLine(paragraph)
        # Split sentences
        para_divd = self.sentenceBoundary(paraflat)
        # Normalize
        n_fcn = lambda x: normalizeText(x,False,False,True).split()
        norm_txt = list(map(n_fcn,para_divd))
        return norm_txt


    # This function may be removed..
    def parseWords(self, paragraph, add_swt=True, rmnewline=True, lwcase=True, expunc=True):
        '''
        Returns dictionary of word counts.
        add_swt: Add additive sub-words starting with ##
        rmnewline: Remove new lines.
        lwcase: Lowercase text.
        expunc: Expand punctuation.
        '''
        para = normalizeText(paragraph,rmnewline,lwcase,expunc)
        words = para.split()
        count_dict = {}
        norm_txt = ''
        for word in words:
            # print(f'size: {len(self.analyze2(word))} \n')
            a2 = self.analyze2(word,add_swt)
            if len(a2) == 0: # If word cannot be analyzed, pass as it is.
                # print(f'not parsed word: {word}')
                txt = word
                analysis = [txt]
            else:
                # get longest first word as analysis...
                a_lens = list(map(lambda x: len(x[0]),a2)) # analysis lengths.
                idx = a_lens.index(max(a_lens))
                analysis = a2[idx] # get first analysis.
                if not add_swt and self.isStopWord(analysis[0]): # If word is a stop-word, and additive words are disregard.
                    continue 
                txt = ' '.join(analysis)
            for a in analysis:
                if a not in count_dict.keys():
                    count_dict[a]=1
                else:
                    count_dict[a] += 1

            norm_txt = norm_txt + ' ' + txt
        return norm_txt, count_dict

