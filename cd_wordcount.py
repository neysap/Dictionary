#Create a word_count program
#Create a function freq_count that parses a provided line of text
# and stores a count of each word in a provided freq dict


def freq_count(line, freq):
    """Parses given line of text. Updates the given freq dictionary with
    words as keys and the frequency of words as values.
    """
    words = line.split()  # get the words by splitting on whitespace
    for word in words: #remember word is a dummy variable... objects like 'here' (as tested) will be placed into it
        word = word.lower()  # convert each word to lower case

        # creates a word that'll be a key in dict, if it doesn’t yet exist
        # increments count (value)
        freq[word] = freq.get(word, 0) + 1

#created a test

#Create a function most_frequent that finds the most frequent word (and count) in the provided freq dict
def most_frequent(freq):
    """Given the freq dictionary with words (keys) and frequencies (values),
    finds the most frequent word.
    """
    #GETS THE KEYS(words) IN THE DICT
    words = list(freq.keys())  # convert dict(freq)_keys object to a list
    frequencies = list(freq.values())  # convert dict_values object to list
    # note, these 2 lists are not sorted, but at least ordered the same as each other

    # get max of frequencies list
    max_freq = max(frequencies)

    # get index of max freq
    desired_index = frequencies.index(max_freq)

    # get word that's associated with the max freq
    max_word = words[desired_index]

    # return both the word and max freq as tuple
    return (max_word, max_freq)

#Now complete the main function in our program
def main():
    freq = {}
    line = input("Enter text, line by line, and use 'quit' to exit the program")
    while line.lower() != 'quit':
        freq_count(line, freq) #this will count the individual word in the line and update dict
        line = input() #populate another line and iterate through this cycle until used enters quit

    for word in freq:
        print(word + ' occurs ' + str(freq[word]) + ' times')

    most_freq = most_frequent(freq)
    print('The most frequent word is', most_freq[0], 'which occurs', most_freq[1], 'times')

if __name__ == "__main__":
    main()




