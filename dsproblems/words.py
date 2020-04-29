from urllib.request import urlopen
import sys


def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        # print("line_words: ", line_words)
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(items):
    for word in items:
        print(word)


def main(url, completion_mess="I am done"):
    words = fetch_words(url)
    print_items(words)
    print(completion_mess)


if __name__ == "__main__":
    main(sys.argv[1])

print(__name__)
