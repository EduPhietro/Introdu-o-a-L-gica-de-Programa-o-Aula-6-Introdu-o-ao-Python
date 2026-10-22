#🐍 Fundamentos de Python: Guia Completo de Estudos

Bem-vindo ao repositório da Aula 6 — Introdução ao Python. Este documento consolida todos os conceitos fundamentais estudados em aula, detalhando ponto a ponto desde a arquitetura e tipagem da linguagem até as funções nativas, tratamento de erros, operadores aritméticos e exemplos práticos de código.

📑 Sumário

Tipagem Dinâmica x Tipagem Estática

Tipagem Forte x Tipagem Fraca

Variáveis: O que são?

Funções: O que são?

Tipos de Dados

Conversão de Tipo (Type Casting)

Exceptions Comuns: ValueError e TypeError

Boas Práticas de Nomeação de Variáveis

Operadores Aritméticos

Tipo de Resultados de Operações

Criador da Linguagem

O Python é uma Linguagem Interpretada

Bônus 1: Type Hints

Bônus 2: Padrão snake_case

Código Prático Completo (main.py)

Fontes e Referências

📚 Detalhamento dos Conteúdos Estudados

1) Tipagem Dinâmica (inferência) x Tipagem Estática (explícita)

Tipagem Dinâmica (Python, Ruby, JavaScript): O interpretador descobre (infere) o tipo da variável automaticamente em tempo de execução com base no valor atribuído a ela. Não é necessário declarar o tipo explicitamente no código, e uma mesma variável pode apontar para tipos diferentes ao longo do programa.

valor = 10        # O Python infere que é 'int'
valor = "Texto"   # Agora a mesma variável passa a ser 'str'


Tipagem Estática (Java, C, C++, Rust): O tipo da variável deve ser declarado explicitamente pelo programador(a) antes da compilação (ou inferido estaticamente em tempo de compilação) e não pode mudar ao longo do ciclo de vida daquela variável.

int valor = 10;
// valor = "Texto"; -> Causaria um erro de compilação!


2) Tipagem Forte x Tipagem Fraca

Tipagem Forte (Python, Java, C#): A linguagem é rigorosa quanto às operações entre tipos incompatíveis e não realiza conversões automáticas (coerções implícitas) sem sentido lógico. Por exemplo, tentar somar um texto com um número em Python ("15" + 5) gera um erro (TypeError), exigindo que você converta os dados explicitamente antes de operar.

Tipagem Fraca (JavaScript, PHP): A linguagem tenta "adivinhar" a intenção do programador e converte os tipos silenciosamente nos bastidores para evitar travar a execução. No JavaScript, por exemplo, "15" + 5 resulta na string "155", enquanto "15" - 5 resulta no número 10.

3) Variáveis: O que são?

Variáveis são espaços reservados na memória RAM do computador utilizados para guardar informações que serão lidas, manipuladas e reutilizadas durante a execução do algoritmo.

No Python: As variáveis funcionam como "etiquetas" (referências) que apontam para objetos armazenados na memória. Quando fazemos idade = 20, criamos o objeto inteiro 20 na memória e colamos a etiqueta idade nele.

4) Funções: O que são? [type(), print(), input()]

Funções são blocos de código encapsulados e reutilizáveis que executam uma tarefa específica, podendo receber dados de entrada (argumentos/parâmetros) e devolver um resultado (retorno). O Python já vem com diversas funções nativas (Built-in Functions) prontas para uso imediato:

Função

Descrição

Comportamento Principal

type(objeto)

Inspeciona um valor ou variável.

Retorna a classe/tipo do dado (ex: <class 'int'>).

print(... )

Exibe informações na saída padrão (tela/console).

Aceita múltiplos valores separados por vírgula e pula linha por padrão (\n).

input(mensagem)

Pausa o programa e lê o que o usuário digitar no teclado.

Atenção: Retorna sempre uma string (str), mesmo que o usuário digite números.

5) Tipos de Dados

Os tipos de dados primitivos/básicos fundamentais em Python determinam que tipo de operações podemos fazer com cada valor:

int (Inteiro): Números positivos, negativos ou zero, sem parte fracionária. Ex: 42, -10, 0.

float (Ponto Flutuante): Números reais que possuem casas decimais (separadas por ponto ., padrão americano). Ex: 10.5, 3.1415, -0.01.

str (String): Cadeias de caracteres (textos) delimitadas por aspas simples ('...') ou aspas duplas ("..."). Ex: "Olá, Mundo!", '123'.

bool (Booleano): Valores lógicos que representam apenas dois estados possíveis: True (Verdadeiro) ou False (Falso).

6) Conversão de Tipo (Type Casting)

Como o Python tem tipagem forte e funções como input() sempre retornam texto (str), frequentemente precisamos converter um tipo de dado em outro manualmente usando funções construtoras de tipo:

int(valor): Converte valores compatíveis para inteiro (ex: int("25") $\rightarrow$ 25 ou int(9.9) $\rightarrow$ 9).

float(valor): Converte valores compatíveis para número decimal (ex: float("10.5") $\rightarrow$ 10.5 ou float(10) $\rightarrow$ 10.0).

str(valor): Transforma números ou outros objetos em texto (ex: str(100) $\rightarrow$ "100").

bool(valor): Converte valores para True ou False (números 0 e textos vazios "" viram False; o restante vira True).

7) Exceptions (Exceções) Comuns: ValueError e TypeError

Exceções são erros detectados durante a execução do programa que interrompem o fluxo normal caso não sejam tratados:

TypeError (Erro de Tipo): Acontece quando você tenta executar uma operação ou função em um tipo de dado incompatível.

Exemplo: Tentar somar texto com número ("Idade: " + 20) ou tentar dividir duas strings ("10" / "2").

ValueError (Erro de Valor): Acontece quando o tipo passado para a função está correto, mas o conteúdo interno daquele dado não é válido para a operação.

Exemplo: int("dez") ou int("10.5"). A função int() aceita receber uma str, mas não consegue transformar letras ou pontos decimais diretamente em um número inteiro válido.

8) Boas Práticas de Nomeação de Variáveis

Criar bons nomes de variáveis torna o código legível e fácil de dar manutenção:

Seja descritivo e semântico: Prefira quantidade_alunos ou taxa_juros em vez de siglas obscuras como qa, tj ou x.

Regras obrigatórias de sintaxe:

Deve começar obrigatoriamente com uma letra (a-z, A-Z) ou sublinhado (_). Nunca comece com números (ex: 1nome é inválido).

Não pode conter espaços em branco ou caracteres especiais (@, !, -, $, %).

Não utilize palavras reservadas da linguagem Python (como if, else, for, while, def, class, return, True, False).

Evite acentuação: Embora o Python 3 suporte caracteres Unicode, a convenção universal é não usar acentos ou ç no nome de variáveis (media_calculada em vez de média_calculada).

9) Operadores Aritméticos [+, -, *, /, %, //, **]

Os operadores aritméticos permitem realizar cálculos matemáticos diretamente no código:

Operador

Nome da Operação

Descrição Prática

Exemplo

Resultado

+

Soma / Adição

Soma dois valores numéricos.

10 + 10

20

-

Subtração

Subtrai o segundo valor do primeiro.

11 - 10

1

*

Multiplicação

Multiplica dois valores.

11 * 10

110

/

Divisão Padrão

Divide o valor da esquerda pelo da direita.

10 / 2

5.0

//

Divisão Inteira

Divide e descarta a parte fracionária (casas decimais).

10 // 3

3

%

Resto (Módulo)

Retorna o resto que sobrou de uma divisão inteira.

10 % 3

1

**

Exponenciação

Eleva a base (esquerda) ao expoente (direita).

10 ** 3

1000

10) Tipo de Resultados de Operações

O tipo do valor resultante de uma expressão matemática depende tanto dos operadores quanto dos tipos de entrada:

int com int usando +, -, *, //, %, **: O resultado permanece sendo int (ex: 10 + 10 gera 20 do tipo int).

Qualquer operação com float: Se pelo menos um dos números envolvidos na conta for float, o Python promove o resultado final para float para evitar perda de precisão decimal (ex: 11 * 10.0 gera 110.0 do tipo float).

O caso especial da Divisão (/): No Python 3, o operador de divisão simples / sempre retorna um float, mesmo quando a divisão entre dois inteiros é exata (ex: 10 / 2 retorna 5.0, que é <class 'float'>).

11) Criador da Linguagem: Guido van Rossum

O Python foi idealizado e criado por Guido van Rossum no final da década de 1980 (com lançamento público em 1991), enquanto trabalhava no instituto de pesquisa Centrum Wiskunde & Informatica (CWI), em Amsterdã.

Nota de Aula / Curiosidade: Em nossas anotações de aula foi citado (Finlandês), uma confusão muito comum com Linus Torvalds (criador do Linux e do Git, que é finlandês). Na realidade, Guido van Rossum é holandês (nascido nos Países Baixos).

Origem do Nome: Ao contrário do que muitos pensam, o nome da linguagem não veio da cobra píton, mas sim de uma homenagem ao famoso grupo humorístico britânico Monty Python (Monty Python's Flying Circus), do qual Guido era fã.

12) O Python é uma Linguagem Interpretada

Uma linguagem interpretada é aquela em que o código-fonte não é traduzido diretamente para um arquivo executável binário da máquina (.exe) antes de rodar.

Quando você executa python main.py, o interpretador lê o código-fonte, compila internamente para um formato intermediário chamado bytecode e o executa instrução por instrução dentro da PVM (Python Virtual Machine).

Isso garante altíssima portabilidade (o mesmo script roda no Windows, macOS e Linux sem alterações) e agilidade no desenvolvimento e testes.

⭐ Tópicos Bônus

13) Bônus: Type Hints (Dicas de Tipo)

Introduzidas a partir do Python 3.5 (PEP 484), as Type Hints permitem anotar explicitamente qual tipo de dado uma variável, parâmetro ou retorno de função deveria ter.

Importante: As Type Hints não transformam o Python em uma linguagem estática. O interpretador ignora essas marcações em tempo de execução (permitindo que a variável mude de tipo normalmente). Elas servem para documentar melhor o código, ativar o autocompletar inteligente nas IDEs (como VS Code e PyCharm) e auxiliar ferramentas de verificação externa (como mypy ou pyright).

num: int = 10  # Anotação visual informando que 'num' é inteiro
num = "10"     # O Python continua permitindo trocar para 'str' sem dar erro!


14) Bônus: Padrão de Nomeação snake_case

Segundo a PEP 8 (o guia oficial de estilo de código do Python), todos os nomes de variáveis e funções devem ser escritos utilizando o padrão snake_case:

Todas as letras devem ser minúsculas.

Palavras compostas devem ser separadas pelo caractere sublinhado / underscore (_).

Padrão

Exemplo

Onde é usado em Python?

snake_case

soma_int, div_inteira_float

✅ Variáveis, funções e módulos (Padrão Oficial)

PascalCase

AnimalInternado, MinhaClasse

Usado apenas para nomes de Classes.

UPPER_CASE

TAXA_FIXA, PI

Usado para representar Constantes.

camelCase

somaInt, minhaVariavel

❌ Não recomendado pela PEP 8 em Python (comum em Java/JS).

💻 Código Prático Completo (main.py)

Abaixo está o código integral desenvolvido e executado durante a aula para comprovar o comportamento dos operadores aritméticos, da função type() e das Type Hints:

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
11) Criador da linguagem Guido Van Rossun (Finlandês / Holandês)
12) O Python é uma linguagem interpretada

Bonus:
13) Type Hints
14) Padrão de nomeação de variáveis snake_case

Funcoes:
    type();
    print();
    input();

Operadores aritméticos:
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
# TYPE HINTS
num: int = 10  # Type Hint
print("num na linha 95: ", type(num))
num = "10"
print("num na linha 97: ", type(num))


🔗 Fontes e Referências

Python Software Foundation. The Python Tutorial — An Informal Introduction to Python (Numbers, Text, Variables). Disponível em: https://docs.python.org/pt-br/3/tutorial/introduction.html

Python Software Foundation. Built-in Functions (print, input, type, int, float, str). Disponível em: https://docs.python.org/pt-br/3/library/functions.html

Python Software Foundation. Built-in Exceptions (TypeError, ValueError). Disponível em: https://docs.python.org/pt-br/3/library/exceptions.html

Van Rossum, G.; Warsaw, B.; Coghlan, N. PEP 8 – Style Guide for Python Code (Naming Conventions & snake_case). Disponível em: https://peps.python.org/pep-0008/

Van Rossum, G.; Lehtosalo, J.; Langa, Ł. PEP 484 – Type Hints. Disponível em: https://peps.python.org/pep-0484/

Python Software Foundation. General Python FAQ — History and Philosophy of Python. Disponível em: https://docs.python.org/pt-br/3/faq/general.html🐍 Fundamentos de Python: Guia Completo de Estudos

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
