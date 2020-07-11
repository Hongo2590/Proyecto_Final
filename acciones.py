

prestamos= []

def listaPersonas (dfp):
    print(dfp)    

def ordenarPersonas (dfp):
    by_name = dfp.sort_values('Nombre')
    
    print(by_name)


def registroPersonas ():
    personas=[ 
        {"ID":1,"302600403" "Nombre Completo:": "Daniel Fernando Ballestero Umaña ", "Correo Electronico":"daniel.ballestero.umana@mep.go.cr"},
        {"ID":2,"106540419" "Nombre Completo:":"Milton Eliseo De San Martin Lobo Nuñez", "Correo Electronico":"miltonelobo@gmail.com"},
        {"ID":3,"502890635" "Nombre Completo:":"Emilce Liseth Vargas Campos", "Correo Electronico":"liseth.vargas.campos@fod.ac.cr"},
        {"ID":4,"502850756" "Nombre Completo:":"Roberto Elias Molina Rosales","Correo Electronico":"roberto.molina.rosales@mep.go.cr"},
        {"ID":5,"108290982" "Nombre Completo:":"Carlos Manuel Zapata Cerdas", "Correo Electronico":"carlos.zapata.cerdas@mep.go.cr"},
        {"ID":6,"107570905" "Nombre Completo:":"Jose Yamil Alvarez Cabalceta", "Correo Electronico":"yamil.alvarez.cabalceta@mep.go.cr"},
        {"ID":7,"112160596" "Nombre Completo:":"Cinthya Yesenia Corrales Alvarado", "Correo Electronico":"112160596@nomail.com"},
        {"ID":8,"105960154" "Nombre Completo:":"Gladys Lorena Jimenez Solano", "Correo Electronico":"esc.puertonuevo@mep.go.cr"},
        {"ID":9,"502820232" "Nombre Completo:":"Seidy Lopez Medina", "Correo Electronico":"seidy.lopez.medina@mep.go.cr"},
        {"ID":10,"107980545" "Nombre Completo:":"Alexis Vargas Calderon", "Correo Electronico":"107980545@nomail.com"},
        {"ID":11,"105210055" "Nombre Completo:":"Hector Miguel Del Carmen Segura Prado", "Correo Electronico":"105210055@nomail.com"},
        {"ID":12,"104850674" "Nombre Completo:":"Miguel Angel Fuentes Fuentes", "Correo Electronico":"miguel.fuentes.fuentes@mep.go.cr"},
        {"ID":13,"107640438" "Nombre Completo:":"Herminia Maria Baldivia Hernandez", "Correo Electronico":"107640438@nomail.com"},
        {"ID":14,"104920381" "Nombre Completo:":"Manuel Antonio Vila Vargas", "Correo Electronico":"104920381@nomail.com"},
        {"ID":15,"105960915" "Nombre Completo:":"Maria Gabriela Matamoros Landazuri", "Correo Electronico":"105960915@nomail.com"},
        {"ID":16,"800720668" "Nombre Completo:":"Janina Ruth Castillo Pasos", "Correo Electronico":"800720668@nomail.com"},
        {"ID":17,"107130829" "Nombre Completo:":"Jorge Enrique Flores Nuñez", "Correo Electronico":"107130829@nomail.com"},
        {"ID":18,"701410305" "Nombre Completo:":"Jhovan Martin Perez Navarrete", "Correo Electronico":"jhovan.perez.navarrete@mep.go.cr"},
        {"ID":19,"701120963" "Nombre Completo:":"Erika Ester Reyes Aleman", "Correo Electronico":"701120963@nomail.com"},
        {"ID":20,"205130061" "Nombre Completo:":"Emidey Gerarda Arias Hernandez", "Correo Electronico":"emidey.arias.hernandez@mep.go.cr"},
        {"ID":21,"501870378" "Nombre Completo:":"Nubia Lides Marchena Viales", "Correo Electronico":"501870378@nomail.com"},
        {"ID":23,"110590870" "Nombre Completo:":"Jessica Perlina Bent Morales", "Correo Electronico":"111090452@nomail.com"},
        {"ID":24,"110590870" "Nombre Completo:":"Karla Vanessa Mora Sanchez", "Correo Electronico":"kmora20@yahoo.com"},
        {"ID":25,"111820374" "Nombre Completo:":"Flor De Maria Corella Monge", "Correo Electronico":"flor.corella.monge@mep.go.cr"},
        {"ID":26,"502820103" "Nombre Completo:":"Yessenia Ruiz Contreras", "Correo Electronico":"yessenia.ruiz.contreras@mep.go.cr"},
        {"ID":28,"503420096" "Nombre Completo:":"Jennifer Marcela Gutierrez Vargas", "Correo Electronico":"esc.camposdeoro@mep.go.cr"},
        {"ID":29,"110300227" "Nombre Completo:":"Juan Carlos Valverde Rivera", "Correo Electronico":"juan.valverde.rivera@mep.go.cr"},
        {"ID":30,"603490324" "Nombre Completo:":"Andrea Merceditas Mejias Gomez", "Correo Electronico":"Amejias_g@hotmail.com"},
        {"ID":31,"107310409" "Nombre Completo:":"Luis Alejandro Aponte Quiros", "Correo Electronico":"esc.canoblanco@mep.go.cr"},
        {"ID":32,"113100411" "Nombre Completo:":"Andrea Carolina Castillo Villalobos", "Correo Electronico":"ancarcavi27@gmail.com"},
    ]

    idpersona= str (input("Digite el ID de la persona: "))
    print(personas[int(idpersona)-1]) 

def listaLibros (dfl):
    print(dfl)

def buscarLibros ():
    libros= [
    {"Nombre": "Cien años de soledad"},
    {"Nombre": "Don Quiojote de la Mancha"},
    {"Nombre": "Hamlet"},
    {"Nombre": "El Principito"},
    {"Nombre": "Orgullo y Prejuicio"},
    {"Nombre": "1984"},
    {"Nombre": "La Odisea"},
    {"Nombre": "El retrato de Dorian Grey"},
    {"Nombre": "Lo que el viento se llevo"},
    {"Nombre": "Moby-Dick"} ]

    search= str (input("Escriba el nombre del libro que desea buscar: "))

    l=0
    while (l < len(libros)):
        if(libros[l]["Nombre"].find(search) >= 0):
            print(libros[l])
        l=l+1

def prestarLibros ():
    personas= [ 
        {"ID":1,"302600403" "Nombre Completo:": "Daniel Fernando Ballestero Umaña ", "Correo Electronico":"daniel.ballestero.umana@mep.go.cr"},
        {"ID":2,"106540419" "Nombre Completo:":"Milton Eliseo De San Martin Lobo Nuñez", "Correo Electronico":"miltonelobo@gmail.com"},
        {"ID":3,"502890635" "Nombre Completo:":"Emilce Liseth Vargas Campos", "Correo Electronico":"liseth.vargas.campos@fod.ac.cr"},
        {"ID":4,"502850756" "Nombre Completo:":"Roberto Elias Molina Rosales","Correo Electronico":"roberto.molina.rosales@mep.go.cr"},
        {"ID":5,"108290982" "Nombre Completo:":"Carlos Manuel Zapata Cerdas", "Correo Electronico":"carlos.zapata.cerdas@mep.go.cr"},
        {"ID":6,"107570905" "Nombre Completo:":"Jose Yamil Alvarez Cabalceta", "Correo Electronico":"yamil.alvarez.cabalceta@mep.go.cr"},
        {"ID":7,"112160596" "Nombre Completo:":"Cinthya Yesenia Corrales Alvarado", "Correo Electronico":"112160596@nomail.com"},
        {"ID":8,"105960154" "Nombre Completo:":"Gladys Lorena Jimenez Solano", "Correo Electronico":"esc.puertonuevo@mep.go.cr"},
        {"ID":9,"502820232" "Nombre Completo:":"Seidy Lopez Medina", "Correo Electronico":"seidy.lopez.medina@mep.go.cr"},
        {"ID":10,"107980545" "Nombre Completo:":"Alexis Vargas Calderon", "Correo Electronico":"107980545@nomail.com"},
        {"ID":11,"105210055" "Nombre Completo:":"Hector Miguel Del Carmen Segura Prado", "Correo Electronico":"105210055@nomail.com"},
        {"ID":12,"104850674" "Nombre Completo:":"Miguel Angel Fuentes Fuentes", "Correo Electronico":"miguel.fuentes.fuentes@mep.go.cr"},
        {"ID":13,"107640438" "Nombre Completo:":"Herminia Maria Baldivia Hernandez", "Correo Electronico":"107640438@nomail.com"},
        {"ID":14,"104920381" "Nombre Completo:":"Manuel Antonio Vila Vargas", "Correo Electronico":"104920381@nomail.com"},
        {"ID":15,"105960915" "Nombre Completo:":"Maria Gabriela Matamoros Landazuri", "Correo Electronico":"105960915@nomail.com"},
        {"ID":16,"800720668" "Nombre Completo:":"Janina Ruth Castillo Pasos", "Correo Electronico":"800720668@nomail.com"},
        {"ID":17,"107130829" "Nombre Completo:":"Jorge Enrique Flores Nuñez", "Correo Electronico":"107130829@nomail.com"},
        {"ID":18,"701410305" "Nombre Completo:":"Jhovan Martin Perez Navarrete", "Correo Electronico":"jhovan.perez.navarrete@mep.go.cr"},
        {"ID":19,"701120963" "Nombre Completo:":"Erika Ester Reyes Aleman", "Correo Electronico":"701120963@nomail.com"},
        {"ID":20,"205130061" "Nombre Completo:":"Emidey Gerarda Arias Hernandez", "Correo Electronico":"emidey.arias.hernandez@mep.go.cr"},
        {"ID":21,"501870378" "Nombre Completo:":"Nubia Lides Marchena Viales", "Correo Electronico":"501870378@nomail.com"},
        {"ID":23,"110590870" "Nombre Completo:":"Jessica Perlina Bent Morales", "Correo Electronico":"111090452@nomail.com"},
        {"ID":24,"110590870" "Nombre Completo:":"Karla Vanessa Mora Sanchez", "Correo Electronico":"kmora20@yahoo.com"},
        {"ID":25,"111820374" "Nombre Completo:":"Flor De Maria Corella Monge", "Correo Electronico":"flor.corella.monge@mep.go.cr"},
        {"ID":26,"502820103" "Nombre Completo:":"Yessenia Ruiz Contreras", "Correo Electronico":"yessenia.ruiz.contreras@mep.go.cr"},
        {"ID":28,"503420096" "Nombre Completo:":"Jennifer Marcela Gutierrez Vargas", "Correo Electronico":"esc.camposdeoro@mep.go.cr"},
        {"ID":29,"110300227" "Nombre Completo:":"Juan Carlos Valverde Rivera", "Correo Electronico":"juan.valverde.rivera@mep.go.cr"},
        {"ID":30,"603490324" "Nombre Completo:":"Andrea Merceditas Mejias Gomez", "Correo Electronico":"Amejias_g@hotmail.com"},
        {"ID":31,"107310409" "Nombre Completo:":"Luis Alejandro Aponte Quiros", "Correo Electronico":"esc.canoblanco@mep.go.cr"},
        {"ID":31,"113100411" "Nombre Completo:":"Andrea Carolina Castillo Villalobos", "Correo Electronico":"ancarcavi27@gmail.com"},
    ]

    libros= [
        {"ID":1,"Nombre del libro":"Cien años de soledad","Genero":"Novela","Autor":"Gabriel Gracía Márquez"},
        {"ID":2,"Nombre del libro":"Don Quijote de la Mancha","Genero":"Aburrido","Autor":"Miguel de Cervantes"},
        {"ID":3,"Nombre del libro":"Hamlet","Genero":"Teatro","Autor":"William Shakespeare"},
        {"ID":4,"Nombre del libro":"El principito","Genero":"Fantasía","Autor":"Antoine dee Saint Exupéry"},
        {"ID":5,"Nombre del libro":"Orgullo y Prejuicio","Genero":"Romantico","Autor":"Jane Austen"},
        {"ID":6,"Nombre del libro":"1984","Genero":"Misterio","Autor":"George Orwell"},
        {"ID":7,"Nombre del libro":"La Odisea","Genero":"Poesía","Autor":"Homero"},
        {"ID":8,"Nombre del libro":"El retrato de Dorian Grey","Genero":"Fantasía","Autor":"Oscar Wilde"},
        {"ID":9,"Nombre del libro":"Lo que el viento se llevo","Genero":"Drama","Autor":"Margaret Mitchell"},
        {"ID":10,"Nombre del libro":"Moby Dick","Genero":"Fantasía","Autor":"Herman Melville"},
    ]

    

    print(personas)
    idPersona= int (input("Introduzaca el ID de la persona que desea buscar: "))
    print(libros)
    idLibro= int (input("Introduzca el ID del libro que desea buscar: "))
    nuevoPrestamo= {"idPersona": idPersona, "idLibro": idLibro, "fecha": "9/7/2020"}
    prestamos.append(nuevoPrestamo)

def verPrestamo ():
    print(prestamos)
    