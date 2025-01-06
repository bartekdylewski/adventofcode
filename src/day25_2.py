print(sum(not any(x==y=='#' for x,y in zip(a,b)) for a,b in __import__("itertools").combinations(open("input/input25.txt").read().split("\n\n"),2)))
