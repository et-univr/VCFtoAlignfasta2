#import vcf

#vcf_reader = vcf.Reader(filename='DANSNP.vcf')
#record = next(vcf_reader)
#print(record.POS)
import vcf
import pandas as pd

def create_snp_matrix(vcf_files):
    """Creates a SNP matrix from a list of VCF files.

    Args:
        vcf_files (list): A list of VCF file paths.

    Returns:
        pandas.DataFrame: The SNP matrix.
    """

    all_snps = set()
    sample_names = set()
    snp_data = {}

    # Extract SNPs and sample names
    for vcf_file in vcf_files:
        vcf_reader = vcf.Reader(filename=vcf_file)
        sample_names.update(vcf_reader.samples)
        for record in vcf_reader:
            snp_key = f"{record.CHROM}_{record.POS}_{record.REF}_{record.ALT}"
            all_snps.add(snp_key)
            for sample in record.samples:
                if snp_key not in snp_data:
                    snp_data[snp_key] = {}
                    
                snp_data[snp_key][sample.sample] = sample.gt_bases[0] 
                
                    
    # Create SNP matrix
    snp_df = pd.DataFrame(snp_data).T
    snp_df.index.name = 'SNP'
    snp_df = snp_df.reindex(sorted(snp_df.index), axis=0)
    snp_df = snp_df.reindex(sorted(sample_names), axis=1)
    snp_df = snp_df.fillna(0)

    return snp_df

# applica la funzione su tutti i vcf della cartella corrente
vcf_files = [ ]
import os
for file in os.listdir(os.getcwd()):#"C:/Users/HP/Desktop/Miceti/Fungi/VCFtotalifiltrati/Allineamento SNP/"
    if file.endswith(".vcf"):
        vcf_files.append(os.path.join(os.getcwd(), file))#"C:/Users/HP/Desktop/Miceti/Fungi/VCFtotalifiltrati/Allineamento SNP/"


snp_matrix = create_snp_matrix(vcf_files)
print(snp_matrix)
allineamento = {}
for i in snp_matrix.columns:
    seq = ''
    for j in snp_matrix.index:
        if snp_matrix[i][j] == 0:
            seq += j.split('_')[-2]
        else:
            seq += snp_matrix[i][j]
    allineamento[i] = seq
f = open("SNP.fasta", "w")
for i in allineamento.keys():
    print(">"+i)
    print(allineamento[i])
    print(len(allineamento[i]))
    f.write(">"+i+"\n"+allineamento[i]+"\n")
f.close()



    
snp_matrix.to_excel('SNP.xlsx')


