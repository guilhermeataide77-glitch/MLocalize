# MLocalize
Um script simples em Python desenvolvido para astrônomos amadores calcularem com precisão matemática a visibilidade dos objetos do Catálogo Messier a partir de qualquer coordenada geográfica e horário.
---

## 📂 Estrutura do Projeto

O código é modularizado para separar a lógica de cálculo dos dados estáticos:

```text
Mlocalize/
├── dados/
│   ├── __init__.py
│   └── catalogo.py     # Contém o dicionário com os objetos Messier e suas coordenadas (AR e Dec)
├── principal.py        # Script principal com os cálculos astronômicos (Astropy)
└── README.md           # Documentação do projeto

##⚙️ Pré-requisitos e Instalação
Certifique-se de ter o Python instalado em sua máquina. Em seguida, instale a dependência necessária (astropy) abrindo o terminal na pasta do projeto e executando:

Bash
pip install astropy

🚀 Como Executar
Com as dependências instaladas e a estrutura de pastas configurada, execute o script principal no terminal:

Bash
python principal.py
O programa irá gerar no terminal:

O momento exato da consulta em UTC.

Uma tabela formatada contendo todos os objetos visíveis (altitude > 15°), ordenados por proximidade ao zênite.

Uma recomendação especial com os melhores alvos da noite no alto céu.

🛠️ Tecnologias Utilizadas
Python

Astropy (para manipulação de tempo, localização e transformações de sistemas de coordenadas celestes ICRS para AltAz)
