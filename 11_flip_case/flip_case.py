def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    upper = to_swap.upper() 
    lower = to_swap.lower() 
    result = ''
    for char in phrase:
        if(char == upper or char == lower):
            result += upper if(char == lower) else lower
        else:
            result += char
        
    return result
            
