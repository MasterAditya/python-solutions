#!/bin/bash

URL="https://www.amfiindia.com/spages/NAVAll.txt"
OUTPUT_FILE="nav_data.tsv"

curl -s "$URL" | \
awk -F ';' '
    BEGIN {
        OFS = "\t";
        print "Scheme Name", "Net Asset Value";
    }
    NF > 1 && $1 != "Scheme Code" {
        print $4, $5;
    }
' > "$OUTPUT_FILE"

echo "✅ Extracted NAV data saved to $OUTPUT_FILE"
