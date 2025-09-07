import json

x = {
    "nome": "Gabriel",
    "idade": 36,
    "cidade": "Sao Paulo"
}

y = json.dumps(x)

print(y)
print(type(x))
print(type(y))

import json

x = {
    "nome": "Gabriel",
    "idade": 36, 
    "cidade": "São Paulo"
}

y = json.dumps(x)

print(y)
print(type(x))
print(type(y))

print(json.dumps({"nome": "Gabriel", "idade": 36}))
print(json.dumps(["maça", "bananas"]))
print(json.dumps(("maça", "bananas")))
print(json.dumps("Ola"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
