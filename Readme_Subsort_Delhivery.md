The Script will primary sort and Subsort Packets.
Its in Python 2.7

Function:
Create a file awbdel.txt in the same directory and enter your barcodes as follows :
Barcode1
Barcode2
Barcode3
.
.
.
BarcodeN

Run the script as :

python subsortdelhivery.py 192.168.7.127
This script will subsort packets with Login as admin when login api is hit.
The Script will bag 1 shipment in 1 Bag.
The Script is Applicable for M3 Controllers where Controller Id and ArmId are same.
In case one needs to use armid + 512 i.e M4 controller concept , one can contact me.
It doesn't cover hitting Image API and saving images.
It is assumed that PPTL id's are #GP5555 for each arm and it is already configured.
