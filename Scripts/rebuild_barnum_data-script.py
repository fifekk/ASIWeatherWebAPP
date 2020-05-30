#!P:\WebDev\Django\ASIWeatherWebApp\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'barnum==0.5.1','console_scripts','rebuild_barnum_data'
__requires__ = 'barnum==0.5.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('barnum==0.5.1', 'console_scripts', 'rebuild_barnum_data')()
    )
