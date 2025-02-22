'''
The file contains code that will be used to generate the name of the file.
'''

from datetime import datetime
from typing import Tuple

def extract_date() -> Tuple[str, str]:
    '''
    Function extracts date and time by using inbuilt datetime module.
    '''
    formatted_date: str = datetime.today().strftime('%Y%m%d %H%M%S')
    return tuple(formatted_date.split(" "))

print(extract_date())