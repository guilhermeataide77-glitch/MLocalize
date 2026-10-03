# principal.py

from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
import astropy.units as u
from dados.catalogo import catalogo_messier

# 1. Definir a sua localização!

latitude_usuario = -7.2300 * u.deg
longitude_usuario = -35.8811 * u.deg
altitude_usuario = 550 * u.m

localizacao_usuario = EarthLocation(
    lat=latitude_usuario, 
    lon=longitude_usuario, 
    height=altitude_usuario
)

# 2. Obter o momento temporal atual
tempo_atual = Time.now()


# 3. Configurar a transformação para o sistema de horizonte local (AltAz)
frame_local = AltAz(obstime=tempo_atual, location=localizacao_usuario)

lista_visiveis = []

# 4. Iterar pelos objetos, converter coordenadas e filtrar os visíveis (> 15°)
for nome_objeto, coordenadas in catalogo_messier.items():
    coordenada_ceu = SkyCoord(
        ra=coordenadas['ar'], 
        dec=coordenadas['dec'], 
        unit=(u.deg, u.deg), 
        frame='icrs'
    )
    
    coordenada_local = coordenada_ceu.transform_to(frame_local)
    
    altitude_graus = coordenada_local.alt.deg
    azimute_graus = coordenada_local.az.deg
    
    if altitude_graus > 15.0:
        lista_visiveis.append({
            "nome": nome_objeto,
            "altitude": altitude_graus,
            "azimute": azimute_graus
        })

# 5. Ordenar os objetos do mais próximo do zênite para o mais distante
lista_visiveis.sort(key=lambda x: x["altitude"], reverse=True)

# 6. Exibir a tabela completa 
largura_coluna_nome = 45
linha_separadora = "-" * (largura_coluna_nome + 26)

print();
print("MLOCALIZE - Objetos Messier Visíveis-----------------------------------\n")
print(f"{'Objeto':<{largura_coluna_nome}} | {'Altitude':<10} | {'Azimute':<10}")
print(linha_separadora)

for obj in lista_visiveis:
    print(f"{obj['nome']:<{largura_coluna_nome}} | {obj['altitude']:>6.2f}°    | {obj['azimute']:>6.2f}°")

print(linha_separadora)
print(f"Total de objetos visíveis no momento: {len(lista_visiveis)}")

# 7. Recomendação dos melhores alvos (mais próximos do zênite)
melhores_alvos = [obj for obj in lista_visiveis if obj["altitude"] >= 60.0]

print("\n" + "=" * len(linha_separadora))
print("RECOMENDAÇÃO DA NOITE (Mais próximos do Zênite / Alto Céu):")
print("=" * len(linha_separadora))

if melhores_alvos:
    for i, obj in enumerate(melhores_alvos[:3], 1):
        print(f"{i}. {obj['nome']} — Altitude de {obj['altitude']:.2f}° (Excelente visibilidade!)")
else:
    if lista_visiveis:
        print(f"Nenhum objeto está muito perto do zênite agora, mas o topo da lista ({lista_visiveis[0]['nome']}) é a melhor opção no momento.")
    else:
        print("Nenhum objeto Messier do catálogo interno está acima de 15° no momento.")
print("=" * len(linha_separadora))