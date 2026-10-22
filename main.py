"""
O que estudamos:
1) Tipagem dinâmica(inferência) x Tipagem estática(explícita);
2) Tipagem forte x Tipagem fraca;
3) Variáveis, o que são;
4) Funções, o que são [type(),print(), input()]
5) Tipos de dados
6) Conversão de Tipo
7) Exception comuns ValueError, TypeError
8) Boas práticas de nomeação de Variáveis
9) Operadores aritméticos [+-*/%//**]
10) Tipo de resultados de operações
11) Criador da linguagem Guido Van Rossun (Finlandês)
12) O Python é uma linguagem interpretada

Bonus:
13) Type Hints
14) Padrão de nomeação de variáveis snake_case




Funcoes:
    type();
    print();
    input();


Operadores aritméticos;
    +: soma
    -: subtracao
    *: multiplicacao
    /: divisao
    //: divisao inteira
    %: resto
    **: exponenciacao
"""

# SOMA
soma_int = 10 + 10
soma_float = 10.0 + 10.1
print("Conteúdo soma_int: ", soma_int)
print("Tipo soma_int: ", type(soma_int), "\n")

print("Conteúdo soma_float: ", soma_float)
print("Tipo soma_float: ", type(soma_float), "\n")

# SUBTRACAO
sub_int = 11 - 10
sub_float = 10.3 - 10.1
print("Conteúdo sub_int: ", sub_int)
print("Tipo sub_int: ", type(sub_int), "\n")

print("Conteúdo sub_float: ", sub_float)
print("Tipo sub_float: ", type(sub_float), "\n")

# MULTIPLICACAO
mult_int = 11 * 10
print("Conteúdo mult_int: ", mult_int)
print("Tipo mult_int: ", type(mult_int), "\n")

mult_float = 11 * 10.0
print("Conteúdo mult_float: ", mult_float)
print("Tipo mult_float: ", type(mult_float), "\n")

# DIVISAO
div_int = 10 / 2
print("Conteúdo div_int: ", div_int)
print("Tipo div_int: ", type(div_int), "\n")

div_float = 10 / 3
print("Conteúdo div_float: ", div_float)
print("Tipo div_float: ", type(div_float), "\n")


# DIVISAO INTEIRA
div_inteira_int = 10 // 2
print("Conteúdo div_inteira_int: ", div_inteira_int)
print("Tipo div_inteira_int: ", type(div_inteira_int), "\n")

div_inteira_float = 10 // 3
print("Conteúdo div_inteira_float: ", div_inteira_float)
print("Tipo div_inteira_float: ", type(div_inteira_float), "\n")

# RESTO
resto = 10 % 3
print("Conteúdo resto: ", resto)
print("Tipo resto: ", type(resto), "\n")

# EXPONENCIACAO
exponenciacao = 10**3
print("Conteúdo exponenciacao: ", exponenciacao)
print("Tipo exponenciacao: ", type(exponenciacao), "\n")

# BONUS
# TYPE
num: int = 10  # Type Hint
print("num na linha 95: ", type(num))
num = "10"
print("num na linha 97: ", type(num))

