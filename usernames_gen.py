"""
Code of application that processes input files, generates usernames and then exports
processed data to one output file.

"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="This is HELP information: To process all input files and generate data "
    "into one output file you need to type following to the command line: "
    "python3 usernames_gen.py -i input_file1 input_file2 ... -o output_file")
    parser.add_argument('-i', '--input', nargs="+", type=argparse.FileType('r'), required=True, help="Input file")
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), required=True, help="Output file")
    args = parser.parse_args()


    for input_file in args.input:
        process_file(input_file, args.output)

def process_file(input_file, output_file):


    for line in input_file:
        splitted_values = line.split(":")
        
        if splitted_values[-1].endswith("\n") == False:
            value_with_n = splitted_values[-1] + "\n"
            splitted_values.pop()
            splitted_values.append(value_with_n)
        else:
            pass
            
        if splitted_values[2] == '':
            user_name = splitted_values[1][0].casefold() + splitted_values[-2].casefold()
        else:
            user_name = splitted_values[1][0].casefold() + splitted_values[2][0].casefold() + splitted_values[-2].casefold()

        sliced_user_name = user_name[0:8]

        if len(user_name) > 8:
            splitted_values.insert(1, sliced_user_name)
        else:
            splitted_values.insert(1, user_name)       
        
        modified_list = list()
        modified_list.append(splitted_values)

        for item in modified_list:
            agreggated_values = ":".join(item)

        output_file.write(agreggated_values)


if __name__ == "__main__":
    main()

