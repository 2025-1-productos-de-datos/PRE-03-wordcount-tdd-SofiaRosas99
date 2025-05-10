import argparse


def parse_args():

    parser = argparse.ArgumentParser(description="Word Count Script")
    parser.add_argument(
        "input_folder", help="Path to the input folder containing text files"
    )
    parser.add_argument(
        "output_folder", help="Path to the output folder where results will be saved"
    )
    parsed_args = parser.parse_args()

    return parsed_args.input_folder, parsed_args.output_folder
