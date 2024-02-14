"""Region Enum Definition"""

from enum import Enum
from typing import List


class Region(Enum):
    """
    Enum class that specifies all possible regions that can be found in
    raw life expectancy tsv file.
    """
    AT = 'AT'
    FI = 'FI'
    ES = 'ES'
    EL = 'EL'
    EE = 'EE'
    DK = 'DK'
    DE = 'DE'
    CZ = 'CZ'
    CY = 'CY'
    CH = 'CH'
    BG = 'BG'
    BE = 'BE'
    FX = 'FX'
    SK = 'SK'
    SI = 'SI'
    SE = 'SE'
    RO = 'RO'
    PT = 'PT'
    PL = 'PL'
    NO = 'NO'
    NL = 'NL'
    LU = 'LU'
    LT = 'LT'
    IT = 'IT'
    UK = 'UK'
    IS = 'IS'
    HU = 'HU'
    IE = 'IE'
    MT = 'MT'
    MK = 'MK'
    LI = 'LI'
    FR = 'FR'
    RS = 'RS'
    HR = 'HR'
    LV = 'LV'
    UA = 'UA'
    TR = 'TR'
    ME = 'ME'
    AL = 'AL'
    AZ = 'AZ'
    GE = 'GE'
    BY = 'BY'
    AM = 'AM'
    MD = 'MD'
    SM = 'SM'
    RU = 'RU'
    XK = 'XK'
    # invalid countries
    EFTA = 'EFTA'
    EA18 = 'EA18'
    EA19 = 'EA19'
    EU28 = 'EU28'
    EEA31 = 'EEA31'
    DE_TOT = 'DE_TOT'
    EU27_2007 = 'EU27_2007'
    EU27_2020 = 'EU27_2020'
    EEA30_2007 = 'EEA30_2007'

    @classmethod
    def considered_regions(cls) -> List[str]:
        """
        Filters the enum Region Class, to create a list of valid regions to be 
        considered in the analysis. Excludes regions that are included in the 
        'invalid' dictionary.

        :param cls: Enum Region class.
        :return List: List of valid regions to be considered.
        """
        # List of invalid regions
        invalid = [
            cls.EFTA,
            cls.EA18,
            cls.EA19,
            cls.EU28,
            cls.EEA31,
            cls.DE_TOT,
            cls.EU27_2007,
            cls.EU27_2020,
            cls.EEA30_2007
        ]

        # List of valid regions
        valid = [region.value for region in cls if region not in invalid]

        return valid
