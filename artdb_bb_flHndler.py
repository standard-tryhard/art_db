import csv

artworks_rootlist_file = 'artdb_dd_rootlist.csv'
artworks_appendlist_file = 'artdb_dd_appendlist.csv'

def unpack_a_csv(a_file_):
    all_bunnies_: dict[int, str] = {}
    with open(a_file_, 'r') as f:
        bunny_reader_ = csv.reader(f)

        next(bunny_reader_)
        for idx_, bunny_row_ in enumerate(bunny_reader_):
            all_bunnies_[idx_] = bunny_row_

        idx_ += 1

    next_artwork_idx_ = idx_ + 1
    return all_bunnies_, next_artwork_idx_


def append_to_csv(artwork_, a_file_):
    file_ = open(a_file_, "a+", newline='')

    with file_:
        writer_ = csv.writer(file_)
        writer_.writerow(artwork_)


def merge_csv(csv_root_, csv_append_):
    csv_receives_updates = open(csv_root_, "w+")

    new_data = [l for l in open(csv_append_).readlines()]

    with csv_receives_updates:
        for line in new_data:
            csv_receives_updates.write(line)


if __name__ == "__main__":
    print("hello from main")
    # merge_csv(artworks_rootlist_file, artworks_appendlist_file)

