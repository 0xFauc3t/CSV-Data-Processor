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

## 📝 Examples

### Display CSV data:
```bash
python main.py data.csv
```

### Filter rows by column value:
```bash
python main.py data.csv --filter Country "United States"
```

### Sort data by a column:
```bash
python main.py data.csv --sort Age
```

### Sort in descending order:
```bash
python main.py data.csv --sort Salary --reverse
```

### Count values in a column:
```bash
python main.py data.csv --count Category
```

### Select specific columns:
```bash
python main.py data.csv --select Name,Email,Phone
```

### Save processed data to a new file:
```bash
python main.py data.csv --filter Department IT --sort Salary --reverse -o it_salaries.csv
```

### Work with different delimiter:
```bash
python main.py data.csv -d ";" --output processed.csv
```


