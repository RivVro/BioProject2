import vcf

#Leest vcf bestand met SNP-varianten. Schrijft chromosoom, positie, variantie en frequentie weg in teksbestand dat als input voor database gebruikt wordt.
def lees_bestand():
    vcf_reader = vcf.Reader(open('gnomad.exomes.r2.1.1.sites.Y.vcf', 'r'))
    open("LijstSNP.txt", "w").close()
    for record in vcf_reader:
        try:
            TXTinput = open("LijstSNP.txt", "a+")
            db_Data = '(\''+str(record.CHROM) +'\',\''+ str(record.POS) +'\',\''+ str(record.REF) +'\',\''+ str(record.ALT).replace("[", "").replace("]","") + '\',\''+ str(record.INFO['AF'][0]) + '\'),\n'
            TXTinput.write(db_Data)
            TXTinput.close
        except KeyError:
            continue

def main():
    lees_bestand()

main()

