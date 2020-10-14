# Install dev environment

## Install wxPython

Command prompt
pip3 install wxpython

See https://stackoverflow.com/questions/32284938/how-to-properly-install-wxpython 
Install python 3xxx in your system opting (Add 3xxx to your path).
open python CLI to see whether python is working or not.
then open command prompt (CMD).
type PIP to see whether pip is installed or not.
enter command : pip install wheel
enter command : pip install pygame
To install wxpython enter command : pip install -U wxPython

## Install OpenPyXl - for accessing Excel spreadsheets

Version 3.0.4 has a bug so use specific version 3.0.3
pip3 -Iv openpyxl==3.0.3

## Install wxGlade

1. Download Zip from Source forge
2. Change Python interpreter in VS Code status bar. Python 3.9.0 x64 doesn't seem to work. python 3.8.5 x32 works
