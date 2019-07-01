rule dataOphalen:
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
                shell("wget 'http://0.0.0.0:5000/?chrom={chrom}&pos={pos}&aft={aft}' --output-document {output}")

#rule all:
#    input:
#        'checked.txt'

#regel voor het ophalen van de data
#rule dataOphalen:
#inputFile is een bestand dat door de user wordt gegeven
#	input:
#		'inputFile.txt'
#het resultaat van de rule komt in een txt bestand
#	output:
#		'outputVariants.txt'
#	run:
#		with open(input[0],"r") as f:
#		    line = f.readline()
#			waarden = line.split(",")
#			chrom = waarden[0]
#			pos = waarden[1]
#			aft = waarden[2].replace("\n", "")
#			shell("wget 'http://0.0.0.0:5000/?chrom={chrom}&pos={pos}&aft={aft}' --output-document {output}")

#rule checkinput:
#    input:
#        'inputFile.txt'
#    output:
#        'checked.txt'
#    run:
#        with open(input[0],"r") as input:
#            text = input.read(1)
#            if not text:
#                print("Bestand is leeg")
#            else:
#                print("Bestand is niet leeg"
