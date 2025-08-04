def get_word_count(book):
    list_of_words = book.split()
    return len(list_of_words)

def count_characters(text):
    results = dict()
    for char in text.lower():
        if char in results:
            results[char] = results[char] + 1
        else: 
            results[char] = 1
    return results

def sort_on(items):
    return items["num"]

def prepare_dict(input_dict):
    list_of_dicts = list()
    for entry in input_dict.keys():
        list_of_dicts.append({'character':entry, 'num':input_dict[entry]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
