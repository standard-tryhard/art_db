import re
import time

# result = re.sub("mouse", "ou", "o") #this is just for 'typographic feedback'
original_art_title = "0001—dog_ch4_(nothing_but_hounddog)"
formatted_art_title = re.split('—|_', original_art_title)



def clean(word_):
	new_word = re.sub(r"[\(\)]", "", word_)
	return new_word


def get_full_title():
	empty = ""
	for idx in range(3):
		print(idx)
		print(formatted_art_title[idx])

def my_func():
#	print(“this is a function”)
	print('avail. funcs. are --> ‘def_dos; def_tres; def_cua’ <-- END..OF..MSG ')



chron_number, project_title, chapter_number = formatted_art_title[:3]


c1 = formatted_art_title[3:]
c2 = [clean(word.title()) for word in c1]
chapter_title = " ".join(c2)


def get_total_db_len(_filename):
	with open(f"{_filename}",'r') as fin:
		_total_works_in_volume = len(fin.readlines()) - 1

	return _total_works_in_volume


def print_db(_filename):
	with open(f"{_filename}",'r') as fin:
		for l in fin.readlines():
			time.sleep(.5)
			print(l)



print_db("artdb_dd_maindb.csv")