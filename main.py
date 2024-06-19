def get_book_text(path):
    with open(path) as f:
        return f.read()

def return_word_count(str):
    words = str.split()
    return len(words)

def return_character_count(str):
    characters = {}
    text = str.lower()
    for x in text:
        if x not in characters.keys():
            characters[x] = 0
        characters[x] += 1
    return characters

def dict_to_list(dict):
    resultList = []
    for key in dict.keys():
        if key.isalpha():
            element = {"char" : key, "occurence" : dict[key]}
            resultList.append(element)
    return resultList

def sort_on(dict):
    return dict["occurence"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = return_word_count(text)
    #print(return_character_count(text))
    characters = dict_to_list(return_character_count(text))
    characters.sort(reverse=True, key=sort_on)
    print("--- Begin report of "+ book_path + " ---")
    print(str(wc) + " words found in the document")
    for element in characters:
        print("The '" + element["char"] +"' character was found " + str(element["occurence"]) + " times")
    print("--- End report ---")


main()