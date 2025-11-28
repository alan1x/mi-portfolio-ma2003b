import os
import matplotlib.pyplot as plt

def save_plot(filename):
    """
    Guarda la gráfica actual en la carpeta 'visualizations/'
    usando rutas robustas.
    """
    base_path = os.path.dirname(os.path.dirname(__file__))  # sube un nivel desde src/
    viz_path = os.path.join(base_path, "visualizations", filename)
    plt.savefig(viz_path, bbox_inches='tight')
