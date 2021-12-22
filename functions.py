def words_alphabetical(message):
    '''
    Checks if the words in the message are arranged in alphabetical order

    Parameters
    -----
    - message

        string: Message to be checked

    Returns
    -----
    boolean value (whether words in the message are arranged in alphabetical order)
    '''

    # Split the message into its constituent words and
    # store them in <words> if their first character is a letter
    words_etc = message.split()
    words = [word.lower() for word in words_etc if word[0].isalpha()]

    # If there are fewer than 5 such words, disregard message
    if len(words) < 5:
        return False

    # Perform the check
    return words == sorted(words)


def all_letters(message):
    '''
    Checks if the message contains every letter in the English alphabet

    Parameters
    -----
    - message

        string: Message to be checked

    Returns
    -----
    boolean value (whether the message contains every letter in the English alphabet)
    '''

    # Split the message into separate characters and
    # store them in <all_chars> if they are letters
    all_chars = [char1.lower() for char1 in message if char1.isalpha()]

    # If there are fewer than 26 letters, disregard message (condition cannot possibly be met)
    if len(all_chars) < 26:
        return False

    # Create a set to store the unique group of letters of the message
    curr_set = set()

    for char2 in all_chars:
        curr_set.add(char2)

        # If there are 26 UNIQUE letters, condition has been met
        if len(curr_set) == 26:
            return True

    return False
