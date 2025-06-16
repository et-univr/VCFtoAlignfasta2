This python script creates a SNP matrix fasta from a list of VCF files.
Dependencies: VCF and Pandas modules
Inputs: A list of VCF files.
Outputs: pandas.DataFrame: The SNP matrix is available as a plain FASTA and as an excel file SNP.xlsx.
Usage: Download the python script and simply execute it in the folder containing your filtered VCF files.
The script works only with SNP VCF. If a SNP in not present in one of the VCFs the script assign by default the reference base present in that position.
