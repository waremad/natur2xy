#
m = 2
n = 2
hw = 15

def xy2natur(x,y):
    out = y + (y+x-2)*(y+x-1)/2
    out = int(out%10)
    return out

def natur2xy(n):
    x = 0
    y = 0 
    while not(x*(x+1)/2 >= n):
        x += 1
    while not(x*(x-1)/2 + y == n):
        y += 1
    x -= y-1
    return (x,y)


ls = []
for i in range(int((hw*1.5)//1)):
    ls.append([" "] * int((hw*1.5)//1))
for i in range(hw**2):
    ls[natur2xy(i+1)[1]-1][natur2xy(i+1)[0]-1] = str((i+1)%10)
for i in ls:
    print("".join(i))

    
"""
for i in range(hw):
  for j in range(hw):
    y = i + 1
    x = j + 1
    out = xy2natur(x,y)
    print(out,end="")
  print()
"""