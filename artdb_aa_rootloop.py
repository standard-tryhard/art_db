import sys
import time

import artdb_bb_flHndler
import artdb_bb_next_artwork_generator
import artdb_cc_formatters


def get_total_db_len(_filename):
    with open(f"{_filename}", 'r') as fin:
        _total_works_in_volume = len(fin.readlines()) - 1

    return _total_works_in_volume


def print_db(_filename):
    with open(f"{_filename}", 'r') as fin:
        for l in fin.readlines():
            time.sleep(.5)
            artdb_cc_formatters.print_f(l)


def end_session():
    rsp_ = input(f"{'OK TO OVERWRITE ROOTLIST WITH NEW DATA?':^50}")
    if rsp_ and rsp_.lower() != "no":
        artdb_bb_flHndler.merge_csv(artdb_bb_flHndler.artworks_rootlist_file,
                                    artdb_bb_flHndler.artworks_appendlist_file)


res_A, bookmarks = artdb_bb_next_artwork_generator.assign_new_artwork()
res_B = artdb_bb_next_artwork_generator.validate_new_artwork(res_A, bookmarks)

if res_B and res_B.lower != "no":
    artdb_cc_formatters.print_f(f"{'Writing; to DB...':^50}")
    artdb_bb_flHndler.append_to_csv(res_A, artdb_bb_flHndler.artworks_appendlist_file)
    end_session()
