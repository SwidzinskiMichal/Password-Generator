# Password Generator
- Function generates a password comprised of random characters (excluding unicode characters).
## Description
- Function produces a password comrpised of random characters (excluding unicode characters) of no less than 8 and no more than 32 characters.\
Password is generated based on chosen charsets (lower and upper case letters, digits and punctuation signs). Password can not be generated without chosing at least one charset. The main program imports the test_generate_password.py and exceptions.py.
## Getting Started
### Setup
This project is using Makefile. To see all available commands run:
```
make

help                           Shows a list of commands with short descriptions
install                        Installs project requirements
setup                          Setup project
start                          Starts Flask server
test                           Run tests
```
### Dependencies
- Python 3.8
- Make 
- Additional requirements in requirements.txt
### Authors
- Michał Świdziński