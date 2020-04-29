def div(x):
    if '/' not in x:
        return x
    else:
        x=' '+x+' '
        while '/' in x:
            c=['+','-','x','/']
            a=x.find('/')
            e=''
            p=1
            pp=''
            for d in x[a+1:]:
                if d not in c:
                    e=e+d
                    p=p+1
                else:
                    if p!=1:
                        break
                    else:
                        pp=d
                        continue
            f=''
            for d in x[a-1:0:-1]:
                if d not in c:
                    f=f+d
                else:
                    break
            f=f[::-1]
            z=float(f)/float(e)
            x=x.replace(f+'/'+pp+e,pp+str(z))
        return x.lstrip().rstrip()

def mul(x):
    if 'x' not in x:
        return x
    else:
        x=' '+x+' '
        while 'x' in x:
            c=['+','-','x','/']
            a=x.find('x')
            e=''
            p=1
            pp=''
            for d in x[a+1:]:
                if d not in c:
                    e=e+d
                    p=p+1
                else:
                    if p!=1:
                        break
                    else:
                        pp=d
                        continue
            f=''
            for d in x[a-1:0:-1]:
                if d not in c:
                    f=f+d
                else:
                    break
            f=f[::-1]
            z=float(f)*1.0*float(e)
            x=x.replace(f+'x'+pp+e,pp+str(z))
        return x.lstrip().rstrip()



def addsub(x):
    if '+' or '-' in x:
        x=x.replace('--','+')
        if x[0]=='+':
            x=x[1:]
        x=x.replace('-','+-')
        y=x.split('+')
        p=[]
        q=[]
        for r in y:
            if  '-' in r:
                p.append(float(r[1:]))
            if '-' not in r and r!='':
                q.append(float(r))
        h=0
        for e in p:
            h=h+e
        w=0
        for f in q:
            w=w+f
        return str(w-h)
    else:
        return x

def smply(x):
    x=x.replace('--','+')
    x=x.replace('-+','-')
    x=x.replace('+-','-')
    y=div(x)
    if y!=x:
        print '=> ',y
    z=mul(y)
    if z!=y:
        print '=> ',z
    zz=addsub(z)
    if zz!=z:
        print '=> ',zz
    print '\tANS:- ',zz



def solve(x):
    x=x.replace('[','(').replace(']',')').replace('{','(').replace('}',')')
    if '(' not in x:
        smply(x)
    else:
        while '(' in x:
            a=x.find('(')
            e=''
            while e=='':
                for c in range(a+1,len(x)):
                    if x[c]==')':
                        e=x[a+1:c]
                        break
                    elif x[c]=='(':
                        a=c
                        break


            
            f=div(e)
            if f!=e:
                print '=> ',x.replace(e,f)
            g=mul(f)
            if g!=f:
                print '=> ',x.replace(e,g)
            p=g.replace('--','+')
            if p!=g:
                print '=> ',x.replace(e,p)
            q=p.replace('+-','-')
            if q!=p:
                print '=> ',x.replace(e,q)
            r=q.replace('-+','-')
            if r!=q:
                print '=> ',x.replace(e,r)
            h=addsub(r)
            if h!=r:
                print '=> ',x.replace(e,h)
            x=x.replace(e,h)
            x=x.replace('('+h+')',h)
            print '=> ',x
        smply(x)
        
        
           
        

    
    
a='23-[4x8.5-{6x9/2+(4/8)+7}-1]/5'
b='5x[5+6x{7x8+9/5}]/9-8/2'
c='[126+{52x13+8/38-(-100/13)}]'
d='5x6+6.2-8/4.0'
e='-2x(-7)x(-5)'
f='8-2+3'
print f
print
print solve(f)
        
    
    

                
        
