Creates a SNP matrix from a list of VCF files.
Args: vcf_files (list): A list of VCF file paths.
Returns: pandas.DataFrame: The SNP matrix as an excel file SNP.xlsx.
Download the python script and simply execute it in the folder containing your filtered VCF files.
The script works only with SNP VCF. If a SNP in not present in one of the VCFs the script assign by default the reference base present in that position
