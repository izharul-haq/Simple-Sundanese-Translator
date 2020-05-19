"""
File ini merupakan modul pencocokan string menggunakan algoritme KMP.
"""

from typing import List

def border_function(pttr : str) -> List[int]:
    """
    Mengembalikan senarai yang berisikan nilai border function untuk
    masing-masing karakter dari pola
    
    CONTOH :
        
        - border_function('abacab') mengembalikan [0, 0, 0, 1, 0, 1]
    """

    size: int = len(pttr)
    idx: int = 0
    n_idx: int = 1

    fail_list: List[int] = [None for i in range(size)]
    fail_list[0] = 0

    while n_idx < size :
        if pttr[idx] == pttr[n_idx] :
            fail_list[n_idx] = idx + 1
            idx += 1 ; n_idx += 1
        
        elif idx > 0 :
            idx = fail_list[idx - 1]
        
        else :
            fail_list[n_idx] = 0
            n_idx += 1
    
    return fail_list

def kmp(text : str, pttr : str) -> int:
    """
    Mengembalikan indeks pertama bagian dari teks yang cocok dengan pola.
    Jika tidak ada bagian teks yang cocok dengan pola akan mengembalikan -1.
    Proses pencarian pola pada teks menggunakan algoritme KMP.

    CONTOH:
        
        - KMP_matching('Mencari-cari kunci jawaban', 'cari') mengembalikan 3
        - KMP_matching('Mencari-cari kunci jawaban', 'langit') mengembalikan -1
    """
    
    txt_size: int = len(text)
    ptr_size: int = len(pttr)

    ptr_fail: List[int] = border_function(pttr)

    txt_idx: int = 0
    ptr_idx: int = 0

    while txt_idx < txt_size:
        if pttr[ptr_idx] == text[txt_idx]:
            if ptr_idx == ptr_size - 1:
                return txt_idx - ptr_size + 1

            txt_idx += 1
            ptr_idx += 1
        
        elif ptr_idx > 0:
            ptr_idx = ptr_fail[ptr_idx - 1]
        
        else :
            txt_idx += 1
        
    return -1