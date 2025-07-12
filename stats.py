def count_words(words_to_be_counted):
    count_list = []
    count_list = words_to_be_counted.split()
    return len(count_list)

def count_characters(characters_to_be_counted):
    character_count_list = []
    character_count_dict = {}
    characters_to_be_counted = characters_to_be_counted.lower()
    character_count_list = list(characters_to_be_counted)
    for c in character_count_list:
        if c not in character_count_dict:
            character_count_dict[c] = 0
            character_count_dict[c] += 1
        else:
            character_count_dict[c] += 1
    return character_count_dict

def sort_on(items):
    return items["num"]

def sort_and_print_dict(dict_to_sort):
    list_of_dicts = []
    for key, value in dict_to_sort.items():
        temp_dict = {"char": key, "num": value}
        list_of_dicts.append(temp_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)
    for entry in list_of_dicts:
        if entry["char"].isalpha() == False:
            pass
        else:
            print(f"{entry["char"]}: {entry["num"]}")