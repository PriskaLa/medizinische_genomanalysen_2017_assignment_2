#! /usr/bin/env python2.7

import vcf

__author__ = 'Priska Lang'


class Assignment2:
    """
    Provides code to calculate and print various properties of the file AmpliseqExome.20141120.NA24385.vcf.

            This class parses the file AmpliseqExome.20141120.NA24385.vcf and calculates the following properties unsing
            the pyvcf module:
            - average quality of son
            - total number of variants of son
            - variant caller of vcf
            - human reference version
            - number of indels
            - number of snvs
            - number of heterozygous variants
            For more information see: https://pyvcf.readthedocs.io/en/latest/

            It provides the constructor method and the method "print_summary" for easy analyzing a vcf file.
            """

    def __init__(self):
        """
        The constructor method validates if pyvcf is installed and calculates various properties of the file
        AmpliseqExome.20141120.NA24385.vcf using the pyvcf module.
        """

        # Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)

        # variable declaration & reading and data:
        self.vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf","r"))
        self.indels = 0                                                 # for counting the indels
        self.qualities = []                                             # list with the qualities of the input file
        self.variantsSon = 0                                            # for counting the variants
        self.hets = 0                                                   # for counting the heterozygous variants
        self.variantCaller = []                                         # for checking witch variant caller was used
        self.snvs = 0                                                   # for counting the SNVs
        self.reference = str.split(self.vcf.metadata["reference"], "/")  # for checking the human reference version

        # calculating the values from vcf body:
        for record in self.vcf:
            self.qualities.append(record.QUAL)
            self.variantsSon += 1
            if record.is_indel:
                self.indels += 1
            if record.num_het > 0:
                self.hets += 1
            if record.is_snp:
                self.snvs += 1

        # calculating the values from vcf header:
        for line in self.vcf._header_lines:
             if line.startswith("##source="):
                 self.variantCaller = str.split(line,'"')

    def print_summary(self):
        """
        print_summary prints the values calculated within the constructor method.

                :Example:

                For the given input file the following is printed on the console:

            :Example:
            PyVCF version: 0.6.8
            average quality of son:
            1753.77822224
            total nuber of variants of son:
            38526
            variant caller of vcf:
            tvc 4.5-1+0 (8ffe53a) - Torrent Variant Caller
            human reference version:
            hg19
            number of indels:
            1823
            number of snvs:
            36703
            number of heterozygous variants:
            23819
            """

        print("average quality of son:")
        # calculating and printing mean of the quality values:
        print(float(sum(self.qualities)) / max(len(self.qualities), 1))
        print("total nuber of variants of son:")
        print(self.variantsSon)
        print("variant caller of vcf:")
        print(self.variantCaller[1])
        print("human reference version:")
        print(self.reference[6])
        print("number of indels:")
        print(self.indels)
        print("number of snvs:")
        print(self.snvs)
        print("number of heterozygous variants:")
        print(self.hets)

# cue:
if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2()
assignment1.print_summary()