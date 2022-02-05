import glob
import pandas as pd


all_filenames = [i for i in glob.glob('*.csv')]
print(all_filenames)

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "summary.csv", index=False, encoding='utf-8-sig')