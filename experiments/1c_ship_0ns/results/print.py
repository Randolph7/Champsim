import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Process an xlsx file.')
parser.add_argument('filepath', metavar='F', type=str, help='a path to an xlsx file')

args = parser.parse_args()

data = pd.read_excel(args.filepath)

print(data)

