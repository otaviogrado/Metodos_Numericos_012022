'''
- Lista de Exercícios II -
- Trabalho individual

Usando NumPy, MatPlotLib e SciPy implemente os seguintes exercícios para exploração
e fixação de comandos e métodos destes módulos.

Os gráficos plotados ou cópias de tela de execução destes exercícios estão
disponíveis na pasta "Exemplos de Resultados" e servem para exemplificar
uma possível solução (estão lá apenas para servir de apoio de explicação).


1) Utilizando o  intervalo [-PI, +PI], plote um gráfico usando o cos(x) como abscissa e o sen(x) como ordenada.
   Pesquise a função sobre axes no matplotlib (ou como foi feito nos exemplos anteriores)
   para deixar o gráfico quadrado, mesma proporção largura x altura,
   caso contrário o círculo parecerá uma elipse.


2) Empregando sen(x) no mesmo intervalo [-PI, +PI], mas agora usando np.arange (com passo 0.2),
   plote 6 gráficos, de sen(x) até sen(x-1), deslocando cada plot de 0.2,
   ou seja sen(x), sen(x-0.2) etc., usando para chamada ao plot os seguintes modelos de linhas:
   '-'    '--'    ':'     '-.'      '.'      'o'
   Depois, brinque com o parâmetro opcional color='cor' testando cores disponíveis (ver na documentação)


3) Plote os dois polinômios f(x) e g(x):
   f(x) = -2xˆ4 + 3xˆ3 + 7xˆ2 -10x + 18
   g(x) = xˆ4 +2xˆ3  -13xˆ2 -14x + 24
   Com x no intervalo [-4.5, 4.5] com 300 pontos. Antes de plt.show(), chame plt.grid().
   Implemente as funções em código Python:
   def f(x):
      # retorno da função f
   def g(x):
      # retorno da função g
   Coloque as equações dos polinômios como rótulos (ver nos exemplos anteriores).
   Pesquise como centralizar os spines em 0,0 de forma a criar um gráfico com
   os eixos cartesianos mostrados no formato tradicional.


4) Crie uma função python que retorna o maior de dois números enviados por parâmetro.
   Ela irá funcionar de maneira regular, ou seja, operando sobre 2 escalares.
   Verifique o funcionamento da função NumPy vectorize, e crie então a função
   que opera sobre vetores.

   Teste sua função duas vezes:
   a) com dois arrays numpy de 10 posições sorteadas de números inteiros
   no intervalo [10, 100[
   b) com dois arrays numpy de 10 posições sorteadas de números reais
   no intervalo ]0, 1[ .
   Em ambos cenários mostre os 3 vetores e use funções do NumPy para o sorteio.


5) Calculando área aproximada com Soma de Riemann

   Elabore um programa que aplique a Soma de Riemann para estimar a área
   solicitando ao usuário o tamanho do passo (base do retângulo), apresente
   o valor estimado da área e o erro relativo.
   Os passos devem ser frações exatas de 1, como por exemplo:
   1, 0.5, 0.25, 0.125, 0.1, 0.0625, 0.05, 0.04, 0.03125, 0.025, 0.0125 etc
   para não extrapolarem o intervalo.

   Erro relativo = | analitico - aproximado | / | analítico |

   Plote o gráfico apresentando os retângulos, o valor aproximado e o erro
   relativo.
   Dica para plotar os retângulos: simplesmente usar plt.bar (deixando as cores sem interferir)
   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html

   Para comparar o resultados, crie 3 gráficos (sub plots) na mesma plotagem
   e contabilize os três valores da área calculada:
   - pegando altura pela esquerda (antes do passo)
   - pegando altura no meio (métade do passo)
   - pegando altura pela direita (depois do passo)

   Use a função python criada para calcular as seguintes integrais definidas:
   a) Para a reta f(x) = 2x, integrada no intervalo [1, 4], cuja solução analítica é 15.
   (ver gráficos exemplos de resultado)

   b) Para a função f(x) = 1/8(x^2 -2x + 8), integrada no intervalo [-2, 4], cuja solução
   analítica é 15/6.
'''

'''
    ************************************* TERMINADO ************************************* 
1) Utilizando o  intervalo [-PI, +PI], plote um gráfico usando o cos(x) como abscissa e o sen(x) como ordenada.
   Pesquise a função sobre axes no matplotlib (ou como foi feito nos exemplos anteriores) 
   para deixar o gráfico quadrado, mesma proporção largura x altura, 
   caso contrário o círculo parecerá uma elipse.


# BIBLIOTECAS
import numpy as np
import matplotlib.pyplot as plt

# VARIÁVEIS
num = np.linspace(-np.pi, np.pi, 100)
x = np.cos(num)
y = np.sin(num)

# PLOTS:
plt.figure(figsize=(3,4))
plt.plot(x,y)
plt.axis('scaled')
plt.suptitle('EXERCICIO 1')
plt.show()
'''

''' 
    ************************************* TERMINADO ************************************* 
2) Empregando sen(x) no mesmo intervalo [-PI, +PI], mas agora usando np.arange (com passo 0.2), 
   plote 6 gráficos, de sen(x) até sen(x-1), deslocando cada plot de 0.2,
   ou seja sen(x), sen(x-0.2) etc., usando para chamada ao plot os seguintes modelos de linhas:
   '-'    '--'    ':'     '-.'      '.'      'o'
   Depois, brinque com o parâmetro opcional color='cor' testando cores disponíveis (ver na documentação)


# bibliotecas
import matplotlib.pyplot as plt
import numpy as np

# variáveis globais
x = np.arange(-np.pi, np.pi,0.2)
l_pontos = []

#formatos = ['-', '--', ':','-.', '.', 'o']             # não funciona o comando passado pelo professor
formatos = ['-', '--', ':','-.', '--', ':']
cores = ['b', 'g', 'r', 'c', 'm', 'y']

for i in range(6):                                      # loop para realizar iterações
    plt.grid()                                          # grid inicial para todos os gráficos

    l_pontos.append(np.sin(x-0.2*i))                    # comandos principais
    plt.subplot(3,2,i+1)
    plt.plot(x, l_pontos[i], linestyle = formatos[i], color = cores[i])

    plt.title(f"Gráfico sen(x-{round(0.2*i, 2)})")      # printa o titulo com arredondamento para duas casas decimais do valor de 0.2*i
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo Y')

plt.grid()                                              # grid no ultimo gráfico
plt.suptitle('EXERCICIO 2')
plt.show()
'''


'''
    ************************************* TERMINADO ************************************* 
3) Plote os dois polinômios f(x) e g(x):
   f(x) = -2xˆ4 + 3xˆ3 + 7xˆ2 -10x + 18
   g(x) = xˆ4 +2xˆ3  -13xˆ2 -14x + 24
   Com x no intervalo [-4.5, 4.5] com 300 pontos. Antes de plt.show(), 
   chame plt.grid(). 
   Implemente as funções em código Python:
   def f(x): 
      # retorno da função f
   def g(x): 
      # retorno da função g     
   Coloque as equações dos polinômios como rótulos (ver nos exemplos 
   anteriores).Pesquise como centralizar os spines em 0,0 de forma a 
   criar um gráfico com os eixos cartesianos mostrados no formato 
   tradicional.


# bibliotecas
import matplotlib.pyplot as plt
import numpy as np


# FUNÇÕES AUXILIARES
def f(x):
    return -(2*(x**4)) + (3*(x**3)) + (7*(x**2)) - (10*x) + 18

def g(x):
    return (x**4) + (2*(x**3)) - (13*(x**2)) - (14*x) + 24


# VARIÁVEIS
eixoX = np.linspace(-4.5,4.5,300)
f1 = np.vectorize(f)
f2 = np.vectorize(g)
eixoY1 = f1(eixoX)
eixoY2= f2(eixoX)

# PLOTAGEM GRÁFICA
fig, ax = plt.subplots()
# making the top and right spine invisible:
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# moving bottom spine up to y=0 position:
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('axes',0))

# moving left spine to the right to position x == 0:
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('axes',0))


plt.plot(eixoX, eixoY1, label = 'Gráfico f(x)')                 # plotagem gráfica das funções
plt.plot(eixoX, eixoY2, label = 'Gráfico g(x)')

plt.title('EXERCICIO 3')                                        # layout do gráfico 
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.grid()

plt.show()
'''


'''
4) Crie uma função python que retorna o maior de dois números enviados por parâmetro.
   Ela irá funcionar de maneira regular, ou seja, operando sobre 2 escalares.
   Verifique o funcionamento da função NumPy vectorize, e crie então a função
   que opera sobre vetores.

   Teste sua função duas vezes:
   a) com dois arrays numpy de 10 posições sorteadas de números inteiros
   no intervalo [10, 100[
   b) com dois arrays numpy de 10 posições sorteadas de números reais
   no intervalo ]0, 1[ .
   Em ambos cenários mostre os 3 vetores e use funções do NumPy para o sorteio.
'''


'''
5) Calculando área aproximada com Soma de Riemann

   Elabore um programa que aplique a Soma de Riemann para estimar a área
   solicitando ao usuário o tamanho do passo (base do retângulo), apresente
   o valor estimado da área e o erro relativo.
   Os passos devem ser frações exatas de 1, como por exemplo:
   1, 0.5, 0.25, 0.125, 0.1, 0.0625, 0.05, 0.04, 0.03125, 0.025, 0.0125 etc
   para não extrapolarem o intervalo.

   Erro relativo = | analitico - aproximado | / | analítico |

   Plote o gráfico apresentando os retângulos, o valor aproximado e o erro
   relativo.
   Dica para plotar os retângulos: simplesmente usar plt.bar (deixando as cores sem interferir)
   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html

   Para comparar o resultados, crie 3 gráficos (sub plots) na mesma plotagem
   e contabilize os três valores da área calculada:
   - pegando altura pela esquerda (antes do passo)
   - pegando altura no meio (métade do passo)
   - pegando altura pela direita (depois do passo)

   Use a função python criada para calcular as seguintes integrais definidas:
   a) Para a reta f(x) = 2x, integrada no intervalo [1, 4], cuja solução analítica é 15.
   (ver gráficos exemplos de resultado)

   b) Para a função f(x) = 1/8(x^2 -2x + 8), integrada no intervalo [-2, 4], cuja solução
   analítica é 15/6.
'''