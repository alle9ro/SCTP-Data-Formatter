# SCTP Data Formatter for Wireshark

## Overview

The `SCTP Data Formatter for Wireshark` is a Python script designed to extract and format SCTP (Stream Control Transmission Protocol) data from CSV and JSON files. This tool simplifies the process of converting raw SCTP data into a format that is compatible with Wireshark, a popular network packet analysis tool. The script is particularly useful for network security professionals and analysts who need to analyze SCTP traffic in a readable and structured manner.

## Purpose

Wireshark is a powerful tool for inspecting network traffic, but it requires data to be in specific formats for effective analysis. SCTP is a transport-layer protocol that is increasingly used in telecoms and other critical applications. Analyzing SCTP data can be crucial for network troubleshooting, performance monitoring, and security analysis.

This script automates the extraction of SCTP payload data from logs or records stored in CSV or JSON formats, commonly used in data collection and logging systems. It then formats this data into a hexadecimal representation that Wireshark can readily interpret, making the process of importing and analyzing SCTP traffic in Wireshark more straightforward and efficient.

## Features

- **CSV and JSON Support:** Handles both CSV and JSON files, making it versatile for various data sources.
- **Hexadecimal Formatting:** Converts SCTP payloads into a hex format that aligns with Wireshark’s requirements, ensuring seamless import and analysis.
- **Automation:** Eliminates the need for manual formatting, reducing the potential for errors and saving time for network analysts.

## Why You Need This Script

Analyzing SCTP traffic is essential in several network security and operational scenarios:
- **Security Monitoring:** Identifying and investigating suspicious SCTP traffic can help detect potential network threats.
- **Performance Analysis:** Understanding SCTP flow can provide insights into network performance issues.
- **Protocol Compliance:** Ensuring that SCTP implementation adheres to standards and behaves as expected.

By converting raw SCTP data into a Wireshark-compatible format, this script aids in deep packet inspection, helping security analysts to uncover vulnerabilities, troubleshoot issues, and ensure the security and reliability of network systems.

## How It Works

1. **Input Selection:** Choose whether to process a single CSV file or a folder containing JSON files.
2. **Data Extraction:** The script extracts the SCTP payload data from the specified file(s).
3. **Data Formatting:** The extracted data is formatted into a hexadecimal string, structured in a way that Wireshark can easily interpret.
4. **Output:** The formatted data is saved to a text file, ready for import into Wireshark.

## Usage Instructions

1. Clone this repository to your local machine.
2. Install any necessary dependencies using `pip install -r requirements.txt`.
3. Run the script using `python sctp_formatter.py`.
4. Follow the on-screen prompts to select your input files and generate the formatted output.

## Example

To format SCTP data from a CSV file:
```sh
python sctp_formatter.py
# Follow the prompt and enter '1' for CSV input
# Provide the path to your CSV file
