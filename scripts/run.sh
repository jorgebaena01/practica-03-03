#!/bin/bash


echo "se comienza el procesooooooooo"





python3 src/ingest.py
python3 src/transform.py
python3 src/plot.py




