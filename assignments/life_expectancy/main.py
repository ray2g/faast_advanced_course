"""Main Module"""

# import libraries
import argparse

from load_data import load_data
from cleaning import clean_data
from save_data import save_data
from regions import Region
from context import Context, ConcreteTsvStrategy, ConcreteJsonStrategy

def main(i_path, region, o_path): # pragma: no cover
    """
    Main function which selects the appropriated Strategy based
    on the input file type, and runs the data workflow processment.
    """
    
    # Select Strategy based on file type
    if i_path.lower().endswith('.zip'):
        context = Context(ConcreteJsonStrategy())
    else:
        context = Context(ConcreteTsvStrategy())

    # Run data processment
    context.data_workflow(i_path, region, o_path)

if __name__ == "__main__":  # pragma: no cover

    # config argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help= "Input file path.", required=True) 
    parser.add_argument('-o', help = "Output file path.", required=True)
    parser.add_argument('-r',  type = Region, choices = Region, \
                        default= Region.PT, help = "Desire region to filter the csv.")
    args = parser.parse_args()
        
    main(args.i, args.r, args.o)
