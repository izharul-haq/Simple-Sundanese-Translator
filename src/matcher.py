"""
File ini merupakan modul untuk melakukan pencocokan secara eksak
"""

from kmp import kmp
from bm import bm
from textor import trim
    
def exact_matching(method, text : str, pttr : str) -> bool:
    """
    Mencari bagian dari teks yang cocok dengan pola secara eksak
    (bagian dari teks yang ditemukan bukan potongan dari sebuah kata,
    lihat contoh untuk lebih jelas) dalam sekali iterasi.
    
    Cara kerja fungsi ini adalah dengan mencari terlebih dahulu bagian
    dari teks yang cocok dengan pola kemudian mengevaluasi apakah bagian
    tersebut merupakan kalimat utuh atau tidak.

    Kasus-kasus yang mungkin adalah sebagai berikut:  
        
        - Pola tidak ditemukan dalam teks, mengembalikan FALSE.
        - Terdapat pola pada teks namun tidak eksak, mengembalikan FALSE
        - Terdapat pola pada teks dan eksak sama, mengembalikan TRUE
    
    CONTOH:
        
        - exact_matching(kmp, 'Fly to the sky', 'moon') mengembalikan FALSE
        - exact_matching(kmp, 'Currently eating now', 'eat') mengembalikan FALSE
        - exact_matching(kmp, 'Typewriter is using the type machine', 'type') mengembalikan TRUE
    """

    first_idx: int = method(text, pttr)

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

def exact_whole_search(method, text : str, pttr : str) -> bool:
    """
    Mengembalikan apakah terdapat kata-kata pada teks yang cocok dengan pola
    dengan menggunakan algoritme sesuai dengan masukan.
    
    Fungsi ini akan mencari hingga benar-benar dipastikan terdapat kata-kata
    yang sesuai dengan pola yang satu kesatuan dalam teks yang diberikan atau tidak.
    
    CONTOH:

        - exact_whole_search(kmp, 'Seleksi asisten-lab untuk lab IRK', 'lab') mengembalikan TRUE
        - exact_whole_search(kmp, 'Seleksi asiten lab-lab, salah satunya labIRK', 'lab') mengembalikan FALSE
    """

    first_idx: int = method(text, pttr)

    if first_idx == -1:
        return False
    
    else:
        found: bool = False
        while len(text) >= len(pttr) :
            if exact_matching(method, text, pttr) :
                found = True
                break
            
            else :
                text = trim(text, first_idx)
                first_idx = method(text, pttr)

        return found

if __name__ == '__main__':
    txt: str = input('teks : ')
    ptr: str = input('pola : ')
    mtd: int = int(input('1. KMP\n2. BM\nMasukan metode : '))


    found : bool
    if mtd == 1:
        found = exact_whole_search(kmp, txt, ptr)
    elif mtd == 2:
        found = exact_whole_search(bm, txt, ptr)

    if found:
        print ('pola ditemukan')
    else:
        print ('pola tidak ditemukan')