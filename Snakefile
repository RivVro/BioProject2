rule ophalen_data:
	input:
		'inputFile.txt'
	output:
		'outputVariants.txt'
	run:
		with open(input[0],"r") as f:
			line = f.readline()
			waarden = line.split(",")
			chrom = waarden[0]
			pos = waarden[1]
			aft = waarden[2].replace("\n", "")
			shell("wget 'http://0.0.0.0:5000/?chrom={chrom}&pos={pos}&aft={aft}' --output-document {output} ")

rule input_databasedata:
	input:
		txtbestand = "lijstSNP.txt",
		pythonbestand = "pythonbestand"
	shell:
		"python3 {input.pythonbestand}{input.txtbestand}"
