import rstr,sys
barcode_pattern = sys.argv[1]
print('{0}'.format(barcode_pattern))

print("Barcode list is as follows : ")
for x in range(5):
	barcode = rstr.xeger(r'{0}'.format(barcode_pattern))
	print(barcode)

print("Done")
