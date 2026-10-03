# principal.py

import tkinter as tk
from tkinter import ttk, messagebox
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
import astropy.units as u
from dados.catalogo import catalogo_messier

class MlocalizeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mlocalize - Objetos Messier Visíveis")
        self.root.geometry("750x600")
        self.root.configure(bg="#121212") # Fundo escuro para astronomia

        # Título
        titulo = tk.Label(root, text="🔭 Mlocalize - Céu de Campina Grande, PB", 
                          font=("Arial", 14, "bold"), fg="#ffffff", bg="#121212")
        titulo.pack(pady=15)

        # Botão de cálculo
        btn_calcular = tk.Button(root, text="Calcular Objetos Visíveis Agora", 
                                 command=self.atualizar_dados,
                                 font=("Arial", 11, "bold"), bg="#1f6feb", fg="white", padx=10, relief="flat")
        btn_calcular.pack(pady=5)

        # Caixa de texto com barra de rolagem (estilo terminal limpo)
        frame_texto = tk.Frame(root, bg="#121212")
        frame_texto.pack(fill="both", expand=True, padx=20, pady=15)

        self.txt_resultados = tk.Text(frame_texto, bg="#1e1e1e", fg="#00ffcc", 
                                      font=("Consolas", 10), relief="flat")
        scrollbar = tk.Scrollbar(frame_texto, command=self.txt_resultados.yview)
        
        self.txt_resultados.configure(yscrollcommand=scrollbar.set)
        
        self.txt_resultados.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Executa o cálculo inicial ao abrir
        self.atualizar_dados()

    def calcular_visibilidade(self):
        # Localização (Campina Grande, PB)
        localizacao = EarthLocation(lat=-7.2300 * u.deg, lon=-35.8811 * u.deg, height=550 * u.m)
        tempo = Time.now()
        frame = AltAz(obstime=tempo, location=localizacao)
        
        visiveis = []
        for nome, coords in catalogo_messier.items():
            sky = SkyCoord(ra=coords['ar'], dec=coords['dec'], unit=(u.deg, u.deg), frame='icrs')
            local = sky.transform_to(frame)
            if local.alt.deg > 15.0:
                visiveis.append({
                    "nome": nome,
                    "altitude": local.alt.deg,
                    "azimute": local.az.deg
                })
        
        visiveis.sort(key=lambda x: x["altitude"], reverse=True)
        return tempo, visiveis

    def atualizar_dados(self):
        self.txt_resultados.delete("1.0", tk.END)
        tempo, visiveis = self.calcular_visibilidade()
        
        largura_coluna_nome = 45
        linha_separadora = "-" * (largura_coluna_nome + 26)

        # Iniciando direto com a tabela sem exibir horário ou local na tela
        texto_saida = f"{'Objeto':<{largura_coluna_nome}} | {'Altitude':<10} | {'Azimute':<10}\n"
        texto_saida += linha_separadora + "\n"
        
        for obj in visiveis:
            texto_saida += f"{obj['nome']:<{largura_coluna_nome}} | {obj['altitude']:>6.2f}°    | {obj['azimute']:>6.2f}°\n"
        
        texto_saida += linha_separadora + "\n"
        texto_saida += f"Total de objetos visíveis no momento: {len(visiveis)}\n\n"
        
        melhores = [o for o in visiveis if o["altitude"] >= 60.0]
        texto_saida += "=" * len(linha_separadora) + "\n"
        texto_saida += "⭐ RECOMENDAÇÃO DA NOITE (Mais próximos do Zênite / Alto Céu):\n"
        texto_saida += "=" * len(linha_separadora) + "\n"
        
        if melhores:
            for i, obj in enumerate(melhores[:3], 1):
                texto_saida += f"{i}. {obj['nome']} — Altitude de {obj['altitude']:.2f}° (Excelente visibilidade!)\n"
        else:
            if visiveis:
                texto_saida += f"Nenhum objeto está muito perto do zênite agora, mas o topo da lista ({visiveis[0]['nome']}) é a melhor opção no momento.\n"
            else:
                texto_saida += "Nenhum objeto Messier do catálogo interno está acima de 15° no momento.\n"
        texto_saida += "=" * len(linha_separadora) + "\n"

        self.txt_resultados.insert(tk.END, texto_saida)

if __name__ == "__main__":
    root = tk.Tk()
    app = MlocalizeApp(root)
    root.mainloop()
