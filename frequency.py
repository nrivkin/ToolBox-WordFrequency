""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg

Noah Rivkin

"""

import string
import os


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    if os.path.exists(file_name): # checks if the file has already been downloaded
        f = open(file_name, 'r')
        lines = f.readlines()  # reads each line of the text into lines
        currline = 0
        while lines[currline].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:  # reads threough lines until it finds the end of the intro
            currline += 1  # moves onto next line
        lines = lines[currline + 1:]  # lines is every thing from the line after START OF ... to the end of the text
        f.close
        word_list = []
        for line in lines:
            line = line.split()
            for word in line:
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                word_list.append(word)
        return word_list
    else:
        print ("\nError: File not found\n")
        return None


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    histogram = {}
    for word in word_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    top_n_words = []
    top_n_freqs = []
    for i in range(n):
        most_common = ''
        most_times = 0
        for key in histogram:
            if key not in top_n_words:
                num = histogram[key]
                if num > most_times:
                    most_times = num
                    most_common = key
        top_n_words.append(most_common)
        top_n_freqs.append(most_times)
    return top_n_words

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation + string.whitespace)
    word_list = get_word_list('pg32325.txt')
    top_words = get_top_n_words(word_list, 100)
    for word in top_words:
        print(word)
