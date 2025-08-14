# Python_14-08-2025
Começando os estudos em Python a partir da data: 14/08/2025 e ver em quanto tempo consigo um emprego ou estágio!

# Guia de estudos Python do Básico ao Avançado (Obs: SEM CURSOS OU PROFESSOR/TUTOR... USANDO APENAS INTELIGÊNCIA ARTIFICIAL PARA APRENDIZAGEM)
# Nivel Básico 1;

    * Sintaxe básica: Indentação, comentários (#, """docstring"""), print(), input(), help(), dir()
    * Variáveis: Convenções de nome (snake_case), tipos de dados (int, float, str, bool)
    * Operadores:
        - Aritméticos: +, -, *, /, // (divisão inteira), % (módulo), ** (exponenciação)
        - Comparação: ==, !=, <, >, <=, >=
        - Lógicos: and, or, not
        - Associação: in, not in
        - Identidade: is, is not
        - Atribuição: =, +=, -=, *=, /=, etc.

    * Conversão de tipos: int(), float(), str(), bool(), list(), tuple(), set(), dict()
    * Funções embutidas úteis:
        - len(), type(), id(), sum(), min(), max(), sorted()
        - abs(), round(), isinstance(), issubclass()
        - bin(), oct(), hex() (conversões numéricas)
        - chr(), ord() (caracteres Unicode)
        - hash() (hash de objetos)
        - callable() (verifica se objeto é chamável)

    * Strings:
        - Indexação e fatiamento: s[0], s[1:5], s[::-1] (reverso)
    * Métodos:
        - Transformação: upper(), lower(), title(), capitalize(), swapcase()
        - Limpeza: strip(), lstrip(), rstrip()
        - Substituição e divisão: replace(), split(), rsplit(), splitlines(), partition(), rpartition()
        - Busca: find(), rfind(), index(), rindex(), count()
        - Verificação: startswith(), endswith(), isalnum(), isalpha(), isdigit(), isdecimal(), isnumeric(), isspace(), isidentifier()
        - Formatação: center(), ljust(), rjust(), zfill(), format_map()
    * Formatação:
        - f-strings (f"Valor: {x}"),
        - str.format() ("{}".format(x)),
        - Formatação com % (antigo)
    * Unicode e encoding: encode() (para bytes), decode() (bytes para string), erros de encoding

    * Listas:
        - Criação, acesso, fatiamento: [], list(), [1, 2, 3], lista[0], lista[1:3]
    * Métodos:
        - Modificação: append(), extend(), insert(), remove(), pop(), clear()
        - Informação: index(), count()
        - Ordenação: sort() (com key= e reverse), reverse()
        - Cópia: copy() (shallow copy)
    * List comprehension: [x*2 for x in range(10)], com condicional


    * Tuplas:
        - Imutabilidade: (), tuple()
        - Métodos: count(), index()

    * Sets (Conjuntos):
        - Criação: {} (não vazio), set()
    * Operações:
        - União: union() ou |
        - Interseção: intersection() ou &
        - Diferença: difference() ou -
        - Diferença simétrica: symmetric_difference() ou ^
    * Métodos:
        - Adicionar/remover: add(), update(), remove(), discard(), pop(), clear()
        - Verificação: isdisjoint(), issubset() (ou <=), issuperset() (ou >=)

    * Controle de Fluxo:
    * Condicionais: if, elif, else
    * Loops:
        - for: iterar sobre sequências
        - while: loop condicional
        - Controle: break, continue, pass
        - Cláusula else em loops (executa se não houve break)
    * Funções para iteração:
        - range(): gera sequências numéricas
        - enumerate(): retorna índice e valor
        - zip(): combina iteráveis
        - any(), all(): verificam se algum/todos os elementos são True
    
    * Funções Básicas:
        - Definição: def nome_funcao(parametros):
        - Parâmetros: posicionais, padrão (default)
        - Retorno: return (pode retornar múltiplos valores)
        - Escopo: global, nonlocal (em closures), local
        - Documentação: docstrings ("""Explicação""")