def capitalize(names: list[str]) -> list[str]:
    return list(map(Solve, names))
def Solve(name: str) -> str :
    partitionName = name.split()
    for item in range(len(partitionName)):
        partitionName[item] = partitionName[item].capitalize()
    return " ".join(partitionName)
# print(capitalize(['ali', 'REYHANEH', 'aMIR', 'AMIR abbas', 'Fatemeh Zahra']))