import re
from string import ascii_lowercase

def is_pangram(sentence):
        pangram = re.sub('[^a-z]','',sentence.lower())
        return set(pangram) == set(ascii_lowercase)