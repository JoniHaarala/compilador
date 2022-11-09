from sintactico import parser

if __name__ == '__main':
    try:
        with open("test.txt", "r") as file:
            data = file.read()
            file.close()
            try:
                parser.parse(data)
                print('Analisis sintáctico Correcto!')
                print(result)
            except Exception as e:
                print(e)
                print('Analisis sintáctico Incorrecto!')
    except IndexError:
        print("Error al leer el archivo")


