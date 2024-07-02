import pandas as pd
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
import datetime

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Leer el archivo JSON en un DataFrame de pandas
    df = pd.read_json(file_path, lines=True)
    # Preparar los datos: fecha y usuario
    data = zip(df['date'].dt.date, df['user'].apply(lambda x: x['username']))

    def count_posts(data):
        # Función auxiliar para contar posts por usuario en una fecha
        date, username = data
        return date, Counter({username: 1})

    counts = Counter()
    # Utilizar ThreadPoolExecutor para paralelizar el conteo
    with ThreadPoolExecutor() as executor:
        for date, user_count in executor.map(count_posts, data):
            if date not in counts:
                counts[date] = Counter()
            counts[date].update(user_count)

    # Obtener las 10 fechas con más actividad
    top_dates = Counter({date: sum(users.values()) for date, users in counts.items()}).most_common(10)
    # Devolver el usuario más activo para las 10 fechas con más actividad
    return [(date, counts[date].most_common(1)[0][0]) for date, _ in top_dates]
