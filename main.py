import string

def main():
    path_to_file = "books/frankenstein.txt"

    text = get_book_text(path_to_file)

    print(f"--- Begin report of books/frankenstein.txt ---\n"
          f"{number_of_words(text)} words found in the document\n")
    for e in count_characters(text):
        print(f"The {e["letter"]} character was found {e["count"]} times")
    print("--- End report ---")


def number_of_words(file):
    words = file.split()
    return len(words)

def count_characters(file):
    letters = list(string.ascii_lowercase)
    count = []
    lower_case_file = file.lower()

    for letter in letters:
        count.append({"letter": letter, "count": lower_case_file.count(letter)})

    count.sort(reverse=True, key=sort_on)

    return count



def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    

def sort_on(dict):
    return dict["count"]
        
main()