def zapisi(file_name, tekst):
    try:
        with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
            file.write(tekst)
    except Exception as e:
        print("greska", e)

def procitaj():
    pass