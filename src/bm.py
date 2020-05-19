"""
File ini merupakan modul pencocokan string menggunakan algoritme Boyer-Moore (BM).
"""

from typing import List

def lastFunc(pttr : str) -> List[int]:
    """
    Mengembalikan senarai indeks kemunculan terakhir dari masing-masing
    karakter pada pola. Jika karakter tersebut tidak pernah muncul pada
    pola, maka akan bernilai -1 pada senarai.
    
    CONTOH:
    
        - lastFunc ('abacad') menghasilkan [4, 1, 3, 5, -1, -1, ..., -1]
    """

    idx: int

    last_list: List[int] = [-1 for i in range(128)]

    for idx in range(len(pttr)) :
        last_list[ord(pttr[idx])] = idx

    return last_list

def bm(text : str, pttr : str) -> int:
    """
    Mengembalikan indeks pertama bagian dari teks yang cocok dengan pola.
    Jika tidak ada bagian teks yang cocok dengan pola akan mengembalikan -1.
    Proses pencarian pola pada teks menggunakan algoritme Boyer-Moore (BM).
    
    CONTOH:

        - bm('Mencari-cari kunci jawaban', 'cari') mengembalikan 3
        - bm('Mencari-cari kunci jawaban', 'langit') mengembalikan -1    
    """
    
    txt_size: int = len(text)
    ptr_size: int = len(pttr)
    txt_idx: int = ptr_size - 1

    last_list: List[int] = lastFunc(pttr)

    if txt_idx > txt_size - 1:
        return -1
    
    else:
        ptr_idx: int = ptr_size - 1
        
        while txt_idx <= txt_size - 1:
            if pttr[ptr_idx] == text[txt_idx]:
                if ptr_idx == 0:
                    return txt_idx
                
                else:
                    txt_idx -= 1; ptr_idx -= 1
            
            else:
                last_occ: int = last_list[ord(text[txt_idx])]
                txt_idx = txt_idx + ptr_size - min(ptr_idx, last_occ + 1)
                ptr_idx = ptr_size - 1
            
        return -1