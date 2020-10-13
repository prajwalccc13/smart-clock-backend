def list_to_csv(text):
    '''
    This function is used to convert a list of text in comma separated values.

    Arguments: 
    text - (list) A list of strings you want to convert to comma separated values (csv). 

    Returns:
    csv - (str) String with comma separated values.
    '''
    if text is not None:
        csv = str()
        for words in text:
            csv += words + ', '
        return csv


def tokenize(text):
    '''
    This function is used to convert string of space seperated words into a list.

    Arguments: 
    text - (string) String of words seperated by space. 

    Returns:
    tokens - (list) A list of words.
    '''
    
    tokens = text.split()
    return tokens