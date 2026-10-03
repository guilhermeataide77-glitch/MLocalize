
import tkinter as tk
from tkinter import ttk, messagebox
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
import astropy.units as u
from datetime import datetime, timezone, timedelta

from dados.catalogo import catalogo_messier


class MlocalizeApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Mlocalize - Objetos Messier Visíveis")
        self.root.geometry("1000x750")
        self.root.minsize(900, 650)
        self.root.configure(bg="#121212")


        # TÍTULO
        

        titulo = tk.Label(
            root,
            text="🔭 Mlocalize - Objetos Messier Visíveis",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#121212"
        )
        titulo.pack(pady=(15, 5))

        subtitulo = tk.Label(
            root,
            text="Previsão de visibilidade dos objetos do catálogo Messier",
            font=("Arial", 10),
            fg="#aaaaaa",
            bg="#121212"
        )
        subtitulo.pack(pady=(0, 15))

       
        # FRAME PRINCIPAL DOS CONTROLES
       

        frame_config = tk.LabelFrame(
            root,
            text=" Configurações da observação ",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#121212",
            bd=1,
            relief="groove"
        )

        frame_config.pack(
            fill="x",
            padx=35,
            pady=5
        )

       
        # LOCALIZAÇÃO
      

        # LATITUDE 

        tk.Label(
            frame_config,
            text="Latitude:",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#121212"
        ).grid(
            row=0,
            column=0,
            padx=(15, 5),
            pady=10
        )

        self.entrada_latitude = tk.Entry(
            frame_config,
            width=12,
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.entrada_latitude.grid(
            row=0,
            column=1,
            padx=5
        )

        self.entrada_latitude.insert(
            0,
            "-7.2300"
        )

        # LONGITUDE

        tk.Label(
            frame_config,
            text="Longitude:",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#121212"
        ).grid(
            row=0,
            column=2,
            padx=(20, 5)
        )

        self.entrada_longitude = tk.Entry(
            frame_config,
            width=12,
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.entrada_longitude.grid(
            row=0,
            column=3,
            padx=5
        )

        self.entrada_longitude.insert(
            0,
            "-35.8811"
        )

        #  ALTITUDE 

        tk.Label(
            frame_config,
            text="Altitude (m):",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#121212"
        ).grid(
            row=0,
            column=4,
            padx=(20, 5)
        )

        self.entrada_altitude = tk.Entry(
            frame_config,
            width=10,
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.entrada_altitude.grid(
            row=0,
            column=5,
            padx=5
        )

        self.entrada_altitude.insert(
            0,
            "550"
        )

       
        # FUSO HORÁRIO
        

        tk.Label(
            frame_config,
            text="Fuso UTC:",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#121212"
        ).grid(
            row=0,
            column=6,
            padx=(20, 5)
        )

        self.entrada_fuso = tk.Entry(
            frame_config,
            width=8,
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.entrada_fuso.grid(
            row=0,
            column=7,
            padx=(5, 15)
        )

        # Brasil / Campina Grande
        self.entrada_fuso.insert(
            0,
            "-3"
        )

        
        # FRAME DATA/HORA
       

        frame_data = tk.LabelFrame(
            root,
            text=" Data e hora da observação ",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#121212",
            bd=1,
            relief="groove"
        )

        frame_data.pack(
            fill="x",
            padx=35,
            pady=10
        )

        #  DATA 

        tk.Label(
            frame_data,
            text="Data:",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#121212"
        ).grid(
            row=0,
            column=0,
            padx=(20, 5),
            pady=12
        )

        self.entrada_data = tk.Entry(
            frame_data,
            width=13,
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.entrada_data.grid(
            row=0,
            column=1,
            padx=5
        )

        #  HORA 

        tk.Label(
            frame_data,
            text="Hora:",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#121212"
        ).grid(
            row=0,
            column=2,
            padx=(20, 5)
        )

        self.entrada_hora = tk.Entry(
            frame_data,
            width=8,
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.entrada_hora.grid(
            row=0,
            column=3,
            padx=5
        )

        
        # BOTÃO PESQUISAR

        btn_pesquisar = tk.Button(
            frame_data,
            text="🔎 Pesquisar",
            command=self.pesquisar_data_hora,
            font=("Arial", 10, "bold"),
            bg="#238636",
            fg="white",
            padx=20,
            pady=7,
            relief="flat",
            cursor="hand2"
        )

        btn_pesquisar.grid(
            row=0,
            column=4,
            padx=5
        )        

        
        # BOTÃO DATA/HORA ATUAL
    
        btn_agora = tk.Button(
            frame_data,
            text="🕐 Usar data/hora atual",
            command=self.atualizar_agora,
            font=("Arial", 10, "bold"),
            bg="#1f6feb",
            fg="white",
            padx=15,
            pady=7,
            relief="flat",
            cursor="hand2"
        )

        btn_agora.grid(
            row=0,
            column=5,
            padx=20
        )

        
        
        # MOMENTO CONSULTADO
        

        self.label_momento = tk.Label(
            root,
            text="",
            font=("Arial", 11, "bold"),
            fg="#00ffcc",
            bg="#121212"
        )

        self.label_momento.pack(
            pady=(5, 5)
        )

      
        # TABELA
        
        frame_tabela = tk.Frame(
            root,
            bg="#121212"
        )

        frame_tabela.pack(
            fill="both",
            expand=True,
            padx=60,
            pady=10
        )

        colunas = (
            "objeto",
            "altitude",
            "azimute"
        )

        self.tabela = ttk.Treeview(
            frame_tabela,
            columns=colunas,
            show="headings"
        )

        # CABEÇALHOS 

        self.tabela.heading(
            "objeto",
            text="Objeto"
        )

        self.tabela.heading(
            "altitude",
            text="Altitude"
        )

        self.tabela.heading(
            "azimute",
            text="Azimute"
        )

        #  COLUNAS 

        self.tabela.column(
            "objeto",
            width=500,
            anchor="w"
        )

        self.tabela.column(
            "altitude",
            width=150,
            anchor="center"
        )

        self.tabela.column(
            "azimute",
            width=150,
            anchor="center"
        )

        #  SCROLLBAR 

        scrollbar = ttk.Scrollbar(
            frame_tabela,
            orient="vertical",
            command=self.tabela.yview
        )

        self.tabela.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabela.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    
        # ESTILO DA TABELA
        

        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure(
            "Treeview",
            background="#1e1e1e",
            foreground="#00ffcc",
            fieldbackground="#1e1e1e",
            rowheight=30,
            font=("Consolas", 10)
        )

        estilo.configure(
            "Treeview.Heading",
            background="#252526",
            foreground="white",
            relief="flat",
            font=("Arial", 10, "bold")
        )

        estilo.map(
            "Treeview",
            background=[
                ("selected", "#264f78")
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        
        # TOTAL DE OBJETOS
        ===

        self.label_total = tk.Label(
            root,
            text="",
            font=("Arial", 10),
            fg="white",
            bg="#121212"
        )

        self.label_total.pack(
            pady=3
        )

        
        # RECOMENDAÇÃO
        

        self.label_recomendacao = tk.Label(
            root,
            text="",
            font=("Arial", 10, "bold"),
            fg="#00ffcc",
            bg="#121212",
            wraplength=850
        )

        self.label_recomendacao.pack(
            pady=(2, 15)
        )

        
        # INICIALIZA COM DATA/HORA ATUAL
        

        self.atualizar_agora()

    # =============================================================
    # OBTER LOCALIZAÇÃO
    # =============================================================

    def obter_localizacao(self):

        try:

            latitude = float(
                self.entrada_latitude.get().replace(",", ".")
            )

            longitude = float(
                self.entrada_longitude.get().replace(",", ".")
            )

            altitude = float(
                self.entrada_altitude.get().replace(",", ".")
            )

            fuso = float(
                self.entrada_fuso.get().replace(",", ".")
            )

        except ValueError:

            raise ValueError(
                "Latitude, longitude, altitude e fuso "
                "devem ser números válidos."
            )

        # Verificar latitude

        if latitude < -90 or latitude > 90:

            raise ValueError(
                "A latitude deve estar entre -90° e +90°."
            )

        # Verificar longitude

        if longitude < -180 or longitude > 180:

            raise ValueError(
                "A longitude deve estar entre -180° e +180°."
            )

        # Verificar fuso

        if fuso < -12 or fuso > 14:

            raise ValueError(
                "O fuso horário deve estar entre UTC-12 e UTC+14."
            )

        localizacao = EarthLocation(
            lat=latitude * u.deg,
            lon=longitude * u.deg,
            height=altitude * u.m
        )

        return localizacao, fuso

    
    # CALCULAR VISIBILIDADE

    def calcular_visibilidade(self, tempo):

        localizacao, _ = self.obter_localizacao()

        frame = AltAz(
            obstime=tempo,
            location=localizacao
        )

        visiveis = []

        for nome, coords in catalogo_messier.items():

            sky = SkyCoord(
                ra=coords["ar"],
                dec=coords["dec"],
                unit=(u.deg, u.deg),
                frame="icrs"
            )

            local = sky.transform_to(frame)

            altitude = local.alt.deg
            azimute = local.az.deg

            # Apenas objetos acima de 15°
            if altitude > 15.0:

                visiveis.append({
                    "nome": nome,
                    "altitude": altitude,
                    "azimute": azimute
                })

        # Maior altitude primeiro

        visiveis.sort(
            key=lambda x: x["altitude"],
            reverse=True
        )

        return visiveis

    
    # ATUALIZAR TABELA

    def atualizar_tabela(self, tempo):

        try:

            visiveis = self.calcular_visibilidade(tempo)

        except ValueError as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

            return

        # Limpar tabela

        for item in self.tabela.get_children():

            self.tabela.delete(item)

        # Inserir objetos

        for obj in visiveis:

            self.tabela.insert(
                "",
                "end",
                values=(
                    obj["nome"],
                    f"{obj['altitude']:.2f}°",
                    f"{obj['azimute']:.2f}°"
                )
            )

        
        # MOMENTO

        momento_local = tempo.to_datetime()

        texto_momento = momento_local.strftime(
            "%d/%m/%Y às %H:%M:%S"
        )

        self.label_momento.config(
            text=f"Resultados para: {texto_momento}"
        )

        
        # TOTAL
       

        self.label_total.config(
            text=f"Total de objetos acima de 15°: {len(visiveis)}"
        )

      
        # RECOMENDAÇÃO
        

        if len(visiveis) == 0:

            self.label_recomendacao.config(
                text=(
                    "🔭 Nenhum objeto Messier do catálogo "
                    "está acima de 15° neste momento."
                )
            )

            return

        # Objetos acima de 60°

        melhores = [
            obj
            for obj in visiveis
            if obj["altitude"] >= 60.0
        ]

        if melhores:

            nomes = ", ".join(
                obj["nome"]
                for obj in melhores[:3]
            )

            self.label_recomendacao.config(
                text=(
                    "🔭 Objetos com maior altitude: "
                    + nomes
                )
            )

        else:

            melhor = visiveis[0]

            self.label_recomendacao.config(
                text=(
                    f"🔭 Maior altitude: {melhor['nome']} "
                    f"({melhor['altitude']:.2f}°)"
                )
            )

   
    # CONVERTER DATA/HORA LOCAL PARA ASTROPY
    
    def criar_tempo_local(self):

        data = self.entrada_data.get().strip()
        hora = self.entrada_hora.get().strip()

        # Obter fuso

        try:

            fuso = float(
                self.entrada_fuso.get().replace(",", ".")
            )

        except ValueError:

            raise ValueError(
                "O fuso horário deve ser um número.\n\n"
                "Exemplo: -3"
            )

        # Converter data/hora

        try:

            data_hora = datetime.strptime(
                f"{data} {hora}",
                "%d/%m/%Y %H:%M"
            )

        except ValueError:

            raise ValueError(
                "Data ou hora inválida.\n\n"
                "Use:\n\n"
                "Data: DD/MM/AAAA\n"
                "Hora: HH:MM\n\n"
                "Exemplo:\n"
                "03/10/2026\n"
                "21:30"
            )

        # Criar timezone usando o UTC informado

        timezone_local = timezone(
            timedelta(hours=fuso)
        )

        data_hora_local = data_hora.replace(
            tzinfo=timezone_local
        )

        # Converter para UTC

        data_hora_utc = data_hora_local.astimezone(
            timezone.utc
        )

        # Criar objeto Time do Astropy

        tempo = Time(
            data_hora_utc
        )

        return tempo

   
    # BOTÃO: PESQUISAR
    def pesquisar_data_hora(self):

        try:

            tempo = self.criar_tempo_local()

            self.atualizar_tabela(
                tempo
            )

        except ValueError as erro:

            messagebox.showerror(
                "Data ou hora inválida",
                str(erro)
            )



   
    # BOTÃO: DATA/HORA ATUAL

    def atualizar_agora(self):

        try:

            _, fuso = self.obter_localizacao()

        except ValueError as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

            return

        # Hora atual em UTC

        agora_utc = datetime.now(
            timezone.utc
        )

        # Converter para o fuso informado

        timezone_local = timezone(
            timedelta(hours=fuso)
        )

        agora_local = agora_utc.astimezone(
            timezone_local
        )

        # Atualizar data

        self.entrada_data.delete(
            0,
            tk.END
        )

        self.entrada_data.insert(
            0,
            agora_local.strftime("%d/%m/%Y")
        )

        # Atualizar hora

        self.entrada_hora.delete(
            0,
            tk.END
        )

        self.entrada_hora.insert(
            0,
            agora_local.strftime("%H:%M")
        )

        # Criar Time

        tempo = Time(
            agora_utc
        )

        # Atualizar tabela

        self.atualizar_tabela(
            tempo
        )

    



# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    root = tk.Tk()

    app = MlocalizeApp(root)

    root.mainloop()
