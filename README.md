#🐍 Fundamentos de Python: Guia Completo de Estudos

Este documento consolida os conceitos fundamentais estudados sobre a linguagem Python, detalhando desde a arquitetura e tipagem da linguagem até a sintaxe básica e operadores.

📚 1. Conceitos Fundamentais da Linguagem

1) Tipagem Dinâmica (inferência) x Tipagem Estática (explícita)

Tipagem Dinâmica (Python): O interpretador infere o tipo da variável automaticamente em tempo de execução. Não é necessário declarar o tipo (ex: idade = 25 o Python já sabe que é um inteiro).

Tipagem Estática (Java, C, C++): Exige que o tipo de dado da variável seja declarado explicitamente antes da compilação e não pode mudar (ex: int idade = 25;).

2) Tipagem Forte x Tipagem Fraca

Tipagem Forte (Python): A linguagem é rigorosa e não faz conversões automáticas (coerções implícitas) que não façam sentido lógico. Por exemplo, tentar somar uma string com um inteiro ("1" + 2) resultará em um erro de tipo.

Tipagem Fraca (JavaScript, PHP): A linguagem tenta adivinhar e converter automaticamente os tipos para forçar a operação a funcionar (ex: em JS, "1" + 2 resulta na string "12").

3) Variáveis: O que são?

Variáveis são espaços reservados na memória do computador utilizados para armazenar dados que podem ser lidos, alterados e manipulados durante a execução de um programa. Em Python, funcionam como "etiquetas" que apontam para valores na memória.

4) Funções: O que são?

São blocos de código reutilizáveis projetados para realizar uma tarefa específica. Evitam a repetição de código.

Funções Nativas (Built-in) Estudadas:

type(valor): Retorna o tipo de dado de uma variável ou valor.

print("texto"): Exibe dados e mensagens no console para o usuário ver.

input("texto"): Pausa a execução e aguarda o usuário digitar um valor no teclado. O retorno é sempre uma string (str).

5) Tipos de Dados

Representam a natureza da informação armazenada. Os principais no Python são:

int: Números inteiros (ex: 10, -5)

float: Números com casas decimais / ponto flutuante (ex: 10.5, 3.14)

str: Strings, textos ou caracteres delimitados por aspas (ex: "Olá", 'Python')

bool: Booleanos, indicam verdadeiro ou falso (True ou False)

6) Conversão de Tipo (Type Casting)

É o processo de transformar um tipo de dado em outro de forma explícita utilizando funções construtoras, como: int(), float(), str().

Exemplo: int("10") converte o texto "10" para o número inteiro 10.

7) Exceptions (Exceções) Comuns

Erros que ocorrem em tempo de execução quando algo dá errado na lógica.

TypeError: Ocorre quando uma operação é aplicada a um tipo de dado inadequado (ex: tentar multiplicar duas strings).

ValueError: Ocorre quando uma função recebe um argumento do tipo certo, mas com um valor inadequado (ex: int("abacaxi") - a função espera uma string, mas não consegue converter letras em números inteiros).

8) Boas Práticas de Nomeação de Variáveis

Utilizar nomes descritivos e claros (ex: salario_base em vez de sb).

Não utilizar caracteres especiais, acentos ou espaços.

Não iniciar nomes de variáveis com números (ex: 1produto).

Evitar o uso de palavras reservadas da linguagem (como if, for, class).

9) Operadores Aritméticos

Símbolos utilizados para realizar operações matemáticas.

+ : Soma

- : Subtração

* : Multiplicação

/ : Divisão padrão

//: Divisão inteira (descarta as casas decimais)

% : Resto da divisão (módulo)

**: Exponenciação (potência)

10) Tipo de Resultados de Operações

A combinação de tipos em operações gera comportamentos específicos:

Inteiro com Inteiro na divisão padrão (/) sempre resulta em float.

Se houver pelo menos um float na operação matemática (+, -, *), o resultado final será promovido para float para não haver perda de precisão.

A divisão inteira (//) entre inteiros retorna int.

11) História: O Criador da Linguagem

O Python foi criado pelo programador Guido van Rossum, que começou a desenvolver a linguagem no final dos anos 1980 no CWI (Centrum Wiskunde & Informatica).

Nota Histórica: Guido van Rossum é holandês (muitas vezes confundido com finlandês por causa de Linus Torvalds, criador do Linux). O nome "Python" foi inspirado no grupo de comédia britânico Monty Python.

12) O Python é uma Linguagem Interpretada

Isso significa que o código fonte escrito em .py é lido, traduzido e executado linha a linha por um "interpretador" (a Máquina Virtual Python - PVM) em tempo real, sem a necessidade de um passo prévio de compilação que transforme tudo em código de máquina de uma só vez (como acontece no C++ ou Java).

⭐ Bônus e Práticas

13) Type Hints (Dicas de Tipo)

Embora Python seja de tipagem dinâmica, a partir da versão 3.5 a linguagem introduziu o suporte a Type Hints. Servem como anotações visuais para ajudar o programador e o editor de código (IDE) a saberem qual tipo é esperado em uma variável ou função, melhorando a documentação e evitando bugs.

Exemplo: idade: int = 25

14) Padrão de Nomeação: snake_case

O Python possui um guia oficial de estilo chamado PEP 8. Nele, a recomendação oficial para o nome de variáveis e funções é utilizar o padrão snake_case, onde todas as letras são minúsculas e os espaços são substituídos por sublinhados (_).

Incorreto/Não recomendado em Python: minhaVariavel, MinhaVariavel

Correto: minha_variavel_de_teste, nome_completo

💻 Exemplo Prático de Código (Operadores e Tipos)

# --- SOMA ---
soma_int = 10 + 10
soma_float = 10.0 + 10.1
print("Conteúdo soma_int: ", soma_int, " | Tipo: ", type(soma_int))
print("Conteúdo soma_float: ", soma_float, " | Tipo: ", type(soma_float), "\n")

# --- SUBTRAÇÃO ---
sub_int = 11 - 10
sub_float = 10.3 - 10.1
print("Conteúdo sub_int: ", sub_int, " | Tipo: ", type(sub_int))
print("Conteúdo sub_float: ", sub_float, " | Tipo: ", type(sub_float), "\n")

# --- MULTIPLICAÇÃO ---
mult_int = 11 * 10
mult_float = 11 * 10.0
print("Conteúdo mult_int: ", mult_int, " | Tipo: ", type(mult_int))
print("Conteúdo mult_float: ", mult_float, " | Tipo: ", type(mult_float), "\n")

# --- DIVISÃO (Retorna sempre float) ---
div_int = 10 / 2
div_float = 10 / 3
print("Conteúdo div_int: ", div_int, " | Tipo: ", type(div_int))
print("Conteúdo div_float: ", div_float, " | Tipo: ", type(div_float), "\n")

# --- DIVISÃO INTEIRA ---
div_inteira_int = 10 // 2
div_inteira_float = 10 // 3
print("Conteúdo div_inteira_int: ", div_inteira_int, " | Tipo: ", type(div_inteira_int))
print("Conteúdo div_inteira_float: ", div_inteira_float, " | Tipo: ", type(div_inteira_float), "\n")

# --- RESTO DA DIVISÃO (Módulo) ---
resto = 10 % 3
print("Conteúdo resto: ", resto, " | Tipo: ", type(resto), "\n")

# --- EXPONENCIAÇÃO ---
exponenciacao = 10**3
print("Conteúdo exponenciacao: ", exponenciacao, " | Tipo: ", type(exponenciacao), "\n")

# --- BÔNUS: TYPE HINTS ---
num: int = 10  # Type Hint indicando inteiro
print("num na linha declarada: ", type(num))
# O Python permite a reatribuição devido à tipagem dinâmica:
num = "10"
print("num após receber string: ", type(num))
 🐍 Fundamentos de Python: Guia de Estudos e Operadores

Resumo dos conceitos fundamentais de Python estudados, abrangendo tipagem, operadores aritméticos, funções nativas e exemplos práticos de código.

---

## 📚 Sumário dos Conteúdos

1. **Tipagem dinâmica (inferência)** vs **Tipagem estática (explícita)**
2. **Tipagem forte** vs **Tipagem fraca**
3. **Variáveis**: O que são e como funcionam
4. **Funções nativas essenciais**: `type()`, `print()`, `input()`
5. **Tipos de dados** básicos
6. **Conversão de Tipo** (*Type Casting*)
7. **Exceções comuns**: `ValueError`, `TypeError`
8. **Boas práticas de nomeação de variáveis** (ex: `snake_case`)
9. **Operadores aritméticos** (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
10. **Tipo de resultados de operações**
11. **Histórico**: Criado por Guido Van Rossum (Finlandês)
12. **Natureza da linguagem**: O Python é uma linguagem interpretada

---

## 🛠️ Funções Principais

* `type()`: Retorna o tipo de dado de um objeto ou variável.
* `print()`: Exibe dados formatados na saída padrão (console).
* `input()`: Recebe dados inseridos pelo usuário via teclado (retornando sempre uma `str`).

---

## ➗ Operadores Aritméticos

| Operador | Descrição | Exemplo |
| :---: | :--- | :--- |
| `+` | Soma | `10 + 10` |
| `-` | Subtração | `11 - 10` |
| `*` | Multiplicação | `11 * 10` |
| `/` | Divisão (retorna `float`) | `10 / 2` |
| `//` | Divisão Inteira | `10 // 3` |
| `%` | Resto da divisão (Módulo) | `10 % 3` |
| `**` | Exponenciação (Potência) | `10 ** 3` |

---

## 💻 Código de Demonstração e Prática

Abaixo encontra-se o script utilitário contendo a implementação e validação dos operadores aritméticos e do comportamento de variáveis em Python:

```python
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

# DIVISAO (Sempre retorna float em Python 3)
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
exponenciacao = 10 ** 3
print("Conteúdo exponenciacao: ", exponenciacao)
print("Tipo exponenciacao: ", type(exponenciacao), "\n")
