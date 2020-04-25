import re

'''Text processing functions.'''

def removeNewLine(text):
    '''Removes New Line Character and splits accordingly.'''
    _subst = re.sub(r'\\n', ' ', text)  # Replacing İ to i because lower function cannot handle it.
    subst = re.sub(r'\n', ' ', _subst)  # Replacing İ to i because lower function cannot handle it.
    dropped = ' '.join(subst.split())
    return dropped

def removePunc(text):
    '''Removes New Line Character and splits accordingly.'''
    splittext = re.sub(r'[^\w\s]', ' ', text) 
    outtext = ' '.join(splittext.split())
    return outtext

# May be cleared soon.
def number2str(text):
    '''Convert numbers to string which indicates number of points.'''
    splittext = text.split()
    isnum = list(map(lambda x: x.isdigit(), splittext))
    isnumidx = [i for i, x in enumerate(isnum) if x]
    for i in isnumidx:
        splittext[i] = '<NUMBER'+str(len(splittext[i]))+'>'
    outtext = ' '.join(splittext)
    return outtext

def lowercase(text):
    '''Lowercase the text.'''
    _text = text.replace('İ','i').replace('I','ı') # For turkish language.
    lowtext = _text.lower()
    return lowtext

def expandPunc(text):
    '''Reduce unnecessary punctuations and seperate from words with whitespace. 
    Used to seperate punctuation from words.'''
    _text = text
    _text = re.sub(r'[.]', ' . ', _text)
    _text = re.sub(r'[,]', ' , ', _text)
    _text = re.sub(r'[;]', ' ; ', _text)
    _text = re.sub(r'[:]', ' : ', _text)
    _text = re.sub(r'[?]', ' ? ', _text)
    _text = re.sub(r'[!]', ' ! ', _text)
    _text = re.sub(r'[%]', ' % ', _text)
    #_text = re.sub(r'[\']', ' \' ', _text) # do not expand apostrophe
    _text = re.sub(r'[/]', ' / ', _text)
    _text = re.sub(r'[’]', '', _text) # make it empty
    # Common things.
    #_text = re.sub(' +', ' ', _text) 

    outtext = ' '.join(_text.split())
    return outtext

# GENERIC FUNCTIONS

def normalizeText(text, rmnewline=True, lwcase=True, expunc=True):
    '''Generic Text normalizer. ,
    Remove new lines;
    Lowercase;
    Adjust punctuations;
    Replace all unknown characters with #
    rmnewline: Remove new lines.
    lwcase: Lowercase text.
    expunc: Expand punctuation.
    '''
    _text = text
    if rmnewline:
        _text = removeNewLine(_text)
    if lwcase:
        _text = lowercase(_text)
    if expunc:
        _text = expandPunc(_text)
    # qwertyuıopğüasdfghjklşizxcvbnmöç1234567890.,:;?!%'
    # for other characters, replace everything with #
    keep_chars = 'QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç1234567890.,:;?!%\'/ ' # do not forget space
    unique_txtch = list(set(_text)) # Unique characters of the text
    isoutlier_txtch = list(map(lambda x: x not in keep_chars, unique_txtch)) # which ones are in 

    for i,char in enumerate(unique_txtch):
        if isoutlier_txtch[i]:
            # print(f'---{char}---')
            # raw_char = r'{}'.format(char)
            # _text = re.sub(raw_char,'_',_text)
            _text = _text.replace(char,'')
    return _text

