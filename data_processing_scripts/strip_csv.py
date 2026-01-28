import argparse
import csv
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                prog='strip_csv.py',
                description="Given a csv file, strip out lines where columns named 'logic' don't change from the previous line.")
    parser.add_argument('filepath')
    args = parser.parse_args()
    
    keep_lines = []
    fields = None    
    with open(args.filepath, 'r') as infile:
        reader = csv.DictReader(infile)
        prev_line = None
        for line in reader:
            if prev_line is None:
                prev_line = line
                fields = reader.fieldnames
            else:
                if (prev_line['logic0'] != line['logic0']) or (prev_line['logic1'] != line['logic1']):
                    keep_lines.append(line)
            prev_line = line
    
    with open(args.filepath.replace('.csv', '_stripped.csv'), 'w') as outfile:
        writer = csv.DictWriter(outfile, fields)
        writer.writeheader()
        writer.writerows(keep_lines)

