fin=open ("sample.txt", "r") 
fout=open ("enc.txt","w")
plainText=fin.read ()
distance=int (input ("Enter the distance value: ")) 
cipherText=""
for ch in plainText: 
    ordValue=ord (ch)
    ciphervalue=ordValue+distance 
    if cipherValue>ord ('z') :
        cipherValue=ord ('a')+distance-(ord ('z')-ordValue+1)
    cipherText+=chr (cipherValue)
fout.write (cipherText)
fin.close ()
fout.close ()