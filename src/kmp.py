from typing import List
import math

def border_function(text : str) -> List[int]:
    """
    Return list of border function values for each character from pattern
    
    EXAMPLE :
        
        - border_function('abacab') returns [0, 0, 0, 1, 0, 1]
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
    Return index of the first character from substring that matches with
    the pattern using KMP algorithm. If no substring matches with the pattern,
    return -1.

    EXAMPLE:
        
        - KMP_matching('Mencari-cari kunci jawaban', 'cari') returns 3
        - KMP_matching('Mencari-cari kunci jawaban', 'langit') returns -1
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
    Searching for a whole word from text that matches with the pattern.
    This function only iterate the text once. If a substring from the text
    matches with the pattern, this function will return wether this substring
    is whole word or not.
    
    Cases that could happen:  
        
        - No substring matches with the pattern, return false.
        - Substring matches with the pattern but it is not a whole word, return false
        - Substring matches with the pattern and it is a whole word, return true
    
    EXAMPLE:  
        
        - KMP_exact\_matching('Fly to the sky', 'moon') return false
        - KMP_exact_matching('Currently eating now', 'eat') return false
        - KMP_exact_matching('Typewriter is using the type machine', 'type') return true
    """

    first_idx: int = KMPMatching(text, pttr)

    if first_idx == -1:                                     # Pattern not found
        return False
    
    elif first_idx == 0:                                    # Pattern found in the beginning of the text
        if text == pttr:                                   
            return True
        
        else:
            return text[first_idx + len(pttr)] == ' '
    
    else:
        if first_idx + len(pttr) == len(text):              # Pattern found in the end of the text
            return text[first_idx - 1] == ' '
        
        else:                                               # Pattern found in the middle of the text
            return text[first_idx - 1] == ' ' and text[first_idx + len(pttr)] == ' '