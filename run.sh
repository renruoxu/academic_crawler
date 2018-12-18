#!/bin/bash
set -e
rm -f data/result.json
echo "Removed data file"
pip install -r requirement.txt
echo "Installed dependencies"

# crawl data
python main.py
