#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#def get_vector():
x = [1,5,7]
y = [0,1,2]
def get_average(vector): #Funkcja obliczająca średnią wektora, pobiera jako parametr wektor

    avg = sum(vector)/len(vector) #Obliczenie średniej polega na zsumowaniu danych przy pomocy wbudowanej fukcji
                                    # sum() wektorze oraz podzieleniu ich przez długość wektora otrzymanej z wbudowanej funkcji len()
    return avg                          #funkcja zwarca obliczoną średnią

def get_product(vector1, vector2): #Fukcja obliczająca iloczyn mnożenia dwóch wektrów pobiera jako parametry dwa wektory

    product = []                   #Utworzenie pustej listy do przechowywania kolejno obliczanych wyników operacji mnożenia wektorów

    for x in range(len(vector1)):   #Pętla iterująca przez elementy wektora1 na podstawie długości jednego z nich
        product.append(vector1[x] * vector2[x]) #(oba wektory muszą mieć identyczną długość wiec bez różnicy długość którego wektora będzie obliczana)
                                                    #dodawanie do listy wyniku mnożenia wektorów
    return product

def get_trendline(vector_x, vector_y):  #Główna funkcja obliczająca parametry linii trendu
                                            #zmienne ułatwiające obliczanie linii trendu oraz poprawiające czytelność kodu
    xy_vector = get_product(vector_x, vector_y)
    xx_vector = get_product(vector_x, vector_x)
    x_average = get_average(vector_x)
    y_average = get_average(vector_y)
    vector_length = len(vector_x)

    a = (sum(xy_vector) - (vector_length * x_average * y_average))/(sum(xx_vector) - vector_length * (x_average) ** 2)
    b = y_average - (a * x_average)

    if b < 0:   #Rozrożnienie dodatniego i ujemnego parametru b w celu poprawnego wypisania wyniku
        print("Obliczona funkcja liniowa ma wzór y = {:.2f}x {:.3f}".format(a, b))
    else:
        print("Obliczona funkcja liniowa ma wzór y = {:.2f}x + {:.3f}".format(a, b))


get_trendline(x,y)