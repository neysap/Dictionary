import unittest

from cd_wordcount import *

class WordCountDictionary_Test(unittest.TestCase):
#changed the name MyTestCase to what i wanted to which is WordCountDictionary_Test

    #now we create our test functions (erase the one given and create your own)
    def test_freq_count(self):
        freq = {}  # create empty dict for testing
        freq_count('Here is a line of text.', freq) # call function(freq_count) with its parameters
        # a line of text(which the function is programed to count the # of times each word appears in the text)
        # we also reference dict (which the function is programed to update the dict when this happens)

        #now we must test the dictionary after calling the function... LET'S SEE IF ITS WORKING?!
        self.assertIn('here', freq)  # test existence of word 'here' to be in the dictionary(& it should be a key)
        self.assertEqual(1, freq['here'])  # test count of word (key)... meaning it should count 'here' 1 time

        freq_count('here is another line of text.', freq)  # call function again but with different line of text
        self.assertEqual(2, freq['here'])  # test updated count of word (key)...
             # meaning it should count 'here' twice now that we've added another line of text with the same word in it


    def test_most_frequent(self):
        freq = {'here': 3, 'is': 2, 'a': 1, 'line': 2, 'of': 2, 'text.': 2}  # create dict for testing

        most_frequent_word = most_frequent(freq)  # call function and get return
        self.assertEqual('here', most_frequent_word[0])  # test expected word
        self.assertEqual(3, most_frequent_word[1])  # test expected count


if __name__ == '__main__':
    unittest.main()
