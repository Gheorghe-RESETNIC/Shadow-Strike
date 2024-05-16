import argparse
from datetime import datetime
from audit import perform_audit
from exploit import hydra_attack, sqlmap_exploit
from utils import store_results, generate_report

def main():
    parser = argparse.ArgumentParser(description="Shadow Strike - Pentesting Suite")
    parser.add_argument("-t", "--target", required=True, help="The target for the pentesting suite")
    args = parser.parse_args()

    current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    results = {
        "target": args.target,
        "date_time": current_datetime,
        "nmap": {},
        "nikto": {},
        "dirb": {},
        "hydra": {},
        "sqlmap": {}
    }

    while True:
        print("\nMain Menu:")
        print("1. Audit")
        print("2. Exploit")
        print("3. Generate Report")
        print("4. Help")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            results.update(perform_audit(args.target))
        elif choice == "2":
            print("Choose exploit:")
            print("1. Hydra")
            print("2. SQLMap")
            exploit_choice = input("Select an option: ")
            if exploit_choice == "1":
                username = input("Enter username: ")
                password_list = input("Enter path to wordlist: ")
                results["hydra"] = hydra_attack(args.target, username, password_list)
            elif exploit_choice == "2":
                results["sqlmap"] = sqlmap_exploit(args.target)
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice == "3":
            if not results["nmap"]:
                print("Please perform an audit first before generating the report.")
            else:
                store_results(results)
                generate_report(results)
                print("Report generated successfully.")
        elif choice == "4":
            print("Help menu:")
            print("1. Audit: Perform an audit including Nmap, Nikto, and Dirb scans.")
            print("2. Exploit: Launch exploits against the target.")
            print("3. Generate Report: Generate a report based on the audit and exploit results.")
            print("4. Help: Display this help message.")
            print("5. Quit: Exit the program.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
