import re
import sys

def parse_r_script(file_path):
    csv_files = []
    libraries = []
    outputs = []

    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # Check for CSV file reads
            if 'read.csv' in line or 'read_csv' in line:
                match = re.search(r'"(.*?)"', line)
                if match:
                    csv_files.append(match.group(1))

            # Check for library imports
            if 'library' in line or 'require' in line:
                match = re.search(r'\((.*?)\)', line)
                if match:
                    libraries.append(match.group(1))

            # Check for output files/images
            if 'write.csv' in line or 'write_csv' in line or 'ggsave' in line or 'save' in line:
                match = re.search(r'"(.*?)"', line)
                if match:
                    outputs.append(match.group(1))

    return {'csv_files': csv_files, 'libraries': libraries, 'outputs': outputs}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the R script as the first argument.")
        sys.exit(1)

    r_script_path = sys.argv[1]
    r_script_info = parse_r_script(r_script_path)
    print(r_script_info)
