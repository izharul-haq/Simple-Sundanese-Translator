"""
File ini merupakan modul untuk membaca file eksternal
yang merupakan kamus bahasa Indonesia - bahasa Sunda
"""

from typing import Dict, List

def read(file : str) -> Dict[str, List[str]]:
    """
    Mengembalikan map yang berisi sebuah kata serta translasi
    yang mungkin untuk kata tersebut. Untuk lebih jelasnya,
    jalankan file ini dengan masukan:
                    dict/<nama file>.txt
    """
    
    with open(file) as f:
        data: List[str] = f.readlines()
    
    entry: str
    dic: Dict[str, List[str]] = {}

    for entry in data:
        entry_split: List[str, str] = entry.split(' = ')
        
        if entry_split[0] in dic:
            dic[entry_split[0]].append(entry_split[1].replace('\n',''))
        else:
            dic[entry_split[0]] = [entry_split[1].replace('\n', '')]
    
    return dic

if __name__ == '__main__':
    file: str = input('Masukan file : ')
    kamus: Dict[str, List[str]] = read(file)
    
    for entri in kamus:
        print('{} = {}'.format(entri, kamus[entri]))