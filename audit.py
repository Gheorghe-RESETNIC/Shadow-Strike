import subprocess

# Function to execute Nmap
def nmap_scan(target):
    result = subprocess.run(["nmap", "-p-", "-T4", "-oG", "-", target], capture_output=True, text=True)
    open_ports = {line.split("/")[0]: line.split()[4] for line in result.stdout.splitlines() if "/open" in line}
    return {"open_ports": open_ports}

# Function to execute Nikto
def nikto_scan(target):
    result = subprocess.run(["nikto", "-h", target], capture_output=True, text=True)
    issues_found = result.stdout
    return {"issues_found": issues_found}

# Function to execute Dirb
def dirb_scan(target):
    result = subprocess.run(["dirb", target], capture_output=True, text=True)
    directories_found = result.stdout
    return {"directories_found": directories_found}

# Function to perform audit
def perform_audit(target):
    audit_results = {}
    audit_results["nmap"] = nmap_scan(target)
    audit_results["nikto"] = nikto_scan(target)
    audit_results["dirb"] = dirb_scan(target)
    return audit_results
