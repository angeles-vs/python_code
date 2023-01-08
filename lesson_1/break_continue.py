def run():
    for contador in range (1000):
        if contador % 2 != 0:
            continue
        print (contador)

    for i in range (100):
        print(i)
        if i == 50:
           break


    texto = input("escribeme: ")
    for letra in texto:
        if letra == 'e':
            break
        print(letra)


if __name__ == "__main__":
    run()


