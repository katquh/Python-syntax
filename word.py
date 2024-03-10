def print_upper_words(words,must_start_with):
    """Given a list of words, return a list of words that start with given letters
    # this should print "HELLO", "HEY", "YO", and "YES"

    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})