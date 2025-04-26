#!/usr/bin/env python3

import argparse
import csv
import sys
import os
from collections import defaultdict

def read_csv(file_path, delimiter=','):
    """Read a CSV file and return its contents as a list of dictionaries"""
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            return list(reader)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def write_csv(file_path, data, fieldnames=None, delimiter=','):
    """Write data to a CSV file"""
    try:
        if not fieldnames and data:
            fieldnames = data[0].keys()
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        return False

def filter_data(data, column, value):
    """Filter data based on a column value"""
    return [row for row in data if row.get(column) == value]

def sort_data(data, column, reverse=False):
    """Sort data based on a column"""
    return sorted(data, key=lambda x: x.get(column, ''), reverse=reverse)

def count_values(data, column):
    """Count occurrences of values in a specific column"""
    counter = defaultdict(int)
    for row in data:
        value = row.get(column, '')
        counter[value] += 1
    return counter

def select_columns(data, columns):
    """Select only specified columns from the data"""
    return [{col: row.get(col, '') for col in columns} for row in data]

def display_data(data, limit=None):
    """Display data in a tabular format"""
    if not data:
        print("No data to display")
        return
    
    # Get column widths
    columns = data[0].keys()
    col_widths = {col: max(len(col), max(len(str(row.get(col, ''))) for row in data)) for col in columns}
    
    # Print header
    header = ' | '.join(f"{col:{col_widths[col]}}" for col in columns)
    print(header)
    print('-' * len(header))
    
    # Print rows
    for i, row in enumerate(data):
        if limit and i >= limit:
            print(f"\n... and {len(data) - limit} more rows")
            break
        print(' | '.join(f"{str(row.get(col, '')):{col_widths[col]}}" for col in columns))

def main():
    parser = argparse.ArgumentParser(description="Process CSV data files")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("-o", "--output", help="Output CSV file")
    parser.add_argument("-d", "--delimiter", default=',', help="CSV delimiter (default: ,)")
    
    # Data processing options
    parser.add_argument("--filter", nargs=2, metavar=('COLUMN', 'VALUE'), help="Filter rows where COLUMN equals VALUE")
    parser.add_argument("--sort", help="Sort by column")
    parser.add_argument("--reverse", action="store_true", help="Reverse sort order")
    parser.add_argument("--count", help="Count values in a column")
    parser.add_argument("--select", help="Select only specified columns (comma-separated)")
    parser.add_argument("--limit", type=int, help="Limit output rows")
    
    args = parser.parse_args()
    
    # Read input CSV
    data = read_csv(args.input, args.delimiter)
    if not data:
        sys.exit(1)
    
    # Process data
    if args.filter:
        column, value = args.filter
        data = filter_data(data, column, value)
    
    if args.select:
        columns = [col.strip() for col in args.select.split(',')]
        data = select_columns(data, columns)
    
    if args.sort:
        data = sort_data(data, args.sort, args.reverse)
    
    if args.count:
        count_result = count_values(data, args.count)
        print(f"\nValue counts for column '{args.count}':")
        for value, count in sorted(count_result.items(), key=lambda x: x[1], reverse=True):
            print(f"  {value}: {count}")
    
    # Output results
    if args.output:
        if write_csv(args.output, data, delimiter=args.delimiter):
            print(f"Data written to {args.output}")
    else:
        # Display data
        print(f"\nData from {args.input}:")
        display_data(data, args.limit)
    
    print(f"\nTotal rows: {len(data)}")

if __name__ == "__main__":
    main()
