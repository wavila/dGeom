from numpy import linspace
from pylab import plot,grid,show, xlim, ylim, legend, text

# Funcao hipotetica
def f(x): 
 return x**2+2

# Ponto primario (a) e secundario (b)
a = 3 
b = 7. 

# Limites do grafico
xlim_inf, xlim_sup = -10, 10
ylim_inf, ylim_sup = -3, 100

# Curva da funcao
x = linspace(xlim_inf,xlim_sup,100)
y = f(x)

# Ponto secundario para reta secante
Qx = b
Qy = f(b)

h_zero = 1E-10

# Primeira derivada com h tendendo a zero
fprime = (f(a + h_zero )-f(a))/ h_zero

# Reta tangente no ponto P
tan = f(a)+fprime*(x-a)  

# Inclinacao da reta secante
m = (Qy-f(a))/(Qx-a)

# Reta secante que cruza os pontos P e Q
sec = m*(x-a)+f(a)

# Imprime informacoes
print('Inclinacao da reta secante que une os P(a) e P(b): ', format(m))
print('Inclinacao da reta tangente no ponto P(a): ', format(fprime))

# Plota a funcao, ponto e retas
plot(x,y,'b', label='y(x)')
plot(x,tan,'--r', label='tan')
plot(x,sec,'--g', label='sec')
plot(a,f(a),'om',label='P')
plot(Qx,Qy,'og',label='Q')

# Legenda
legend(loc='upper left')

# Limites dos eixos
xlim(xlim_inf-0.25, xlim_sup+0.25)
ylim(ylim_inf, ylim_sup)

# Imprime quadriculado e exibe
grid()
show()
