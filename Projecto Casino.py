name = input("Hola, como te llamas\n")

#si es boris o no
if name == "Boris":
    no_curro = input("Curras?\n")

     #si boris no curra
    if no_curro == "No":
        print("Fuera de aqui Boris, Ponte a currar")
        exit()

     #si boris curra
    else:
        print("Bienvendio " + name + " al Casino")
        
        menu = "piti, peta o cafe"
        
        elecion = input("De menu tenemos " + menu + ", que le apetece?\n")

        #si boris eligue bien
        if elecion == "piti" or elecion == "peta" or elecion == "cafe":

            cantidad = input("Cuanto quisiera de " + elecion + "?\n")
        
            precio = 3
        
            total = precio * int(cantidad)
        
            print("Su total es de " + str(total) + ", que la pase chill")

         #si boris eligue mal
        else:
            intento = input("No tenemos de eso, te lo vuelo a repetir, tenemos " + menu + ", que va a eleguir?\n")

            #si boris eligue bien por 2 vez
            if intento == "piti" or elecion == "peta" or elecion == "cafe":
        
              cantidad = input("Vale, ahora si, cuanto quisiera de " + elecion + "?\n")
        
              precio = 3
                    
              total = precio * int(cantidad)
                    
              print("Su total es de " + str(total) + ", que la pase chill")

             #si boris eligue mal por 2 vez
            else:
                print("Tu eres tonto? Fuera de aqui i a currar coño")
                exit()

else:#si no es Boris
    print("Bienvendio " + name + " al Casino")

    menu = "piti, peta o cafe"

    elecion = input("De menu tenemos " + menu + ", que le apetece?\n")

    #si elgue bien
    if elecion == "piti" or elecion == "peta" or elecion == "cafe":

        cantidad = input("Cuanto quisiera de " + elecion + "?\n")

        precio = 3

        total = precio * int(cantidad)

        print("Su total es de " + str(total) + ", que la pase chill")

     #si eligue mal
    else:
        intento = input("No tenemos de eso, te lo vuelo a repetir, tenemos " + menu + ", que va a eleguir?\n")
        
        #si eligue bien por 2 vez
        if intento == "piti" or elecion == "peta" or elecion == "cafe":

            cantidad = input("Vale, ahora si, cuanto quisiera de " + elecion + "?\n")

            precio = 3
            
            total = precio * int(cantidad)
            
            print("Su total es de " + str(total) + ", que la pase chill")

         #si eligue mal por 2 vez
        else:
            print("Tu eres tonto? Fuera de aqui i a currar coño")
            exit()