NAJMUDDİN  QURBANUGHLİ  
160401081def  readFile ( dosya adı ):
    dosya  =  açık ( dosya adı )
    list  = []
    için  hat  içinde  dosyanın . readlines ():
        line  =  line . rstrip ( ' \ n ' )
        listesi . append ( kayan nokta ( satır ))
    dosyası . kapat ()
    dönüş  listesi


def  gaussElimination ( m ):
    n  =  len ( m )
    için  I  içinde  aralığı ( n ):
        pivot ( m , n , i )
        için  j  olarak  aralık ( i  +  1 , n )
            m [ j ] = [ m [ j ] [ k ] -  m [ i ] [ k ] *  m [ j ] [ i ] /  m [ i ] [ i ] için  k  olarak  aralık ( n  +  1 )]

    eğer  m [ n  -  1 ] [ n  -  1 ] ==  0 : ValueError değerini yükseltin  ( 'hatalı format!' )

    x  = [ 0 ] *  n
    için  i  içinde  aralığı ( n  -  1 , - 1 , - 1 ):
        s  =  toplamı ( m, [ i ] [ j ] *  x [ j ] için  j  olarak  aralık ( i , n ))
        x [ i ] = ( m [ i ] [ n ] -  s ) /  m [ i ] [ i ]
    dönüş  x


def  pivot ( m , n , i ):
    max  =  0
    için  r  olarak  aralık ( i , n )
        Eğer  azami  <  abs ( m, [ r ] [ i ]):
            max_row  =  r
            max  =  abs ( m [ r ] [ i ])
    m [ i ], m [ max_row ] =  m [ max_row ], m [ i ]


def  getCoefficients ( n ; veri ):
    xiList  = [[] için  y  de  aralık ( n  +  2 )]

    için  I  içinde  aralığı ( 0 , N  +  2 ):
        için  k  olarak  aralık ( 0 , N  +  2 ):
            eğer  i  ==  0 :
                xiList [ i ]. sonda ( k  +  1 )
            başka :
                xiList [ i ]. ek (( k  +  1 ) ** ( i  +  1 ))
    dönüş  xiList


def  getSumCoefficients ( veri ):
    için  k  olarak  aralık ( len ( veri )):
        data [ k ] =  sumOfDataLen ( veri [ k ])
    dönüş  verileri


def  getAllXiYi ( n ; veri ; yi ; katsayılar ):
    Liste  = [ X  için  X  olarak  aralık ( 6 )]
    için  j  olarak  aralık ( n ):
        için  i  de  aralık ( 6 ):
            liste [ i ] + =  veri [ j ] *  katsayıları [ i ] [ j ]

    listesi . insert ( 0 , yi )
    dönüş  listesi


def  sumOfDataLen ( arr ):
    t  =  0
    için  i  de  aralık ( 10 ):
        t  + =  dizi [ i ]
    dönüş  t


def  createEquationForAllDegrees ( katsayılar , xiyi , n ):
    Liste  = [ X  için  X  olarak  aralık ( 6 )]
    w , h  =  3 , 2

    # tüm dereceler için denklemenizilım
    için  i  de  aralık ( 6 ):
        Matris  = [[ 0  için  x  olarak  aralık ( a ]) için  y  de  aralık ( h )]
        için  k  olarak  aralık ( h ):
            için  l  olarak  aralık ( a ):
                eğer  k  ==  0 :
                    eğer  k  ==  0  ve  l  ==  0 :
                        matris [ k ] [ l ] =  n
                    başka :
                        için  z  olarak  aralık ( len ( katsayıları )):
                            Eğer  katsayıları [ Z ] de  matris [ k ]:
                                geçmek
                            başka :
                                matris [ k ] [ l ] =  katsayılar [ z ]
                                mola
                    Eğer  l  == ( ağırlık  -  1 :)
                        matris [ k ] [ l ] =  xiyi [ k ]
                başka :
                    için  z  olarak  aralık ( len ( katsayıları )):
                        Eğer  katsayıları [ Z ] de  matris [ k ]:
                            geçmek
                        elif  matrisi [ k  -  1 ] [ l ] ==  katsayılar [ z ] veya  matris [ k  -  1 ] [ l ] >  katsayıları [ z ]:
                            geçmek
                        başka :
                            Eğer  katsayıları [ z ] >  matris [ k ] [ l  -  1 ]:
                                matris [ k ] [ l ] =  katsayılar [ z ]
                                mola
                    Eğer  l  == ( ağırlık  -  1 :)
                        matris [ k ] [ l ] =  xiyi [ k ]

        w  + =  1
        h  + =  1
        list [ i ] =  matris
    dönüş  listesi


def  standartEstimateError ( veri ; liste ):
    arr  = []
    val  =  0
    için  k  olarak  aralık ( 1 , len ( liste ) +  1 ):
        için  i  içinde  aralığı ( len ( veri )):
            seeVal =  veri [ i ]
            için  j  olarak  aralık ( k  +  1 ):
                seeVal  =  seeVal  - ( liste [ k  -  1 ] [ j ] * (( i  +  1 ) **  j ))
            val  + =  seeVal  **  2
        val  = ( val  / ( len ( veri ) - ( k  +  1 ))) **  .5
        arr . append ( val )
    dönüş ( arr )


def  getOptimalValue ( liste ):
    dönüş  min ( aralık ( len ( liste )), anahtar = liste . __getitem__ )


def  granularData ():
    data  =  readFile ( "içinde.txt" )
    için  I  içinde  aralığı (( len ( veri ) -  9 )):
        yığın  =  veri [ i : i  +  10 ]

        n  =  len ( yığın )
        yi  =  toplam ( yığın )
        rawCoefficients  =  getCoefficients ( n , yığın )
        xiyi  =  getAllXiYi ( n , yığın , yi , ham Katsayılar )
        katsayılar  =  getSumCoefficients ( rawCoefficients )

        equationList  =  createEquationForAllDegrees ( katsayılar , xiyi , n )

        çözeltiler  = [ X  için  X  olarak  aralık ( 6 )]
        için  j  olarak  aralık ( len ( çözümler )):
            çözümler [ j ] =  gaussElimination ( equationList [ j ])

        oranlar  =  standartEstimateError ( yığın , çözümler )
        minIndex  =  getOptimalValue ( oranlar )
        print ( f " { i  +  1 } - { i  +  10 } aralığındaki odalar için { minIndex  +  1 } . derece polinom en uygun, hata miktari:"
              f " { oranlar [ minIndex  -  1 ] } " )

        f  =  açık ( 'sonuc.txt' , 'a' )
        f . yazma ( " \ n " )
        f . write ( f " { i  +  1 } - { i  +  10 } aralığındaki odalar için { minIndex  +  1 } . derece polinom en uygun, hata miktari:"
                f " { oranlar [ minIndex  -  1 ] } " )
        f . kapat ()


def  main ():
    data  =  readFile ( "içinde.txt" )
    n  =  len ( veri )
    yi  =  toplam ( veri )
    rawCoefficients  =  getCoefficients ( n ; veri )
    xiyi  =  getAllXiYi ( n ; veri ; yi ; ham Katsayılar )
    katsayılar  =  getSumCoefficients ( rawCoefficients )

    equationList  =  createEquationForAllDegrees ( katsayılar , xiyi , n )

    çözeltiler  = [ X  için  X  olarak  aralık ( 6 )]
    için  i  içinde  aralığı ( len ( çözümler )):
        çözümler [ i ] =  gaussElimination ( equationList [ i ])

    f  =  açık ( 'sonuc.txt' , 'w' )
    için  j  olarak  aralık ( len ( çözümler )):
        f . yazma ( f " { j  +  1 } .derece => { str ( çözümler [ j ]) } \ n " )
    f . kapat ()

    oranlar  =  standartEstimateError ( veriler ; çözümler )

    f  =  açık ( 'sonuc.txt' , 'a' )
    f . yazma ( " \ n \ n " )
    için  m  olarak  aralık ( len ( çözümler )):
        f . yazma ( f " { m  +  1 } .derece polinom için standart tahmini hata => { str ( oranlar [ m ]) } \ n " )
    f . kapat ()

    minIndex  =  getOptimalValue ( oranlar )
    print ( f "Tüm bölgelerde için en uygun polinom: { minIndex  +  1 } . derece polinomdur, hata miktari: { oranlar [ minIndex  -  1 ] } " )

    f  =  açık ( 'sonuc.txt' , 'a' )
    f . yazma ( " \ n \ n " )
    f . write ( f "Tüm alanlarda için en uygun: => { ( minIndex  +  1 ) } . derece polinomdur \ n " )
    f . kapat ()

    granularData ()


eğer  __name__  ==  "__main__" :
    ana ()


