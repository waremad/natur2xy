#
m = 2
n = 2
hw = 10

def xy2natur(x,y):
    x,y = x+1,y+1
    out = y + (y+x-2)*(y+x-1)/2
    out -= 1
    return out

def natur2xy(n):
    n = n+1
    x = 0
    y = 0 
    while not(x*(x+1)/2 >= n):
        x += 1
    while not(x*(x-1)/2 + y == n):
        y += 1
    x -= y
    y -= 1
    return (x,y)


ls = []
for i in range(int((hw*1.5)//1)):
    ls.append([" "] * int((hw*1.5)//1))
for i in range(hw**2):
    ls[natur2xy(i)[1]][natur2xy(i)[0]] = str((i)%10)
for i in ls:
    print("".join(i))


for y in range(hw):
  for x in range(hw):
    out = xy2natur(x,y)
    print(int(out%10),end="")
  print()