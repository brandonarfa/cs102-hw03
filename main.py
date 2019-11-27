import sys
from statistics import mean

def isFloat(string):
    try: 
        float(string)
        return True
    except ValueError: 
        return False 



def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    # TODO: Fill in the actual logic here!

    f = open(input_file_path, "r")
    values = f.read()
    values = values.split("\n")

    for val in values:
        strvals = val.split(",")
        numvals = []
        for nv in strvals:
            if isFloat(nv):
                numvals.append(float(nv))
        if numvals != []:
            print(mean(numvals))


if __name__ == "__main__":
    main()