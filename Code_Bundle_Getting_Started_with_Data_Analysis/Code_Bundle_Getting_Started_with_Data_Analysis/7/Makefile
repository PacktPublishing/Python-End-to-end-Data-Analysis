SHELL = /bin/bash

all: rbrted_cleaned.csv sunshine.tsv

rbrted_cleaned.csv: rbrted.csv
	python clean_rbrted.py

clean:
	rm -f rbrted_cleaned.csv sunshine.tsv

sunshine.tsv:
	python makedata.py > sunshine.tsv
