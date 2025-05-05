nomes = ["teste1","teste2"]

for nome in nomes:
    with open("./carta_model.txt") as file:
        content = file.read()
        content = content.replace("Xnome",nome)
        print(content)