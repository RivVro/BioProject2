# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:56:40 2019

@author: Nicky
"""
import myvariant				# import die het mogelijk maakt om gegevens van Clinvar op te halen
mv = myvariant.MyVariantInfo()
	
# nog toevoegen: rs code uit outputdb.txt bestand halen dat gemaakt wordt in app.py

info = mv.querymany(['rs121913364'], scopes='dbsnp.rsid')	# Haalt informatie op adv de rs code
a = ([d['_id'] for d in info])								# haalt regel met informatie nodig voor het ophalen van clinvar gegevens uit alle informatie
genomeposition = (a[0])										# zet de bv 'chr1:g.35367G>A' in de variabele genomeposition
print(genomeposition)
clinvar_result = mv.getvariant(genomeposition)				# haalt clinvar resultaten op
text = str(clinvar_result)									# slaat de resultaten op in de variabele text
print(clinvar_result)
file = open("ClinvarResults.txt","w") 						# opend bestand genaamd ClinvarResults.txt
if text == None:											# als text gelijk is aan None wordt er geschreven dat er geen resultaten zijn gevonden
  file.write("No results found on Clinvar")
else:														# als text ongelijk is aan None worden alle gegevens in het txt bestand geschreven
  file.write(text)
file.close()
with open('ClinvarResults.txt', 'r') as f2:
    data = f2.read()
    print(data)
