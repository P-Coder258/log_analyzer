# Automated Log Analysis & Incident Reporting Tool

A Python automation script designed to streamline root cause analysis by parsing large-scale server logs. This tool utilizes Regular Expressions (Regex) to extract critical failure patterns and generates automated CSV reports for stakeholder review.

Built to demonstrate how scripting can reduce Mean Time to Resolution (MTTR) by instantly aggregating error frequency and identifying top failure modes.

## Key Features
- Regex Pattern Matching: Efficiently parses unstructured text logs to isolate ERROR and CRITICAL incidents.
- Automated Reporting: Exports analysis results to a structured CSV file (incident_report.csv) for documentation and ticket attachment.
- Frequency Analysis: Aggregates error counts to identify the most recurring issues (e.g., Database Timeouts vs. Memory Spikes).
- Root Cause Identification: Extracts specific error messages to provide immediate context for troubleshooting.

## Technical Stack
- Language: Python 3.14.0
- Text Processing: re (Regular Expressions) module.
- Data Handling: collections.Counter for statistical aggregation.
- Output: csv module for report generation.
