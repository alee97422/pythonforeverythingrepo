import subprocess
import argparse

def convert_odg_to_pdf(input_file, output_file):
    try:
        subprocess.check_call(["unoconv", "-f", "pdf", "-o", output_file, input_file])
        print(f"{input_file} was successfully converted to {output_file}")
    except subprocess.CalledProcessError:
        print(f"Failed to convert {input_file} to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert ODG files to PDF")
    parser.add_argument("input", help="Path to the input .odg file")
    parser.add_argument("output", help="Path to the output .pdf file")

    args = parser.parse_args()
    convert_odg_to_pdf(args.input, args.output)
