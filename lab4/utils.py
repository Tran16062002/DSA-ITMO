def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

        lines = [line.strip() for line in lines]
        return lines

def write_file(file_path, result):
    with open(file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(result)