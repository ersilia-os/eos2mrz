import sys
import csv
import deepsmiles

input_file = sys.argv[1]
output_file = sys.argv[2]
converter = deepsmiles.Converter(rings=True, branches=True)

smiles_list = []
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles_list += [r[0]]

deepsmiles_list = []
for smi in smiles_list:
    deepsmiles_list += [converter.encode(smi)]

with open(output_file, "w") as f:
    writer = csv.writer(f, delimiter= " ")
    writer.writerow(["deepsmiles"])
    for deepsmiles in deepsmiles_list:
        writer.writerow([deepsmiles])