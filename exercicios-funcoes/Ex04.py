#como não tava claro se era pra gente pedir a quantidade de votos que teria ou
#parar quando a entrada fosse vaiz, escolhi a segunda opção
def validar_voto(val):
    return val in ["101","202","303"]

n = {"101": ["candidato 1", 0], "202": ["candidato 2", 0], "303": ["candidato 3", 0]}

print("\tTabela de votação\nCandidato 1: 101\nCandidato 2: 202\nCandidato 3: 303")
x = 1
while(True):
    a = input(f"Pessoa {x}|Voto: ")
    if(validar_voto(a)):
        n[a][1] += 1
        x += 1
    elif(a == ""):
        break
    else:
        print("Vote novamente")

n_aux = sorted(n, key = lambda x:n[x][1], reverse = True)

for i in n_aux:
    print(f"{n[i][0]}: {n[i][1]} votos")

if(n[n_aux[0]][1] > n[n_aux[1]][1]):
    print(f"{n[n_aux[0]][0]} venceu a eleição")
else:
    print("Empate, não houve nenhum vencedor")