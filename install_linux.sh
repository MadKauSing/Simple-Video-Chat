#!/bin/bash
sudo apt install python3

python3 -m pip install --user --upgrade pip
python3 -m pip --version
python3 -m pip install --user virtualenv
python3 -m venv env

source env/bin/activate
which python


python3 -m pip install requests
python3 -m pip install pyfiglet
python3 -m pip install opencv-python
python3 -m pip install pytest-socket
python3 -m pip install PyAudio

