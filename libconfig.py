import subprocess
import sys
import os

PS1_SCRIPT_DIR = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\pathconfig.ps1'
script = subprocess.Popen(
      ["powershell.exe", PS1_SCRIPT_DIR],
      stdout=sys.stdout
  )
script.communicate()
