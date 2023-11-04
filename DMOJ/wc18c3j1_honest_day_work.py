paint = int(input())
badge = int(input())
sell = int(input())

amount = (paint // badge) * sell + (paint % badge)

print(amount)
