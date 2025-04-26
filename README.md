# 📊 CSV Data Processor

A simple command-line tool for processing, analyzing, and transforming CSV data files.

## ✨ Features

- 📋 Read and write CSV files with custom delimiters
- 🔍 Filter rows based on column values
- 🔀 Sort data by any column
- 📈 Count value occurrences in columns
- ✂️ Select and extract specific columns
- 📊 Display data in a readable tabular format

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/csv-processor.git
cd csv-processor
```

2. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x main.py
```

## 🔍 Usage

```bash
python main.py <input_file.csv> [options]
```

## ⚙️ Options

- `input`: Input CSV file (required)
- `-o, --output`: Output CSV file
- `-d, --delimiter`: CSV delimiter (default: ,)
- `--filter COLUMN VALUE`: Filter rows where COLUMN equals VALUE
- `--sort COLUMN`: Sort by column
- `--reverse`: Reverse sort order
- `--count COLUMN`: Count values in a column
- `--select COLUMNS`: Select only specified columns (comma-separated)
- `--limit N`: Limit output rows displayed


