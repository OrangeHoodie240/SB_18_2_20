def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowel_list = []
    index_list = []
    for i in range(len(s)):
        char = s[i]
        if(char.lower() in 'aeiou'):
            vowel_list.append(char)
            index_list.append(i)

    # swap vowels
    vowel_list = vowel_list[::-1]

    results = ''
    vowel_index = 0
    for i in range(len(s)):
        j = index_list[vowel_index] if(vowel_index < len(index_list)) else None
        if(i == j):
            results += vowel_list[vowel_index]
            vowel_index += 1
        else:
            results += s[i]

    return results