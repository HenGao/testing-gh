import sys

def fcopy(input, output):
    input_file = open(input, 'r')
    output_file = open(output, 'w')
    for l in input_file: 
        output_file.write(l)
    input_file.close()
    output_file.close()
    
def main():
    fcopy(sys.argv[1], sys.argv[2])
    
main()
