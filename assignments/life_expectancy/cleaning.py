# Script to clean data/life_expectancy_raw.tsv ___//

# import libraries
import io
import csv
import argparse
import pandas as pd
import numpy as np

# config argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", help= "Input file path.") 
parser.add_argument("-o", help = "Output file path.")
parser.add_argument("-r", default="PT", help = "Desire region to filter the csv.")
args = parser.parse_args()


if __name__ == "__main__":  # pragma: no cover

    def clean_data(input_path:str, output_path:str, region:str) -> csv:
        '''
        Function that reads a raw tsv file from a path
        and cleans it by:
        - Replacing "," with '\t'
        - Replacing ":" with NaN values
        - Renaming column "geo\time" for "region"
        - Transforming the tsv to dataframe
        - unpivot the dataframe
        - remove characters from value column
        - convert columns to the respetive type
        - drop null values
        - filter dataframe by region
        - convert dataframe to csv

        :return cleaned csv file.
        '''

        print("\nCleaning tsv file...\n")

        # open and read raw data file
        with open(input_path, 'r', encoding="utf8") as raw_data:
            data = raw_data.read()

        # replace ',' with '\t' values in 
        data_clear = data.replace(',' , '\t')

        # Create a StringIO object
        data_buffer = io.StringIO(data_clear)

        # Read the TSV data into a list of lists
        tsv_data = []
        for row in csv.reader(data_buffer, delimiter='\t'):
            tsv_data.append(row)

        # transform into dataframe 
        df = pd.DataFrame(tsv_data[1:], columns=tsv_data[0])

        # rename "geo\time" column with "region"
        df.columns.values[3] = 'region'

        # replace ":" as NaN
        df_replace_nulls = df.replace(to_replace=':.*', value=np.nan, regex=True)

        # unpivot dataframe
        df_unpivot = pd.melt(
                    df_replace_nulls, 
                    id_vars=list(df_replace_nulls.iloc[:, :4].columns),
                    value_vars=list(df_replace_nulls.iloc[:, 4:].columns),
                    var_name='year'
        )

        # remove strings from value column
        # .replace({r'([a-zA-Z]*)':""},regex=True)
        df_unpivot['value'] = df_unpivot['value'].str.replace('[^\d\-+\.]', '', regex=True)

        # convert value column into float
        df_unpivot['value'] = df_unpivot['value'].apply(pd.to_numeric, errors="raise")

        # convert "year" column to integer
        df_unpivot['year'] = df_unpivot['year'].astype(int)
        
        # drop nulls from "value" column
        df_clean = df_unpivot.dropna()
        
        # filter dataframe by desire region
        df_clean = df_clean[df_clean["region"] == region]
        
        print(f"Process Finished! The file was saved as csv in:\n{output_path}\n")

        # save dataframe as csv
        return df_clean.to_csv(output_path, index=False)

    # clean tsv and save it as csv
    clean_data(args.i, args.o, args.r)
    