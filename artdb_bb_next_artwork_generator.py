# artdb_bb_next_artwork_generator

import csv
import time

import artdb_bb_flHndler, artdb_cc_formatters

database_columns = [
    'Chronological Number'
    , 'Title'
    , 'Subtitle'
    , 'Year Signed'
    , 'Media'
    , 'Substrate'
    , 'Width in CM'
    , 'Height in CM'
    , 'Price'
    , 'Tag 1'
    , 'Tag 2'
    , 'Tag 3'
]

artwork_csv_database = 'artdb_dd_rootlist.csv'


def assign_new_artwork():
    print(f"{'===NEW ARTWORK===':^80}")

    db_, next_new_idx_ = artdb_bb_flHndler.unpack_a_csv(artwork_csv_database)
    next_new_idx_fmttd = f"{next_new_idx_:06}"
    new_artwork_ = []
    new_artwork_.append(next_new_idx_fmttd)

    for idx, f_name in enumerate(database_columns[1:]):
        bookmarks_ = []
        rsp_ = input("{0:^40}".format(f_name.upper()))
        if not rsp_ or rsp_ == ' ':
            new_artwork_.append("...")
            bookmarks_.append(idx)
        else:
            new_artwork_.append(rsp_)

    return new_artwork_, bookmarks_


def validate_new_artwork(newly_created_artwork_, bookmarks_):
    print("\n")
    print(f"{'•••ARTWORK READY•••':^50}")
    contains_all_info = "..." not in newly_created_artwork_[:6]

    if contains_all_info:
        for field, value in zip(database_columns, newly_created_artwork_):
            time.sleep(.2)
            print(f"{field.upper():^50} :::: {value}")

        rsp_ = input(f"\n{'OK? TO WRITE TO DB? ':^50}  ")

    else:
        for idx in bookmarks_:
            print(database_columns[idx])
            time.sleep(.33)
        rsp_ = input(f"{'THOSE ARE DEFAULTS WRITTEN TO DB, OK?':^50}  ")

    return rsp_



def write_new_artwork_toDB(var_):
    pass


if __name__ == "__main__":
    artdb_cc_formatters.print_f("printed from __main__")



# ===== EXTRA ====== #
# def propagate_dict(list_):
#     bunny_indv_dict_ = {}
#     print(f'\nARTWORK NO.{list_[0]}')
#     for fieldname_ in list_:
#         print(fieldname_)

