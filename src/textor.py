"""
File ini merupakan modul untuk memproses teks
"""

def trim(text : str, prev_idx : int) -> str:
    """
    Mengembalikan kata selanjutnya dan seterusnya relatif terhadap
    indeks dari kata tersebut. Jika indeks berada di kata terakhir
    maka fungsi mengembalikan ''
    
    CONTOH :
        
        - trim_word('tucilnya susah banget', 3) mengembalikan 'susah banget'
        - trim_word('stop', 1) mengembalikan ''
    """
    
    i: int = prev_idx + 1
    txt_size: int = len(text)

    while i < txt_size and text[i] != ' ':
        i += 1
    
    if i == txt_size:
        return ''
    
    else:
        return text[i + 1 :]

def get_word(text : str) -> (str, str):
    """
    Mengekstrak sebuah kata dari teks dimulai dari sebelah kiri
    serta teks sisanya
    """

    first_space_index: int = text.find(' ')

    head: str = text[ : first_space_index - 1]
    tail: str = text[first_space_index + 1 : ]

    return (head, tail)