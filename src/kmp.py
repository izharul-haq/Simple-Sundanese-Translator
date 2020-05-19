from typing import List

"""
File ini merupakan modul pencocokan string menggunakan algoritme KMP.
"""

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

def KMP_matching(text : str, pttr : str) -> int:
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

def KMP_exact_matching(text : str, pttr : str) -> bool:
    """
    Mencari bagian dari teks yang cocok dengan pola secara eksak
    (bagian dari teks yang ditemukan bukan potongan dari sebuah kata,
    lihat contoh untuk lebih jelas)
    dalam sekali iterasi menggunakan algoritme KMP.
    
    Cara kerja fungsi ini adalah dengan mencari terlebih dahulu bagian
    dari teks yang cocok dengan pola kemudian mengevaluasi apakah bagian
    tersebut merupakan kalimat utuh atau tidak.

    Kasus-kasus yang mungkin adalah sebagai berikut:  
        
        - Pola tidak ditemukan dalam teks, mengembalikan FALSE.
        - Terdapat pola pada teks namun tidak eksak, mengembalikan FALSE
        - Terdapat pola pada teks dan eksak sama, mengembalikan TRUE
    
    CONTOH:
        
        - KMP_exact_matching('Fly to the sky', 'moon') mengembalikan FALSE
        - KMP_exact_matching('Currently eating now', 'eat') mengembalikan FALSE
        - KMP_exact_matching('Typewriter is using the type machine', 'type') mengembalikan TRUE
    """

    first_idx: int = KMP_matching(text, pttr)

    if first_idx == -1:                                     # Pola tidak ditemukan
        return False
    
    elif first_idx == 0:                                    # Pola ditemukan di awal teks
        if text == pttr:                                   
            return True
        
        else:
            return text[first_idx + len(pttr)] == ' '
    
    else:
        if first_idx + len(pttr) == len(text):              # Pola ditemukan di akhir teks
            return text[first_idx - 1] == ' '
        
        else:                                               # Pola ditemukan di tengah-tengah teks
            return text[first_idx - 1] == ' ' and text[first_idx + len(pttr)] == ' '

def KMP_exact_whole_search(text : str, pttr : str) -> bool:
    """
    Mengembalikan apakah terdapat kata-kata pada teks yang cocok dengan pola
    dengan menggunakan algoritme KMP.
    
    Fungsi ini akan mencari hingga benar-benar dipastikan terdapat kata-kata
    yang sesuai dengan pola yang satu kesatuan dalam teks yang diberikan atau tidak.
    """

    first_idx: int = KMP_matching(text, pttr)

    if first_idx == -1:
        return False
    
    else:
        found: bool = False
        while len(text) >= len(pttr) :
            if KMP_exact_matching(text, pttr) :
                found = True
                break
            
            else :
                text = trimWord(text, first_idx)
                first_idx = KMP_matching(text, pttr)

        return found

if __name__ == '__main__' :
    txt : str = input('text string : ')
    ptr : str = input('pttr string : ')

    isExist : bool = KMP_exact_matching(txt, ptr)

    if isExist :
        print ('pttr found')
    else :
        print ('pttr not found')