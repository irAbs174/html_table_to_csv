import sys
from bs4 import BeautifulSoup
import csv

def html_table_to_csv(input_file, output_file):
    # Read HTML content from input file
    with open(input_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    if not table:
        print("Error: No <table> tag found in the HTML document.", file=sys.stderr)
        sys.exit(1)

    # Extract rows
    rows = table.find_all('tr')

    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            # Extract all header and data cells
            cells = row.find_all(['th', 'td'])
            # Clean text and create row data
            row_data = [cell.get_text(strip=True) for cell in cells]
            writer.writerow(row_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.html> <output.csv>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    html_table_to_csv(input_file, output_file)
    print(f"Successfully converted {input_file} to {output_file}")