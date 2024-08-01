from matplotlib import pyplot as plt
import numpy as np

class Plot:

    def plot(self, x, y, z, f):
        x_f = np.linspace(min(x), max(x), 100)
        y_f = np.linspace(min(y), max(y), 100)
        x_f, y_f = np.meshgrid(x_f, y_f)

        # Passo 4: Calcular os Valores da Função
        z_f = f(x_f, y_f)
        
        ax = plt.axes(projection="3d")

        ax.plot_surface(x_f, y_f, z_f, cmap='viridis')
        ax.scatter(x, y, z, s=10, color='r')
        plt.show()
