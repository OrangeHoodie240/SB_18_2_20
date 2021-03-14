def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    frequencyLog = dict() 
    for num in nums:
        frequencyLog[num] = frequencyLog.get(num, 0) + 1
    
    mode = None
    highestOccurence = 0
    for num, freq in frequencyLog.items():
        if(freq > highestOccurence):
            mode = num
            highestOccurence = freq
    return mode