import os
import re
from openpyxl import Workbook

# Specify the path to the output folder
output_dir = '../output'

# Create a new Excel workbook and a worksheet
wb = Workbook()
ws = wb.active
ws.title = 'Statistics'
ws.append(['Filename', 'Core_0_IPC', 'Core_0_LLC_total_access', 'Core_0_LLC_total_hit', 'Core_0_LLC_average_miss_latency'])

# Regular expression patterns for matching
ipc_pattern = re.compile(r'Core_0_IPC (\d+\.\d+)')
llc_total_access_pattern = re.compile(r'Core_0_LLC_total_access (\d+)')
llc_total_hit_pattern = re.compile(r'Core_0_LLC_total_hit (\d+)')
llc_avg_miss_latency_pattern = re.compile(r'Core_0_LLC_average_miss_latency (\d+\.\d+)')

# Iterate through all files in the output directory
for filename in os.listdir(output_dir):
    filepath = os.path.join(output_dir, filename)
    ipc_value = None
    llc_total_access_value = None
    llc_total_hit_value = None
    llc_avg_miss_latency_value = None

    with open(filepath, 'r') as file:
        content = file.read()

        # Find IPC stat
        ipc_match = ipc_pattern.search(content)
        if ipc_match:
            ipc_value = ipc_match.group(1)

        # Find LLC stats
        llc_total_access_match = llc_total_access_pattern.search(content)
        if llc_total_access_match:
            llc_total_access_value = llc_total_access_match.group(1)

        llc_total_hit_match = llc_total_hit_pattern.search(content)
        if llc_total_hit_match:
            llc_total_hit_value = llc_total_hit_match.group(1)

        llc_avg_miss_latency_match = llc_avg_miss_latency_pattern.search(content)
        if llc_avg_miss_latency_match:
            llc_avg_miss_latency_value = llc_avg_miss_latency_match.group(1)

        # Append the values to the worksheet
        ws.append([filename, ipc_value, llc_total_access_value, llc_total_hit_value, llc_avg_miss_latency_value])

# Save the workbook
wb.save('statistics.xlsx')

print('IPC and LLC values have been successfully extracted to combined_statistics.xlsx')
