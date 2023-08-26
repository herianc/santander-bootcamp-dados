# Introdução ao Python
`dir()` - comando que lista os métodos de um objeto ou o escopo atual do programa

`help(print)` - comando que mostra os textos de ajuda sobre módulo, função, classe, método ou variável. 

## Boas práticas em Python

- Variáveis não constantes são escritas em snake_case 
- Variáveis com nomes sugestivos (Evitar nomes genéricos como x ou y)
- Nomes de variáveis constantes (ou seja, imutáveis) em maiúsculo. Ex: `LIMITE_VELOCIDADE = 40`

## Strings e métodos úteis 

```python 
curso = "pYtHon"

curso.upper() # deixa todos os caracteres da string maíusculos
curso.lower() # deixa todos os caracteres da string minúsculos
curso.title() # a primeira letra fica em maiúsculo e o resto em minúsculo

curso = "   Python  "

curso.strip() # remove os espaços em branco da string ou um caracter passado como parametro. 
curso.lstrip() # remove o espaço em branco à esquerda da string
curso.rstrip() # remove os espaços em branco à direita da string 

curso = "python"

curso.center(10, '#') # centraliza a string e a envolve de sinais de sua preferência.
".".join(curso) # separa a string com um caractere de preferência

```

# Interpolação de variáveis 

formatação de variáveis em strings (_old style %, .format e f strings_)

f strings é o método mais utilizado de interpolação de variáveis. 

### Strings de múltiplas linhas 
```python
mensagem = f"""
Oi, eu sou o Goku!
Sou um sayajin e gosto de treinar artes marciais. 
"""
```

## Tipo de dado Set 

Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável 

```python
set([1,2,3,1,3,4]) # {1,2,3,4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(["palio", "gol", "celta", "palio"]) # {"gol", "celta", "palio"}

# também pode ser declarado como
linguagens = {"python", "java", "python"} # {"python", "java"}

```

O set não mantém a ordem dos seus itens, pode mudar ocasionalmente. Sets não suportam indexação e fatiamento, neste caso é necessário converter o conjunto para lista. 

### Enumerate

Função usada para saber o índice do objeto dentro de um laço __for__ 
```python
carros = {'gol', 'celta', 'palio'}

for indice, carro in enumerate(carros):
	print(f'{ìndice}: {carros}')
```

### Métodos de set 

```python
# UNIÃO DE DOIS CONJUNTOS
conjunto_a = {1,2}; conjunto_b = {3,4}

conjunto_a.union(conjunto_b) # {1,2,3,4}

# INTERSEÇÃO 
conjunto_a = {1,2,3}; conjunto_b = {2,3,4}

conjunto_a.intersection(conjunto_b) # {2,3}

# DIFERENÇA
conjunto_a = {1,2,3}; conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

# DIFERENÇA SIMÉTRICA
conjunto_a = {1,2,3}; conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) # {1,4}

# SUB CONJUNTO (is sub set?)
conjunto_a = {1,2,3}; conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

# SUPER SET (is super set?)
conjunto_a = {1,2,3}; conjunto_b = {4,1,2,5,6,3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True

# CONJUNTO DISJUNTO (is disjoint)
conjunto_a = {1,2,3,4,5}; conjunto_b = {6,7,8,9}; conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False
```


Outros métodos 

```python 
# ADIÇÃO DE ELEMENTOS
sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

# LIMPAR O CONJUNTO
sorteio.clear() # {}

sorteio.copy()

# DESCARTAR 
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.discard(1) #{2,3,4,5,6,7,8,9,0}
numeros.discard(45) #{2,3,4,5,6,7,8,9,0} não dá erro

# POP
numeros.pop() # 0
numeros.pop() # 1

numeros # {2,3,4,5,6,7,8,9}

# REMOVE
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros.remove(0)
numeros.remove(45) #DÁ ERRO

numero # {1,2,3,1,2,4,5,5,6,7,8,9}
```

### Dicionários 

Conjunto não ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. 

Também é possível colocar dicionários aninhados 

```python 
{}.copy() # copia um dicionário

{}.fromkeys(lista, valor_associado) # cria chaves sem valores a partir de uma lista

{}.get("chave") # "pega" o valor da chave passada no parametro. Caso não a chave não exista, retorna None

{}.get("chave","valor") #é possivel associar um valor caso a chave não exista

{}.items() # retorna uma lista de tuplas (chave, valor) de todas as chaves

{}.keys() # retorna uma lista com todas as chaves

{}.pop() # remove um valor e o retorna 

{}.setdefault("chave", "valor") #adiciona um valor caso ele não exista, caso exista ele não muda

{}.update(novo_dicionario) # atualiza o dicionário com chaves de nomes iguais
```

### Funções 

Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões.  Programar baseado em funções, __é o mesmo que dizer que estamos programando de maneira estruturada.__

Funções em python podem retornar mais de um valor, diferente de outras linguagens. 

### Args e kwargs 

Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos, o método recebe os valores como tupla e dicionário respectivamente. 

### Objetos de primeira classe 
Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. Com isso, podemos __atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados__ e usar como valor de retorno para uma função (closures). 

### Escopo local e escopo global

Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto, alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave __global__, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global. __Não é uma boa prática, deve ser evitada.__  

