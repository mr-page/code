from threading import local


local p,i,j
p = [[],[],[],[],[]]
i = 0
j = 0
def q():
    global p,i,j
    p[i][j]='#'
    print(p)