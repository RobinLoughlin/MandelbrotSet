import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

class MandelbrotSet:
    def __init__(self, max_iter = 255, escape_radius = 2):
        self.max_iter = max_iter
        self.escape_radius = escape_radius
        
    def is_in_mandelbrot(self, c):
        """
        Determines if the complex number c is in the Mandelbrot set
        using the escape time algorithm.
        """
        z = 0
        for n in range(self.max_iter):
            if abs(z) > self.escape_radius:
                return n
            z = z*z + c
    
    def generate_mandelbrot(self, x_min, x_max, y_min, y_max, width, height):
        """
        Generates a 2D array representing the Mandelbrot set over the specified range and resolution.
        """
        x_vals = np.linspace(x_min, x_max, width)
        y_vals = np.linspace(y_min, y_max, height)

        image = np.zeros((height, width))

        for i, y in enumerate(y_vals):
            for j, x in enumerate(x_vals):
                c = complex(x, y)
                m = self.is_in_mandelbrot(c)
                image[i, j] = m

        return image
    
if __name__ == "__main__":
    mandelbrot = MandelbrotSet(max_iter=255)

    x_min, x_max = float(input("Enter x_min: ")), float(input("Enter x_max: "))
    y_min, y_max = float(input("Enter y_min: ")), float(input("Enter y_max: "))

    width, height = int(input("Enter image width: ")), int(input("Enter image height: "))

    data = mandelbrot.generate_mandelbrot(x_min, x_max, y_min, y_max, width, height)

    plt.figure(figsize=(10, 10))
    plt.imshow(data, extent=(x_min, x_max, y_min, y_max), cmap="plasma")
    plt.colorbar(label="Iterations to divergence")
    plt.title("Mandelbrot Set")
    plt.xlabel("Real part")
    plt.ylabel("Imaginary part")
    plt.show()







                               




    
