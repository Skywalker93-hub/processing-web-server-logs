# Web Server Log Processing

## Overview
This project contains a Python script that processes a large Nginx web server log file and generates a report with the number of requests made by each IP address.

The script reads the log file line by line using a generator (yield), which allows processing large files without loading the entire file into memory.

## Features
1. Reads large log files efficiently.
2. Uses a generator to minimize memory usage.
3. Counts the number of requests for each IP address.
4. Saves the results to a text file in the following format:
   
128.148.46.126: 15
52.56.245.28: 8
122.100.81.4: 3

## Implementation

The script consists of three functions:

- **extract_ip()** – extracts IP addresses from the log file using a generator.
- **count_ip()** – counts the number of requests for each IP address.
- **write_to_file()** – writes the statistics to the output file.

## Usage

Run the script:

**python3 processing-web-server-logs.py**

The script reads data from:

**your log file**

and writes the processed statistics to:

**result of log**
