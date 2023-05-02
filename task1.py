def Replace(string, position=5, character='K'):
    # make the text a list#
    mytext = list(string)
    # Replace the char as per the position#
    mytext[position] = character
    # Rearrange the text#
    final = ''.join(mytext)
    print(final)


Replace('abracadabra')
