import random
import pandas as pd

murid_l = [
    "adit", "agavra", "akhdan", "alfi", "beryl", "bama", "farhan", "khoirul", "fadli", "rafi", "rayyan", "zayyan"
]

murid_p = [
    "aisyah", "alika", "naira", "ami", "netta", "cassia", "kia", "faiza", "anin", "kira", "kenia", "khadijah", "audrey", "raisha", "sabila", "sachi", "sheril", "saski"
]

duduk_dengan = []
kursi = [[[], [], [], []],
         [[], [], [], []],
         [[], [], [], []],
         [[], [], []]]

random.shuffle(murid_l)
random.shuffle(murid_p)

for murid in range(0, len(murid_l), 2):

    duduk_dengan.append([murid_l[murid], murid_l[murid+1]])
    # murid1 = random.choice(murid_l)
    # murid_l.remove(murid1)
    # murid2 = random.choice(murid_l)
    # murid_l.remove(murid2)
    # temp = [murid1, murid2]
    # duduk_dengan.append(temp)

for murid in range(0, len(murid_p), 2):

    duduk_dengan.append([murid_p[murid], murid_p[murid+1]])
    # murid1 = random.choice(murid_p)
    # murid_p.remove(murid1)
    # murid2 = random.choice(murid_p)
    # murid_p.remove(murid2)
    # temp = [murid1, murid2]
    # duduk_dengan.append(temp)


for pasangan in duduk_dengan:
    while True:
        row = random.choice(kursi)
        cell = random.choice(row)
        if cell == []:
            cell.extend(pasangan)
            break

print(kursi)
df = pd.DataFrame(kursi)
df.to_csv('duduk.csv', index=False)