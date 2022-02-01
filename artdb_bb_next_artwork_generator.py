# artdb_bb_next_artwork_generator

import sys
import re
import csv
import itertools
import time
from typing import Dict

bunny_fields = [
	'Chronological Number'
	,'Title'
	,'Year Signed or Completed'
	,'Media'
	,'Width in CM'
	,'Height in CM'
	,'Price'
	,'Quantity'
	,'Tag 1'
	,'Tag 2'
	,'Tag 3']

bunnies_csv = 'artdb_rootlist.csv'
# bunnies_unsorted_items = bunny_house_extraction.items()
# bunnies_ordrd_dict = collections.OrderedDict(sorted(bunnies_unsorted_items))
# bunnies_ordrd_dict_with_default_values = populate_dict_with_default_values()

def get_next_artwork():
	return '000001'

def unpack_a_csv(a_file_):
	all_bunnies_: dict[int, str] = {}
	with open(a_file_, 'r') as f:
		bunny_reader_ = csv.reader(f)

		next(bunny_reader_)
		for idx_, bunny_row_ in enumerate(bunny_reader_):
			# propagate_dict(bunny_row_)
			all_bunnies_[idx_] = bunny_row_


		idx_ += 1

	next_artwork_idx_ = idx_ + 1
	return all_bunnies_, next_artwork_idx_

def propagate_dict(list_):
	bunny_indv_dict_ = {}
	print(f'\nARTWORK NO.{list_[0]}')
	for fieldname_ in list_:
		print(fieldname_)

def assign_new_artwork():
	print(f"{'===NEW ARTWORK===':^80}")

	db_, next_new_idx_ = unpack_a_csv(bunnies_csv)
	next_new_idx_fmttd = f"{next_new_idx_:06}"
	new_artwork_ = []
	new_artwork_.append(next_new_idx_fmttd)


	for f_name in bunny_fields[1:]:
		rsp_ = input("{0:^40}".format(f_name.upper()) )
		if not rsp_:
			new_artwork_.append("...")
		else:
			new_artwork_.append(rsp_)

	return new_artwork_

def validate_new_artwork(newly_created_artwork_):
	print("\n")
	print(f"{'•••ARTWORK READY•••':^80}")
	contains_all_info = "..." not in newly_created_artwork_[:6]

	if contains_all_info:
		for field, value in zip(bunny_fields, newly_created_artwork_):
			time.sleep(.2)
			print(f"{field.upper():^40} :::: {value}")

		rsp_ = input(f"{'OK? TO WRITE TO DB? ':^80}\n")

	else:
		rsp_ = input("Are you sure you want to leave the following blank?\n")

	return rsp_

if __name__ == "__main__":
	print("printed from __main__")





