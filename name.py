##########################################################################
# The file contains code that will be used to generate the name of the file.
##########################################################################

from datetime import datetime
from typing import Tuple
from dataclasses import dataclass


def get_date_time() -> Tuple[str, str]:
    """
    Function extracts date and time in string format by using inbuilt datetime module.
    """
    formatted_date: str = datetime.today().strftime("%Y%m%d %H%M%S")
    return tuple(formatted_date.split(" "))


@dataclass
class Tags:
    """
    Class for capturing the tag information.
    default location: location for capturing all the tags

    """
