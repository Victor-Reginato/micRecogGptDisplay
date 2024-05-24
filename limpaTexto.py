import re
from unidecode import unidecode

def limpar_texto(texto):
    # Remove acentos
    texto_sem_acento = unidecode(texto)
    
    # Remove caracteres especiais usando regex
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto_sem_acento)
    
    return texto_limpo