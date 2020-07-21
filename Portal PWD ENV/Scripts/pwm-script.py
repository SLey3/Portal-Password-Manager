#!"C:\Users\ghub4\AppData\Local\Programs\Portal Password Manager\Portal PWD ENV\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'passwordmeter==0.1.8','console_scripts','pwm'
__requires__ = 'passwordmeter==0.1.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('passwordmeter==0.1.8', 'console_scripts', 'pwm')()
    )
