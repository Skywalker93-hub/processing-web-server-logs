#Variables 
old_log_file = "nginx.log"
new_log_file = "result.nginx.log"

#The function as a generator extracts IP addresses without storing the temporary variable with this data in RAM and saving memory
def extract_ip(old_log_file):
    with open(old_log_file, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.split()[0] 

#The function extracts the data from the dictionary and writes the data in the needed format to a file 
def write_to_file(new_log_file, ip_list):
    with open(new_log_file, 'w+', encoding='utf-8') as f:
        for x0, x1 in ip_list.items():
           output_line = f"{x0}: {x1}\n"
           f.write(output_line)
            
#The function creates the dictionary that stores IP addressess and their number of request
def count_ip(group_ip):
    ip_list = {}
    for ip in group_ip:
        if ip in ip_list:
            ip_list[ip] += 1
        else:
            ip_list[ip] = 1
    write_to_file(new_log_file, ip_list)

group_ip = extract_ip(old_log_file)
count_ip(group_ip)
