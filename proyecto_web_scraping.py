import requests
import bs4
#base de la pagina para cambiar de paginas con el .format
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
libros_ato_rating = []

#loop que nos ayuda a iterar por las 50 paginas de la pagina de libros
for n in range (1,51):
    #creamos el url de la pagina n (actual)
    url_pagina = requests.get(url_base.format(n))
    #creamos la sopa para poder jugar con los valores del codigo html de la pagina n
    sopa = bs4.BeautifulSoup(url_pagina.text,'lxml')

    libros = sopa.select('.product_pod') # como libros es una lista ahora podemos iterar en cada libro y tomar el rating y el titulo de cada libro
    #iteramos cada libro en libros
    for libro in libros:
        #si el libro actual tiene un len != 0 quiere decir que no tiene una lista vacia por lo tanto tiene una lista con el rating 4 o 5
        if len(libro.select('.star-rating.Four'))!=0 or  len(libro.select('.star-rating.Five'))!=0:
           #tomamos el titulo del libro actual
           titulo_libro = libro.select('a')[1]['title']
           #guardamos el titulo del libro en una lista
           libros_ato_rating.append(titulo_libro)

#mostramos en pantalla todos los libros con rating de 4 o 5
for libro in libros_ato_rating:
    print(libro)