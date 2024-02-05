pip install pylint

import pylint
import time
import argparse

def read_words_from_file(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words_in_line = line.strip().split()
            words.extend(words_in_line)
    return words

def count_word_frequencies(words):
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def main():
    parser = argparse.ArgumentParser(description="Word Count Tool")
    parser.add_argument('file', type=str, help="File path to read data from.")
    parser.add_argument('action', choices=['read', 'count'], help="Action to perform: 'read' to read words, 'count' to count frequencies.")
    args = parser.parse_args()

    start_time = time.time()

    if args.action == 'read':
        words = read_words_from_file(args.file)
        print(f"Words read: {len(words)}")
    elif args.action == 'count':
        words = read_words_from_file(args.file)
        frequencies = count_word_frequencies(words)
        for word, frequency in sorted(frequencies.items()):
            print(f"{word}: {frequency}")

    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()