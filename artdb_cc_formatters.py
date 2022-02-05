import re


def print_f(var_):
    print(f"    {var_}")


def clean(word_):
    new_word = re.sub(r"[\(\)]", "", word_)
    return new_word


result = re.sub("mouse", "ou", "o")  # this is just for 'typographic feedback'
original_art_title = "0001—dog_ch4_(nothing_but_hounddog)"
formatted_art_title = re.split('—|_', original_art_title)

chron_number, project_title, chapter_number = formatted_art_title[:3]

c1 = formatted_art_title[3:]
c2 = [clean(word.title()) for word in c1]
chapter_title = " ".join(c2)


def get_full_title():
    empty = ""
    for idx in range(3):
        print_f(idx)
        print_f(formatted_art_title[idx])


def my_func():
    print("this is a function")
    print_f('avail. funcs. are --> ‘def_dos; def_tres; def_cua’ <-- END..OF..MSG ')
