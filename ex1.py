import random

while True:

    def llegir_llista_enters():
        print("Introdueix nombres enters (. per finalitzar)")
        num = -1
        i = 0 
        llista = []
        while num != ".":
            i += 1
            num = input(f"Nombre {i}: ")
            llista.append(num)
        llista.pop()
        return llista


    def senars_llista():
        llista = [1, 2, 3, 4, 5, 6, 7, 8]
        for num in llista:
            if num % 2 == 0:
                llista.remove(num)
        return llista


    def sumar_parells_llista():
        llista = [1, 2, 3, 4, 5, 6, 7, 8]
        suma = 0
        for num in llista:
            if num % 2 == 0:
                suma += num
        return suma


    def cercar_numero_llista():
        llista = [3, 1, 5, 2, 7, 9, 6]
        num_usuari = int(input("Introdueix un número: "))
        for index, num in enumerate(llista): 
            if num == num_usuari:
                print(index + 1)
                break
        else:
                print(- 1)


    def llegir_llista_paraules():
        paraules = ""
        i = 0
        llista = []
        while paraules != ".":
            i += 1
            paraules = input(f"Paraula {i}: ")
            llista.append(paraules)
        llista.pop()
        return llista


    def crear_paraula_llista(llista):
        for paraules in llista:
            inicial = paraules[0]
            print(inicial)
                

    def crear_llista_num_aleatoris():
        llista = []
        for i in range(5):
            num = random.randint(1, 100)
            llista.append(num)
        return llista


    def comparar_llistes(llista1, llista2):
        llista = []
        for element in llista1:
            if element in llista2:
                if llista1.index(element) == llista2.index(element):
                    llista.append(2)
                else:
                    llista.append(1)

            else:
                llista.append(0)
                
        return llista


    def majors_edat(edat1, edat2):
        if edat1 >= 18:
            print("Edat 1 és major dèdat")
        else:
            print("Edat 1 no és major dèdat")

        if edat2 >= 18:
            print("Edat 2 és major dèdat")
        else:
            print("Edat 2 no és major dèdat")

        

    def menu():
        print("""
            1. llegir_llista_enters()
            2. senars_llista()
            3. sumar_parells_llista()
            4. cercar_numero_llista()
            5. llegir_llista_paraules()
            6. crear_paraula_llista(llista)
            7. crear_llista_num_aleatoris()
            8. comparar_llistes(llista1, llista2)
            9. majors_edat(edat1, edat2)
    """)
        
    menu()

    opcio = int(input("Introdueix el nombre de l'opció que vol fer: "))

    if opcio == 1:
        print(llegir_llista_enters())
    elif opcio == 2:
        print(senars_llista())
    elif opcio == 3:
        print(sumar_parells_llista())
    elif opcio == 4:
        cercar_numero_llista()
    elif opcio == 5:
        print(llegir_llista_paraules())
    elif opcio == 6:
        crear_paraula_llista(llista=["Hawai", "Olimpiades", "Llibreta", "Algortime"])
    elif opcio == 7:
        print(crear_llista_num_aleatoris())
    elif opcio == 8:
        print(comparar_llistes(llista1=["Hawai", "Olimpiades", "Llibreta", "Algortime"], llista2=["Hola", "Olimpiades", "Algortime", "Llibreta"]))
    else:
        majors_edat(edat1=15, edat2=22)
