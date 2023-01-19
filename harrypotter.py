import csv
import sys
import pathlib

if len(sys.argv) < 3:
    print("To few command-line arguments")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()
elif len(sys.argv) == 3:
   
    _ , input_file, output_file = sys.argv 
    if not pathlib.Path(input_file).exists():
        print("This file does not exist")
        sys.exit()
    

with open(input_file, "r") as in_file:
    
    with open(output_file, "w", newline="") as out_file:

        reader = csv.reader(in_file)
        writer = csv.writer(out_file)

        # write headers to the output file
        writer.writerow(["first", "last", "house"])

        # skips first row in input file(header)
        next(reader)
        for row in reader:
            name, house = row 
            last, first = name.split(", ")
            
            writer.writerow([first, last, house])
