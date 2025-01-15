import numpy as np
from scipy import integrate, optimize
from scipy.stats import norm
import sympy as sp

#Numpy
print("Numpy")
# Funciones matemáticas comunes
raiz = np.sqrt([1, 4, 9])  # [1., 2., 3.]
logaritmo = np.log([1, np.e, np.e**2])  # [0., 1., 2.]
seno = np.sin(np.pi / 2)  # 1.0

# Álgebra lineal
matriz = np.array([[1, 2], [3, 4]])
inversa = np.linalg.inv(matriz)  # [[-2.,  1.], [ 1.5, -0.5]]
determinante = np.linalg.det(matriz)  # -2.0
autovalores, autovectores = np.linalg.eig(matriz)  # Eigenvalues & Eigenvectors


print("Raiz:\t",raiz)
print("Logaritmo:\t",logaritmo)
print("Seno:\t",seno)
print("Matriz:\n",matriz)
print("Inversa:\n",inversa)
print("Determinante:\t",determinante)
print("Autovalores y Autovectores\n",autovalores, autovectores)

#Scipy
print("Scipy")
# Integración
resultado, error = integrate.quad(lambda x: x**2, 0, 1)  # Integral de x^2 de 0 a 1

# Optimización (mínimos y máximos)
minimo = optimize.minimize(lambda x: x**2 + 2*x + 1, x0=0)  # Mínimo de la función x^2 + 2x + 1

# Distribuciones estadísticas
media, desviacion = 0, 1
probabilidad = norm.cdf(1, loc=media, scale=desviacion)  # P(X ≤ 1) para N(0, 1)
densidad = norm.pdf(0, loc=media, scale=desviacion)  # f(0) para N(0, 1)

print("Integracion:\n",resultado,error)
print("Maximos y minimos:\n", minimo)
print("Probabilidad:\n",probabilidad)
print("densidad:\n",densidad)
#Sympy
print("Sympy")
# Variables simbólicas
x, y = sp.symbols('x y')

# Resolución de ecuaciones
ecuacion = sp.Eq(x**2 - 4, 0)
solucion = sp.solve(ecuacion, x)  # [2, -2]

# Series de Taylor
taylor = sp.series(sp.sin(x), x, 0, 5)  # Aproximación de sin(x) en 5 términos

# Expresiones simbólicas
simplificar = sp.simplify(sp.sin(x)**2 + sp.cos(x)**2)  # 1
expandir = sp.expand((x + y)**2)  # x**2 + 2*x*y + y**2
factorizar = sp.factor(x**2 - 4)  # (x - 2)*(x + 2)

print("Resolucion de ecuaciones:\n",ecuacion,solucion)
print("Series de Taylor:\n",taylor)
print("Expresiones simbolicas:\n",simplificar,expandir,factorizar)