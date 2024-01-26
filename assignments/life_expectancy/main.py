"""Main Module"""

# import libraries
import argparse

from load_data import load_data
from cleaning import clean_data
from save_data import save_data
from regions import Region

def main(i_path, region, o_path): # pragma: no cover
    """
    Main function which config the arparse and
    calls the functions to load, clean and save the tsv file.

    Functions description:
    - load_data: Function wich loads the tsv file.
    - clean_data: Function which cleans a DataFrame by:
                  replacing "," with '\t',
                  replacing ":" with NaN values,
                  renaming column "geo\time" for "region",
                  unpivot the dataframe,
                  removing characters from value column,
                  converting columns to the respetive type,
                  dropping the null values,
                  filtering the dataframe by region.
    - save_data: Function which saves a dataframe as csv.

    :param i_path: Input file path.
    :param region: Region to filter the dataframe.
    :param o_path: Output file path to save the cleaned dataframe.
    """
    
    # read tsv file
    data = load_data(i_path)
    # clean tsv file
    df = clean_data(data, region)
    # save dataframe as csv
    save_data(df, o_path)

    return df


if __name__ == "__main__":  # pragma: no cover

    # config argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help= "Input file path.") 
    parser.add_argument('-o', help = "Output file path.")
    parser.add_argument("-r",  type = Region, choices = list(Region), \
                        default= Region.PT, help = "Desire region to filter the csv.")
    args = parser.parse_args()

    # Check if all required arguments are provided
    required_args = ["i", "o"]
    for arg in required_args:
        if arg not in args:
            raise ValueError(f"Missing argument: '{arg}'")
        
    main(args.i, args.r, args.o)       
# %%
