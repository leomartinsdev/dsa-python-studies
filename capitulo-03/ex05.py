a1 = 1
b1 = 2
c1 = True
d1 = False

print(a1 > b1 and c1 or d1)
# Isso seria: false and c1 or d1
# False and True or False
# False or False
# False

a2 = 10
b2 = 3
c2 = False
d2 = True

print(a2 > b2 and c2 or d2)
# Isso seria: false and c2 or d2
# True and False or True
# False or True
# True

a3 = 5
b3 = 1
c3 = True
d3 = True

print(a3 > b3 and c3 or d3)
# Isso seria: True and c3 or d3
# True and True or True
# True or True
# True
