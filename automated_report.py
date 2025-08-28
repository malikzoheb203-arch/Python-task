import csv
from fpdf import FPDF

# Read data from a CSV file
def read_csv_data(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Analyze the data
def analyze_data(data):
    scores = [int(d["Score"]) for d in data]
    average = sum(scores) / len(scores)
    highest = max(data, key=lambda x: int(x["Score"]))
    lowest = min(data, key=lambda x: int(x["Score"]))
    return average, highest, lowest

# Generate a PDF report
def generate_pdf(data, average, highest, lowest, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Automated Report Generation", ln=True, align="C")
    pdf.ln(10)

    # Table header
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, "Name", border=1)
    pdf.cell(40, 10, "Score", border=1)
    pdf.ln()

    # Table data
    pdf.set_font("Arial", '', 12)
    for row in data:
        pdf.cell(60, 10, row["Name"], border=1)
        pdf.cell(40, 10, row["Score"], border=1)
        pdf.ln()

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Average Score: {average:.2f}", ln=True)
    pdf.cell(0, 10, f"Highest Score: {highest['Name']} - {highest['Score']}", ln=True)
    pdf.cell(0, 10, f"Lowest Score: {lowest['Name']} - {lowest['Score']}", ln=True)

    pdf.output(filename)
    print(f"PDF report generated: {filename}")

# Main function
def main():
    data = read_csv_data("data.csv")
    average, highest, lowest = analyze_data(data)
    generate_pdf(data, average, highest, lowest)

if __name__ == "__main__":
    main()
