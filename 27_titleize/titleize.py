def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split(' ')
    results = ''
    for i in range(len(words)):
        word = ''
        for j in range(len(words[i])):
            if(j == 0):
                word = words[i][j].upper() 
            else:
                word += words[i][j].lower()
        results += word
        if(i < len(words) - 1):
            results += ' '
    return results

