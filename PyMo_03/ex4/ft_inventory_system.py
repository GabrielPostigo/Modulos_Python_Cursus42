import sys

dc = {}

lis = sys.argv[1:]

for i in lis:
    dc.update(i)

print("Diccionario:", dc)
