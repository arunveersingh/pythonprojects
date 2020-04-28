from array import array
from urllib.request import urlopen

from datastructures import words, evenodd, arrayrotation

story = urlopen(
        "https://scroll.in/article/959016/the-political-fix-why-india-will-have-a-hard-time-navigating-its-way-out-of"
        "-the-covid-19-lockdown")
story_words = []
for line in story:
    line_words = line.decode("utf-8").split()
    # print("line_words: ", line_words)
    for word in line_words:
        story_words.append(word)
        # print(story_words)
    for word in story_words:
        print(word)


words.fetch_words()
evenodd.even_or_odd(10)
evenodd.even_or_odd(3)
evenodd.is_permutation(["a", "b", "c"], ["c", "b", "a"])

arrayrotation.rotate_array(array("i", [1, 2, 3]))



