Encryptor = {
    
    "A": "T",
    "B": "'",
    "C": "6",
    "D": "0",
    "E": "U",
    "F": "S",
    "G": "7",
    "H": ",",
    "I": "O",
    "J": "R",
    "K": "W",
    "L": " ",
    "M": "8",
    "N": "9",
    "O": "H",
    "P": "C",
    "Q": "3",
    "R": "Y",
    "S": "J",
    "T": "M",
    "U": "K",
    "V": "E",
    "W": "I",
    "X": "B",
    "Y": "1",
    "Z": "Q",
    " ": "V",
    "1": "D",
    "2": "X",
    "3": "F",
    "4": "P",
    "5": "5",
    "6": "2",
    "7": "Z",
    "8": "N",
    "9": "4",
    "0": "A",
    ".": "L",
    ",": "G",
    "'": ".",

}

#flip the values to make the Decryptor 
Decryptor = {v: k for k, v in Encryptor.items()}
Cypher = "OV HEUV6TMJGV'KMVOV6T9.MVUTMVTVI,H UVH9UL"


def Decrypt_Cypher(Cypher):
    cipher = ''
    for char in Cypher:
        cipher += Decryptor[char]
    return cipher
    
