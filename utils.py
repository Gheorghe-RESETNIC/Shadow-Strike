import json
import fpdf
from datetime import datetime

# Function to store results in JSON
def store_results(results, filename="results.json"):
    with open(filename, "w") as file:
        json.dump(results, file)

# Function to generate PDF report with summary
def generate_report(results, filename="report.pdf"):
    pdf = fpdf.FPDF()
    pdf.add_page()
    
    # Title, target, and date/time
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Pentesting Report", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Target: {results['target']}", ln=True)
    pdf.cell(200, 10, txt=f"Date/Time: {results['date_time']}", ln=True)
    pdf.ln(10)
    
    # Summary of Nmap Results
    pdf.cell(200, 10, txt="Summary of Nmap Results:", ln=True)
    nmap_summary = ", ".join([f"Port {port}: {status}" for port, status in results["nmap"]["open_ports"].items()])
    pdf.multi_cell(0, 10, txt=nmap_summary)
    pdf.ln(10)
    
    # Summary of Nikto Results
    pdf.cell(200, 10, txt="Summary of Nikto Results:", ln=True)
    pdf.multi_cell(0, 10, txt=results["nikto"]["issues_found"])
    pdf.ln(10)
    
    # Summary of Dirb Results
    pdf.cell(200, 10, txt="Summary of Dirb Results:", ln=True)
    pdf.multi_cell(0, 10, txt=results["dirb"]["directories_found"])
    pdf.ln(10)
    
    # Summary of Hydra Results
    pdf.cell(200, 10, txt="Summary of Hydra Results:", ln=True)
    pdf.multi_cell(0, 10, txt=results["hydra"]["issues_found"])
    pdf.ln(10)
    
    # Summary of SQLMap Results
    pdf.cell(200, 10, txt="Summary of SQLMap Results:", ln=True)
    pdf.multi_cell(0, 10, txt=results["sqlmap"])
    
    pdf.output(filename)
