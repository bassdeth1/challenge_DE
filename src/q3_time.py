import pandas as pd
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

def q3_time(file_path: str):
    # Leer el archivo JSON en un DataFrame de pandas
    df = pd.read_json(file_path, lines=True)
    
    def count_mentions(text):
        # Contar todas las menciones en un texto
        return Counter(word for word in text.split() if word.startswith('@'))
    
    counts = Counter()
    # Utilizar ThreadPoolExecutor para paralelizar el conteo de menciones
    with ThreadPoolExecutor() as executor:
        for mentions in executor.map(count_mentions, df['content']):
            counts.update(mentions)
    
    # Devolver las 10 menciones más comunes
    return counts.most_common(10)
