import os
import pandas as pd

def load_data(filename):
    """
    Carga un CSV desde la carpeta 'data/' usando rutas robustas.
    """
    base_path = os.path.dirname(os.path.dirname(__file__))  # sube un nivel desde src/
    data_path = os.path.join(base_path, "data", filename)
    return pd.read_csv(data_path)
