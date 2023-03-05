""" ---------------------------------------------------------------------------
       File: convert.py
     Author: Rodrigo Bento
Description: Attempts extracting tables from well-formed PDF files to a CSV.
--------------------------------------------------------------------------  """

import os
import sys
import tabula


CSV = "csv"


def replace_extension(source_file, extension = CSV):
    return (source_file.rsplit(".", maxsplit=1)[0]) + "." + extension


def is_pdf(source_file):
    return source_file.lower().endswith(".pdf") and os.path.isfile(source_file)


def pdf_to_csv(source_file):
    print("Converting", source_file)
    destination_file = replace_extension(source_file)
    tabula.convert_into(source_file, destination_file, pages = "all", output_format = CSV);
    print("> Converted to", destination_file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for source_file in sys.argv[1:]:
            if is_pdf(source_file):
                pdf_to_csv(source_file)
            else:
                print("Skipping non-pdf source file", source_file)
    else:
        print("No source file(s) provided")
