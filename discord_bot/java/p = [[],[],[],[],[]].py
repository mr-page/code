global p,i,j
p = [[],[],[],[],[]]
i = 0
j = 0
def q():
    global p,i,j
    new_func()
    print(p)

def new_func():
    p[i][j]='#'
while i in range(5):    
    j = 0
    while j in range(4):
        p[i].append('.')
        j = j +1
    i = i +1
print(p)

i = 2
j = 2
n = 1
#while i*j < 16:
#    j = j +n
#    q()
#    n = 0 - (n +1)
#    i = i +n
#    q()
#    n = 0 - (n +1)