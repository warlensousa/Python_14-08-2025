

# Indentação => 




# Exibir valores no console;
# sep: Separador entre valores;
print(24, 8, 2002, sep="/")

# end: Vai a adicionar algo no final dos caracter imposto no print e vai pegar o print abaixo e colocar na mesma linha;
print("Linha 1",  end="!")
print("Linha 2")


# input: Lê dados do usuário. Sempre vai retornar uma str (String);
# type(): Vai verificar o tipo;
nome = input("Digite seu nome: ")
print(f"{type(nome)}: {nome}")

# Ele ta convertendo a return (saida) que seria o padrão (str) para int (inteiro)
idade = int(input("Digite sua idade: "))
print(f"{type(idade)}: {idade}")


# Acessa a documentação de objetos.
# Como do exemplo abaixo: Vai mostrar a documentação do objeto String
help(str)


#!ESTUDAR DEPOIS
# file e flush do print() 

# Serve para explorar na hora do desenvolvimento consultando métodos e atributos de um objeto!
palavra = {"Naruto"}
print(dir(palavra))


