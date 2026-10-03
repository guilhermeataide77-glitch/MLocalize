# 🌌 MLocalize

[![Powered by Astropy Logo](https://img.shields.io/badge/powered%20by-Astropy-orange.svg?style=flat)](https://www.astropy.org/)

Uma aplicação simples em **Python** desenvolvida para astrônomos amadores calcularem, com precisão matemática razoável, a visibilidade dos objetos do **Catálogo Messier** a partir de qualquer coordenada geográfica e horário.

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
```

---

## ⚙️ Pré-requisitos e Instalação

Certifique-se de ter o **Python** instalado em sua máquina.

Em seguida, instale a dependência necessária, **Astropy**, abrindo o terminal na pasta do projeto e executando:

```bash
pip install astropy
```

---

## 🚀 Como Executar

Com as dependências instaladas e a estrutura de pastas configurada, execute o script principal no terminal:

```bash
python principal.py
```
NÃO ESQUEÇA DE INFORMAR SUA LATITUDE, LONGITUDE E ALTITUDE:

```bash
# Localização (INFORME AQUI SUA LATITUDE, LONGITUDE E ALTITUDE)
        localizacao = EarthLocation(lat=-7.2300 * u.deg, lon=-35.8811 * u.deg, height=550 * u.m)
        tempo = Time.now()
        frame = AltAz(obstime=tempo, location=localizacao)
```


A interface gráfica irá exibir:

* 🔭 Uma tabela formatada contendo todos os objetos visíveis (**altitude > 15°**).
* 📐 Os objetos ordenados por proximidade ao **zênite**.
* ⭐ Uma recomendação especial com os **melhores alvos da noite** no alto céu.

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Astropy** — utilizada para manipulação de tempo, localização e transformações entre sistemas de coordenadas celestes **ICRS** e **AltAz**.
* **Tkinter** — para a construção da interface gráfica em modo escuro otimizada para observação noturna.
---

## 📚 Fonte dos Dados

As coordenadas de **Ascensão Reta (AR)** e **Declinação (Dec)** dos objetos do Catálogo Messier utilizadas neste projeto foram obtidas a partir dos dados disponibilizados pelo **SEDS (Students for the Exploration and Development of Space)**:

**Messier Objects — SEDS**
http://www.messier.seds.org/data.html

Os dados foram utilizados como referência para o arquivo `dados/catalogo.py`.

---

## 🔭 Funcionamento

O MLocalize utiliza as coordenadas de **Ascensão Reta (AR)** e **Declinação (Dec)** dos objetos do Catálogo Messier para determinar sua posição aparente no céu.

A partir da:

* 📍 localização geográfica do observador;
* 🕐 data e horário da observação;
* 🌌 coordenadas celestes do objeto;

o programa realiza a transformação de coordenadas **ICRS → AltAz** utilizando o **Astropy**.

A altitude resultante é utilizada para determinar quais objetos estão suficientemente altos no céu para observação.

Por padrão, o programa considera como visíveis os objetos com:

```text
Altitude > 15°
```

Os objetos são então organizados de acordo com sua proximidade ao **zênite**, permitindo identificar rapidamente os alvos que estão em melhores condições geométricas de observação.

---

## 📋 Exemplo de Saída

A execução do programa apresenta informações semelhantes a:

```text
Objetos Messier visíveis:

Objeto                         Altitude       Azimute
-----------------------------------------------------
M8 (Nebulosa da Lagoa)          42.31°        215.42°
M20 (Nebulosa Trífida)          38.17°        218.73°
M4 (Aglomerado Globular)        35.82°        202.16°
...

Melhores alvos da noite:
M8, M20, M4
```

---

## 🎯 Objetivo

O objetivo do **MLocalize** é fornecer uma ferramenta simples para auxiliar astrônomos amadores a descobrir **quais objetos do Catálogo Messier estão visíveis e em que posição se encontram no céu** em determinado momento.

O projeto também pode servir como base para futuras funcionalidades, como:

* 🌠 suporte a outros catálogos astronômicos;
* 🧭 cálculo de coordenadas para apontamento de telescópios;
* 📡 integração com montagens motorizadas;
* ⭐ filtros por tipo de objeto;
* 📱 interface gráfica melhor ou aplicação web;
* 🔭 integração com softwares de astronomia.
