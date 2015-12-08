#!/bin/bash
cd "$( dirname ${BASH_SOURCE[0]})"

./powebscr/legacy/install_libicu52.sh
pip install -e .[legacy]