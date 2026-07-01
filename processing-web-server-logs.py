import collections
import os

#Variables 
old_log_file = "test.test.log"
new_log_file = "testresult.nginx.log"

#The function as a generator extracts IP addresses without storing the temporary variable with this data in RAM and saving memory
def extract_ip(old_log_file):
    with open(old_log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield line.split()[0]

#The function extracts the data from the dictionary and writes the data in the needed format to a file 
def write_to_file(new_log_file, sorted_ip_list):
    with open(new_log_file, 'w+', encoding='utf-8') as f:
        for ip, count in sorted_ip_list.items():
           output_line = f"{ip}: {count}\n"
           f.write(output_line)
            
# The function creates the dictionary that stores IP addressess and their number of request
def count_ip(group_ip):
    ip_list = collections.Counter(group_ip)
    sorted_ip_list = dict(sorted(ip_list.items(), key=lambda item: item[1], reverse=True))
    write_to_file(new_log_file, sorted_ip_list)

# Call the function to extract IP addresses from the log file and count their occurrences
if os.path.exists(old_log_file):
    group_ip = extract_ip(old_log_file)
else:
    print(f"File {old_log_file} does not exist.")
    exit(1)

count_ip(group_ip)
