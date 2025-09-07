dict1 = {
    "Nome": "Gabriel",
    "Sobrenome": "Artigas",
    "Ano": 1985
}

# x = dict1["Sobrenome"]
print(dict1["Sobrenome"])

x = dict1.get("Nome")
print(x)

x = dict1.keys()
print(x)
dict1["Idade"] = 36
print(x)

x = dict1.values()
print(x)
dict1["Altura"] = 1.65
print(x)

x = dict1.items()
print(x)
dict1["Altura"] = 1.75
print(x)

if "Idade" in dict1:
    print("Sim, 'Idade' é uma das chaves deste dictionary")