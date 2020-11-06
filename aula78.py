

times = ('palmeiras','corinthias','santos','sao paulo','vasco', 'flamengo','curitiba')

for indice in times:
    print(indice)
print(times[:5])
print(times[5:])
print(sorted(times))
print(len(times))
print(f'vasco esta na posição {times.index("vasco") + 1}ª')
