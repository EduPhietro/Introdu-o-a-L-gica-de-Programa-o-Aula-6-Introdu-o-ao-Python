""""
O que estudamos:
1) Tipagem dinâmica (inferência) x Tipagem estática (explícita);
2) Tipagem forte x Tipagem fraca;
3) Variáveis, o que são;
4) Funções nativas [type(), print(), input()]
5) Tipos de dados
6) Conversão de Tipo (Casting)
7) Exceptions comuns: ValueError, TypeError
8) Boas práticas de nomeação de Variáveis
9) Operadores aritméticos [+, -, *, /, //, %, **]
10) Tipo de resultados de operações
11) Criador da linguagem: Guido Van Rossum (Holandês - Obs: correção do país de origem)
12) O Python é uma linguagem interpretada

Bônus:
13) Type Hints
14) Padrão de nomeação de variáveis: snake_case
"""

# ==========================================
# TESTES DE OPERADORES ARITMÉTICOS E TIPAGEM
# ==========================================

# 1. SOMA (+)
# Se ambos são inteiros (int), o resultado é int.
soma_int = 10 + 10
print("Conteúdo soma_int:", soma_int)
print("Tipo soma_int:", type(soma_int), "\n")

# Se há pelo menos um número decimal (float), o resultado é float.
soma_float = 10.0 + 10.1
print("Conteúdo soma_float:", soma_float)
print("Tipo soma_float:", type(soma_float), "\n")


# 2. SUBTRAÇÃO (-)
sub_int = 11 - 10
sub_float = 10.3 - 10.1
print("Conteúdo sub_int:", sub_int)
print("Tipo sub_int:", type(sub_int), "\n")

print("Conteúdo sub_float:", round(sub_float, 2)) # round() usado para corrigir precisão de ponto flutuante
print("Tipo sub_float:", type(sub_float), "\n")


# 3. MULTIPLICAÇÃO (*)
mult_int = 11 * 10
print("Conteúdo mult_int:", mult_int)
print("Tipo mult_int:", type(mult_int), "\n")

mult_float = 11 * 10.0
print("Conteúdo mult_float:", mult_float)
print("Tipo mult_float:", type(mult_float), "\n")


# 4. DIVISÃO (/)
# No Python 3, a divisão normal SEMPRE retorna float, mesmo entre números pares.
div_int = 10 / 2
print("Conteúdo div_int:", div_int)
print("Tipo div_int:", type(div_int), "\n")

div_float = 10 / 3
print("Conteúdo div_float:", round(div_float, 2))
print("Tipo div_float:", type(div_float), "\n")


# 5. DIVISÃO INTEIRA (//)
# Corta as casas decimais e retorna apenas a parte inteira (arredonda para baixo).
div_inteira_int = 10 // 2
print("Conteúdo div_inteira_int:", div_inteira_int)
print("Tipo div_inteira_int:", type(div_inteira_int), "\n")

div_inteira_float = 10 // 3
print("Conteúdo div_inteira_float:", div_inteira_float)
print("Tipo div_inteira_float:", type(div_inteira_float), "\n")


# 6. RESTO DA DIVISÃO / MÓDULO (%)
# Retorna o que sobra de uma divisão. Muito útil para saber se um número é par ou ímpar.
resto = 10 % 3
print("Conteúdo resto:", resto)
print("Tipo resto:", type(resto), "\n")


# 7. EXPONENCIAÇÃO (**)
# Eleva o primeiro número à potência do segundo (10 elevado a 3).
exponenciacao = 10 ** 3
print("Conteúdo exponenciacao:", exponenciacao)
print("Tipo exponenciacao:", type(exponenciacao), "\n")


# ==========================================
# BÔNUS: TYPE HINTS
# ==========================================
# O ": int" é apenas uma dica visual (Type Hint). O Python continua sendo de tipagem dinâmica.
num: int = 10 
print("Conteúdo num original:", num)
print("Tipo num na declaração:", type(num), "\n")

# Mesmo com a dica dizendo que era "int", o Python permite trocar para string livremente:
num = "10"
print("Conteúdo num alterado:", num)
print("Tipo num após reatribuição:", type(num), "\n")""
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

