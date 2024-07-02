import json
from collections import Counter

def q3_memory(file_path: str):
    # Contador para las menciones
    counts = Counter()
    
    def extract_mentions(text: str):
        # Extraer todas las menciones del texto
        return [word for word in text.split() if word.startswith('@')]
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Leer cada línea del archivo JSON y extraer menciones
            counts.update(extract_mentions(json.loads(line)['content']))
    
    # Devolver las 10 menciones más comunes
    return counts.most_common(10)
