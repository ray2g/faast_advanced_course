from random import sample
from pathlib import Path
from typing import Union

from . import OUTPUT_DIR, FIXTURES_DIR

i_path: Path = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
o_path: Path = FIXTURES_DIR / "eu_life_expectancy_subset.tsv"


def gen_data_subset(i_path: Union[str,Path], region: str, sub_freq:int, o_path: Union[str,Path]) -> None:
    """
    Generates a data subset, verifing that an instance for a
    specific region exists.

    param: Input file path.
    param: Region filter.
    """
    # read file
    with open (i_path, "r") as data:
        rows = data.readlines()

    header = rows[0]
    instances = rows[1:]

    # subset rows with at least a desire region
    found_region = False
    while found_region == False:
        rows_subset = sample(instances, int(sub_freq))
        found_region = any(region in row for row in rows_subset)

    # write data subset
    with open(o_path, "w") as data_subset:
        data_subset.write(header)
        for row in rows_subset:
            data_subset.write(row)

def main():
    gen_data_subset(
        i_path = i_path,
        region = "PT",
        sub_freq = 33,
        o_path = o_path
    )

if __name__ == "__main__":
    main()