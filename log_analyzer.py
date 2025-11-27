import re
import csv
from collections import Counter

def analyze_logs(log_file):
    error_patterns = []
    error_count = 0
    
    # 1. Open the file (Simulating reading a production log)
    with open(log_file, 'r') as file:
        for line in file:
            # 2. Use Regex to find ERROR or CRITICAL lines
            if re.search(r'(ERROR|CRITICAL)', line):
                error_count += 1
                # Extract the actual message after the timestamp/level
                match = re.search(r'\d{2}:\d{2}:\d{2}\s(ERROR|CRITICAL):\s(.*)', line)
                if match:
                    error_patterns.append(match.group(2))

    # 3. Aggregate the data
    most_common_errors = Counter(error_patterns).most_common()

    print(f"--- Analysis Complete ---")
    print(f"Total Critical Issues Found: {error_count}")
    print("Top Error Patterns:")
    for error, count in most_common_errors:
        print(f"[{count}x] {error}")

    # 4. Generate a Report
    with open('incident_report.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Error Message', 'Frequency'])
        writer.writerows(most_common_errors)
        print("\nReport saved to incident_report.csv")

if __name__ == "__main__":
    analyze_logs('server.log')
