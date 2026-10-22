# 🐍 Fundamentos de Python: Guia de Estudos e Operadores

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
