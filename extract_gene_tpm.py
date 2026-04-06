import os
import pandas as pd

assemble_dir = "assemble" # Change to assemble directory after running stringtie
tpm_dict = {}

for sample in sorted(os.listdir(assemble_dir)):
    tab_file = os.path.join(assemble_dir, sample, f"{sample}_gene_abundance.tab")
    if not os.path.exists(tab_file):
        continue
    df = pd.read_csv(tab_file, sep="\t", skipinitialspace=True)
    df.columns = df.columns.str.strip()
    tpm_dict[sample] = df.groupby("Gene ID")["TPM"].sum()

tpm_matrix = pd.DataFrame(tpm_dict)
tpm_matrix.index.name = "gene_id"
tpm_matrix.to_csv("gene_tpm_matrix.csv")
print(f"TPM matrix shape: {tpm_matrix.shape}")