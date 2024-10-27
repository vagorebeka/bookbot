def countwords(text):
    words = text.split()
    wordcount = len(words)
    return wordcount

def countchars(text):
    text = text.lower()
    chars_counts = {}
    for i in text:
        if i in chars_counts:
            chars_counts[i] += 1
        else:
            chars_counts[i] = 1
    return chars_counts

def sort_on(dict):
    return dict["count"]

def printreport(characters):
    dict = {}
    for i in characters:
        if i.isalpha():
            dict[i] = characters[i]
    charlist = []
    for i in dict:
        chardict = {}
        chardict["char"] = i
        chardict["count"] = dict[i]
        charlist.append(chardict)
    charlist.sort(reverse=True, key=sort_on)
    for i in charlist:
        charcount = i
        print(f"The {charcount["char"]} character was found {charcount["count"]} times.")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number_of_words = countwords(file_contents)
        #print(number_of_words)
        characters_count = countchars(file_contents)
        #print(characters_count)
        print(f"Begin report of {f.name}")
        printreport(characters_count)
        print("End of report")

main()