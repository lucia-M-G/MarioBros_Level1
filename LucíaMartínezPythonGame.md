# 24-25-python-game-lucia-M-G
24-25-python-game-lucia-M-G created by GitHub Classroom

PLANIFICACIÓ DEL JOC: MARIO BROS - NIVELL 1
Utilitzaré PyGame.
1. IDEA
  Crear una versió inspirada en el primer nivell de Super Mario Bros, el clàssic joc de plataformes. L'objectiu és que el jugador guï a Mario a través d'un nivell ple d'obstacles, recollint monedes i eliminant enemics fins a arribar a la bandera final.
2. MECÀNIQUES
  Controls:
    Esquerra/Dreta: Moviment lateral de Mario.
    Salt: Mario pot saltar per esquivar obstacles o enemics, així com per trencar blocs i recollir objectes especials.
    Baix: Ajupir-se (opcional per esquivar alguns enemics).
  Interacció amb blocs:
    Blocs de monedes: Mario obté una moneda cada cop que trenca un bloc d’aquest tipus.
    Blocs sorpresa: Poden contenir monedes, una flor de foc o un bolet de creixement.
  Enemics:
    Els Goombas són enemics comuns que Mario pot eliminar saltant-hi a sobre.
    Els Koopas (tortugues) es poden colpejar per alliberar la closca i usar-la per eliminar altres enemics o trencar blocs.
4. GRÀFICS I SO
  Gràfics:
    Sprites de Mario: Diferents animacions per a córrer, saltar, estar quiet, etc.
    Enemics: Sprites per als Goombas, Koopas i altres.
    Escenari: Fons de pantalla de nivell, blocs, canonades, arbres i muntanyes de fons.
    Objectes: Monedes, bolets i flors de foc.
  So:
    Música de fons clàssica del primer nivell de Super Mario Bros.
    Efectes de so per a saltar, recollir monedes, colpejar blocs i eliminar enemics.
5. ESTRUCTURA
  Escena principal (Nivell 1):
    Comença amb Mario a l'esquerra de la pantalla i l'objectiu és arribar al final del nivell.
    Inclou plataformes, blocs sorpresa, blocs de monedes i canonades.
    Els primers enemics, com Goombas i Koopas, apareixen progressivament per ensenyar al jugador les mecàniques bàsiques.
    Col·locació estratègica de blocs amb objectes de suport (bolets i flors).
  Escena final:
    Quan Mario arriba a la bandera, el jugador puja per la plataforma per completar el nivell.
