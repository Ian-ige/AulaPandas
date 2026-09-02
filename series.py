from pandas import Series

index = ['a','b','c','d','e','f','g','h','i','j']
listaNuemrica = [0,1,2,3,4,5,6,7,8,9]
listaNomes = ["Ian","Arthur","Samuel","Jao","Jao","Jao","Jao","Jao","Jao","Jao"]
serieNomes = Series(listaNomes)
serieNumeros = Series(listaNuemrica, index = index)
somaNumeros = serieNumeros.sum()
NumerosDict = serieNumeros.to_dict()
NomesDict = serieNomes.to_dict()
print(serieNumeros)
print(serieNomes)
print(somaNumeros)
print(serieNumeros.head(6))
print(serieNumeros.tail(7))
print(NumerosDict)
print(NomesDict)