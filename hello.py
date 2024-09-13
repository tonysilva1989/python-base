#!/usr/bin/env python3
"""Hello World Multi Languages

    Depending on what language is configured, this program will
    display a different language in its output.

    Usage:
        Make sure the LANG variable is set. Ex:
            export LANG=pt_BR

    Execution:
        python3 hello.py
        or
        ./hello.py
"""

import os
print('tony'.upper())

__version__="0.0.1"
__author__="Tony Silva"
__license__="Unlicensed"

msg="Hello, World!"

current_language= os.getenv("LANG","en_US")

if current_language == "pt_BR":
    msg="Olá, Mundo!"
if current_language == "en_US":
    msg="Hello, World!"
if current_language == "es_SP":
    msg="Hola, Mundo!"
if current_language == "fr_FR":
    msg="Bonjour Monde!"

print(msg)