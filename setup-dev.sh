#!/bin/bash
cd "$( dirname ${BASH_SOURCE[0]})"

./powebscor/legacy/install_libicu52.sh
pip install -e .[legacy]
