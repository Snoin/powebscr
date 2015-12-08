#!/bin/bash
cd "$( dirname ${BASH_SOURCE[0]})"

unzip ./powebscr/legacy/phantomjs.zip -d ./powebscr/legacy/
sudo ./powebscr/legacy/install_libicu52.sh
pip install -e .[legacy]
