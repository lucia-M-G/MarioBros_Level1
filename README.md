# 🎮 Mario Bros - Nivell 1 (Python Game) 
**24-25-python-game-lucia-M-G created by GitHub Classroom**  
Faré aquest projecte utilitzant PyGame. Inspirat en el primer nivell del clàssic joc de **Super Mario Bros**, és un joc de plataformes on el jugador controla a Mario mentre recull monedes, derrota enemics, i arriba a la bandera per completar el nivell.

---

## 🎯 Objectiu del Joc
L'objectiu principal és guiar a Mario a través del nivell, evitant obstacles, derrotant enemics, i arribant a la bandera final. Pots recollir monedes, obtenir power-ups i superar reptes.

---

## 📋 Planificació del Joc

### 1. IDEA
Es tracta d'un joc de **plataformes** clàssic, on el jugador controla a Mario per avançar en el nivell, superant obstacles i derrotant enemics.

### 2. MECÀNIQUES
- **Controls:**
  - ➡️ **Esquerra/Dreta**: Moviment lateral de Mario.
  - ⬆️ **Salt**: Mario pot saltar per esquivar obstacles o trencar blocs.
  - ⬇️ **Ajupir-se**: Opcional per esquivar alguns enemics.

- **Interacció amb Blocs:**
  - **Blocs de monedes**: Mario obté una moneda per cada bloc trencat.
  - **Blocs sorpresa**: Poden contenir monedes, flors de foc o bolets de creixement.

- **Enemics:**
  - **Goombas**: Enemics comuns; Mario pot eliminar-los saltant-hi a sobre.
  - **Koopas**: Mario pot fer-los fora de la closca, usant-la per eliminar altres enemics o trencar blocs.

---

### 3. GRÀFICS I SO
- **Gràfics:**
  - **Sprites de Mario**: Inclouen animacions per a córrer, saltar, etc.
  - **Enemics**: Sprites de Goombas, Koopas, etc.
  - **Escenari**: Fons del nivell, blocs, canonades, arbres i muntanyes de fons.
  - **Objectes**: Monedes, bolets i flors de foc.

- **So:**
  - 🎶 **Música de fons**: Música clàssica del primer nivell de Super Mario Bros.
  - 🔊 **Efectes de so**: Per a saltar, recollir monedes, colpejar blocs i derrotar enemics.

---

### 4. ESTRUCTURA DEL NIVELL
- **Escena Principal (Nivell 1):**
  - Mario comença a l'esquerra de la pantalla i ha d'arribar a la bandera.
  - Plataformes, blocs sorpresa, blocs de monedes i canonades.
  - Enemics com Goombas i Koopas apareixen progressivament per introduir mecàniques de joc.
  - Col·locació de power-ups com bolets i flors de foc per ajudar al jugador.

- **Escena Final:**
  - Quan Mario arriba a la bandera, el nivell es completa amb l'animació de la plataforma.

---

## 🛠️ Requisits Tècnics
- **Python** 3.12
- **PyGame** (poden instal·lar-lo amb `pip install pygame`)

---

## 📂 Estructura de Fitxers
- `main.py`: Script principal del joc.
- `README.md`: Aquesta documentació.

---

## 🚀 Com Iniciar el Joc
1. Clona aquest repositori:
   ```bash
   git clone https://github.com/tuusuariogithub/24-25-python-game-lucia-M-G.git
