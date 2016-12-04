PlainKey = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.,'"
EnigmaKey = "T'60US7,ORW 89HC3YJMKEIB1QVDXFP52ZN4ALG."
Cypher = "OV HEUV6TMJGV'KMVOV6T9.MVUTMVTVI,H UVH9UL" 


def Decrypt_Cypher(Cypher):
    cipher = ''
    for char in Cypher:
        index1 = EnigmaKey.find(char)
        transLetter = PlainKey[index1]
        cipher += transLetter
    print (cipher)

Decrypt_Cypher(Cypher)
    
