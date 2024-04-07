import os
import subprocess

# Specify the path to the trace directory and the executable file
trace_dir = '/media/ext_hdd/traces/spec2k17'
exec_file = '../../bin/perceptron-no-no-no-ship-1core'

# Get a list of all cases in the trace directory
cases = os.listdir(trace_dir)

# Calculate the total number of cases for progress tracking
total_cases = len(cases)
completed_cases = 0

# Ensure the output directory exists
output_dir = './output'
os.makedirs(output_dir, exist_ok=True)

# Iterate over all cases
for case in cases:
    # Construct the full path to the trace
    trace_path = os.path.join(trace_dir, case)
    # Construct the path for the output file
    output_path = os.path.join(output_dir, case + '.txt')
    # Construct the command to execute
    command = f'{exec_file} --warmup_instructions=1000000 --simulation_instructions=1000000 --cxl_latency=0 -traces {trace_path}'
    
    # Execute the command and redirect output to the file
    with open(output_path, 'w') as output_file:
        subprocess.run(command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

    # Update and print the progress
    completed_cases += 1
    progress = (completed_cases / total_cases) * 100
    print(f'Case {case} completed, output file located at {output_path}')
    print(f'Progress: {completed_cases}/{total_cases} ({progress:.2f}%)')

print('All cases have been processed.')
