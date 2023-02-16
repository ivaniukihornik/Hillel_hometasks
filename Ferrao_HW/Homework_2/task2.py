# 2
# You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba.
# Show it in code. Keep in mind that people with the same name can be in both companies

Eleks = ['Anna A', 'Brian B', 'Cristian C']
Toshiba = ['Brian B', 'Cesar C', 'Frank F', 'George G', 'Phil P', 'Mila M']

Toshiba.extend(Eleks)
print(f'Toshiba workers after Eleks taking over: {Toshiba}')