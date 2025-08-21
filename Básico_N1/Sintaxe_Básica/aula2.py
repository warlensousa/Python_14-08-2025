


# Usar "snake_case" para nomes de variáveis e funções;


# Tipos da dados básicos;
# int
numero = 1 
# str
palavra = "Warlen"
# float
numero_quebrado = 1.80
# Bool
verdadeiro = True
false = False


# Operadores Aritméticos;
a = 10
b = 3

print(a + b)    # 13 - Adição
print(a - b)    # 7 - Subtração
print(a * b)    # 30 - Multiplicação
print(a / b)    # 3.333... - Divisão normal
print(a // b)   # 3 - Divisão inteira
print(a % b)    # 1 - Módulo (resto da divisão)
print(a ** b)   # 1000 - Exponenciação (10³)



# Operadores de Comparação;
x = 5
y = 7

print(x == y)   # False - Igual a
print(x != y)   # True - Diferente de
print(x < y)    # True - Menor que
print(x > y)    # False - Maior que
print(x <= y)   # True - Menor ou igual a
print(x >= y)   # False - Maior ou igual a



# Operadores Lógicos;
idade = 25
tem_carteira = True

# AND - Ambos devem ser True
pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir)  # True

# OR - Pelo menos um deve ser True
tem_desconto = idade < 12 or idade > 60
print(tem_desconto)  # False

# NOT - Inverte o valor booleano
nao_pode_dirigir = not pode_dirigir
print(nao_pode_dirigir)  # False




# Operadores de Associação;
frutas = ["maçã", "banana", "laranja"]
texto = "Python é uma linguagem poderosa"

# in => está em
print("banana" in frutas)        # True
print("uva" not in frutas)       # True
print("linguagem" in texto)      # True
print("Java" not in texto)       # True


# Operadores de Identidade;
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# is => é igual, mas só se forem do mesmo objetos/compartimento...
print(a is b)        # False - Objetos diferentes
print(a is c)        # True - Mesmo objeto
print(a == b)        # True - Conteúdo igual
print(a is not b)    # True - Objetos diferentes



# Conversão de Tipos (Type Casting)
# int() 
print(int(3.14))        # 3 (trunca a parte decimal)
print(int("123"))       # 123
print(int(True))        # 1
print(int(False))       # 0

# float()
print(float(10))        # 10.0
print(float("3.14"))    # 3.14
print(float(True))      # 1.0
print(float(False))     # 0.0

# str()
# Conversões válidas (quase tudo pode ser convertido para string)
print(str(123))         # "123"
print(str(3.14))        # "3.14"
print(str(True))        # "True"
print(str([1, 2, 3]))   # "[1, 2, 3]"
print(str({"a": 1}))    # "{'a': 1}"

# bool()
# Valores que são False
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(""))         # False (string vazia)
print(bool([]))         # False (lista vazia)
print(bool({}))         # False (dicionário vazio)
print(bool(None))       # False
# Valores que são True (quase tudo mais)
print(bool(1))          # True
print(bool(0.1))        # True
print(bool("a"))        # True
print(bool([1]))        # True
print(bool({"a": 1}))   # True


# list() - Conversão para lista;
# De string (cada caractere vira um elemento)
print(list("abc"))              # ['a', 'b', 'c']
# De tupla
print(list((1, 2, 3)))          # [1, 2, 3]
# De conjunto (a ordem pode variar)
print(list({1, 2, 3}))          # [1, 2, 3] (ordem não garantida)
# De dicionário (pega apenas as chaves)
print(list({"a": 1, "b": 2}))   # ['a', 'b']
# De range
print(list(range(5)))            # [0, 1, 2, 3, 4]


# tuple() - Conversão para tupla;
# Similar à list(), mas retorna uma tupla
print(tuple([1, 2, 3]))         # (1, 2, 3)
print(tuple("abc"))              # ('a', 'b', 'c')
print(tuple({"a": 1, "b": 2}))   # ('a', 'b')


# set() - Conversão para conjunto;
# Remove duplicatas e não mantém ordem
print(set([1, 2, 2, 3, 3]))     # {1, 2, 3}
print(set("banana"))             # {'b', 'a', 'n'}
print(set((1, 2, 1, 3)))         # {1, 2, 3}


# dict() - Conversão para dicionário;
# De lista de tuplas (chave, valor)
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}
# De lista de listas (cada sublista com 2 elementos)
print(dict([['a', 1], ['b', 2]]))  # {'a': 1, 'b': 2}
# De string (não funciona diretamente)
# dict("ab")  # ValueError
# De dicionário já existente (cria cópia)
original = {'a': 1, 'b': 2}
copia = dict(original)
print(copia)  # {'a': 1, 'b': 2}



# Funções embutidas Úteis

# len() => Retorna o tamanho do objeto
print(len("12345678"))
# type() => Retorna o tipo do objeto
print(type(("Naruto")))
# id() => Retorna a identidade única do objeto
caixa1 = [1, 2, 3]
caixa2 = caixa1 # mesmo endereço;
# sum() => Soma dos elemenmtos de um inteiravel
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numeros)) # 55
# min() => menor valor e de str a letra que vem primeiro na ordem alfabetica
# max() => maior valor e str letra que vai depois ordem alfabetica;
n1 = [3, 1, 4, 2]
print(max(n1))  # 4
print(min(n1))  # 1
# Sorted(), reverse= True, key=len (por tamanho) => retorna um lista ordenada
print(sorted(numeros, reverse=True)) #decrescente

# ! tenho que estudar isso aqui ainda, pois não lembro mais akskdkkf
# isinstance() => Verifica se o objeto é uma instância de uma classe
# issubclass() - Verifica se uma classe é subclasse de outra
# callable() - Verifica se objeto é chamável
