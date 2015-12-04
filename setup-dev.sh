#!/bin/bash
cd "$( dirname ${BASH_SOURCE[0]})"

echo "install pre-commit hook (forced)"
ln -sf ../../hooks/pre-commit .git/hooks/pre-commit
echo

echo "setup basic environ for develop in python"
pip install -e .[tests]
echo

echo "test the pre-commit hook"
exec .git/hooks/pre-commit
