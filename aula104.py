import json

x = {
    "nome": "Gabriel",
    "idade": 36,
    "casado": True,
    "divorciado": False,
    "filhos": ("Arthur","Lucas"),
    "pets": None,
    "carros": [
        {"modelo": "BMW 230", "cor": "Branca"},
        {"modelo": "Ford Edge", "cor": "Preto"}
    ]
}

#print(json.dumps(x))
#print(json.dumps(x, indent = 4))
#print(json.dumps(x, indent = 4, separators=(". ", " = ")))
##y = json.dumps(x, indent = 4, separators=(". ", " = "), sort_keys=True)
y = json.dumps(x, separators=(". ", " = "), sort_keys=True)
print(y)