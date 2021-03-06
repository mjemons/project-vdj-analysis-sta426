#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""demultiplexer.py

This script demultiplex the data, i.e. it creates a separate file for each
cell containing the contigs.

Adapted from: https://github.com/Teichlab/bracer/issues/21

"""


import os


list_of_cells = list()


def main():
    for folder in os.listdir("../data/demultiplexed"):
        if "preprocessed" in folder:
            os.removedirs(folder)

    for folder in os.listdir("../data/raw"):
        with open(
            f"../data/raw/{folder}/outs/filtered_contig.fasta", "r"
        ) as input:
            for line in input:
                if line.startswith(">"):
                    cell = line.split("-1_contig")[0][1:]
                    list_of_cells.append(cell)

                if not os.path.exists(
                    f"../data/demultiplexed/{folder}-preprocessed/"
                ):
                    os.mkdir(f"../data/demultiplexed/{folder}-preprocessed/")

                with open(
                    f"../data/demultiplexed/{folder}-preprocessed/{cell}.fasta",
                    "a",
                ) as output:
                    output.write(line)

        with open(
            f"../data/demultiplexed/{folder}-preprocessed/list_of_cells.txt",
            "w",
        ) as file:
            file.write(str(list_of_cells))


if __name__ == "__main__":
    main()
