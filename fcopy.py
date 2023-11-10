import sys

def fcopy(input, output):
    input_file = open(input, 'r')
    output_file = open(output, 'w')
    for l in input_file: 
        output_file.write(l + "\n")
    input_file.close()
    
def main():
    print("Input file: ", sys.argv[0])
    print("\nOutput file: ", sys.argv[1])
    fcopy(sys.argv[0], sys.argv[1])
    
