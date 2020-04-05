#ikiye bölme yöntemi ile ikinci dereceden bir fonksiyonun kökünü bulma
def f(x):
    return(x**2-4*x+3)

x1=int(input("baslangic degerini gir: "))
x2=int(input("bitis degerini gir"))

if(f(x1)*f(x2)==0):
    print("tahminlerinizden biri dogru")
elif(f(x1)*f(x2)>0):
    print("bu aralıkta tek ssyida kok yoktur")
else:
    for i in range(20):
        xr=(x1+x2)/2
        if(f(xr)==0):
            print("kok :",xr)
        elif(f(x1)*f(xr)<0):
            x2=xr
        else:
            x1=xr
        print(xr)