def zapisi(file_name, tekst):
    with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
        file.write(tekst)

def procitaj():
    pass