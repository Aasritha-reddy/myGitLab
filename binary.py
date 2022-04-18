def bin_helper(n,a):
    if(len(a)==n):
        [print(i,end='') for i in a]
        print(end='\n')

        
        
    else:
        a.append('0')
        bin_helper(n,a)
        a.pop()
        a.append('1')
        bin_helper(n,a)
        a.pop()

def bin(n):
    a=[]
    bin_helper(n,a)
bin(4)
