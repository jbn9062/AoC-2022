import itertools
print(["".join(ktup) for ktup in itertools.product("ACGT", repeat=13)])