minhaTupla = ("Gabriel", "Danny", "Arhur")
meuIt = iter(minhaTupla)

print(next(meuIt))
print(next(meuIt))
print(next(meuIt))

fruta = "banana"
meuIt2 = iter(fruta)
print(next(meuIt2))
print(next(meuIt2))
print(next(meuIt2))
print(next(meuIt2))
print(next(meuIt2))
print(next(meuIt2))


for x in minhaTupla:
    print(x)
