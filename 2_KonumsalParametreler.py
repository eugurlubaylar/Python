def sayiTopla(n1, n2, n3=200):
    """n3' e default değer vererek kullancının iki değişken
girmesi durumunda, üçüncü değerin default değerini kullanmasını
sağladık. Eğer kullanıcı üçüncü değeride girerse default değer
yerine bu değer işleme girer. Eğer üç değerede default değer atanırsa
hiç bir parametre girilmese dahi işlem yapılır."""
    toplam = n1 + n2 + n3
    return toplam

t = sayiTopla(10, 30)
print("Toplam =", t)
    
