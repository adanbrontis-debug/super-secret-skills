---
name: brontis-disecar-referencias
description: 'Analiza una imagen o un video de referencia y extrae su lenguaje visual en capas nombradas (encuadre, lente, luz, color, textura, dirección de arte, movimiento, edición). Devuelve un "ADN visual" reutilizable con bloque de prompt en inglés para generar cosas nuevas que se sientan de la misma familia sin copiar la pieza. Trigger cuando el usuario diga "disecar referencias", "/disecar", "analiza esta referencia", "quiero que se vea así", "qué tiene esta imagen", "extrae el estilo", "moodboard a prompt", "me gusta esto, cómo lo pido". NO usar para extraer la idea o el mecanismo creativo de una pieza (para eso está Robar como Artista) ni para entender por qué un video se hizo viral (para eso está ¿Por Qué Se Hizo Viral?).'
---

# Disecar Referencias

Una skill de Brontis_ para convertir un "me gusta esto" en algo que un modelo, un fotógrafo o un editor pueda ejecutar.

## Regla de oficio

**"Me gusta" no es una instrucción.**

Todos los moodboards dicen lo mismo: "esta vibra". Pero la vibra está hecha de decisiones concretas: dónde está la cámara, de qué color son las sombras, cuánto dura cada plano. Esta skill desarma la referencia hasta encontrar esas decisiones, les pone nombre y las vuelve a armar como una receta que se puede usar con otro sujeto, otra marca y otra historia.

## Input

- La referencia: imagen, captura, link o video. Si es descripción, se trabaja con eso y se avisa que el análisis es menos fino.
- Qué le gusta al usuario de ella, si lo sabe. Ayuda a saber qué capa pesa más.
- Para qué la quiere usar: key visual, video, empaque, redes.

Si llegan varias referencias, se disecan una por una y al final se busca lo que comparten.

## Las capas

Cada referencia se separa en estas capas, siempre con estos nombres y en este orden:

1. **Encuadre.** Tamaño de plano, altura de cámara, dónde cae el sujeto, cuánto aire hay, proporción.
2. **Óptica.** Lente aparente, profundidad de campo, distorsión, enfoque.
3. **Luz.** Fuente, dirección, dureza, contraste, hora del día, de qué color son las sombras.
4. **Color.** Paleta dominante en tres a cinco tonos con nombre concreto, saturación, temperatura.
5. **Textura y soporte.** Grano, nitidez, digital o película, halación, imperfecciones.
6. **Dirección de arte.** Vestuario, objetos, locación, época que sugiere, qué está ausente a propósito.
7. **Movimiento** (solo video). Cámara fija o móvil, tipo de movimiento, velocidad, estabilidad.
8. **Edición** (solo video). Duración promedio de plano, tipo de corte, ritmo, transiciones.

Cada capa termina con una sola frase de **por qué funciona**: qué siente el espectador gracias a esa decisión.

## Proceso

1. **Mirar sin opinar.** Describir lo que hay, sin "bonito", "potente" ni "aesthetic".
2. **Disecar capa por capa.** Una decisión concreta por línea. Si una capa no tiene nada notable, se dice "neutra" y se sigue.
3. **Encontrar la capa dominante.** La que, si la quitas, la referencia deja de parecerse a sí misma. Casi siempre es una o dos.
4. **Separar ADN de accidente.** El ADN es lo que hace a la referencia reconocible. El accidente es el sujeto, la marca, el texto, la persona específica. El accidente no viaja.
5. **Escribir el ADN visual** como bloque de prompt en inglés, sin sujeto, para pegarlo antes de cualquier sujeto nuevo.
6. **Probar el ADN con un sujeto distinto.** Un ejemplo de prompt con algo que no tenga nada que ver con la referencia, para comprobar que el estilo viaja solo.

## Output

```
DISECAR REFERENCIAS · [nombre corto de la referencia]

LO QUE HAY
[Descripción en hechos, dos o tres frases.]

CAPAS
Encuadre: [decisiones] · Por qué funciona: [frase]
Óptica: ...
Luz: ...
Color: [tonos con nombre] · ...
Textura y soporte: ...
Dirección de arte: ...
Movimiento: [solo video]
Edición: [solo video]

CAPA DOMINANTE
[Cuál y por qué.]

LO QUE NO VIAJA
[Sujeto, marca, texto, persona, composición exacta.]

ADN VISUAL (bloque en inglés, sin sujeto)
[...]

PRUEBA CON OTRO SUJETO
[Prompt en inglés: ADN visual + un sujeto nuevo.]
```

## Anti-patrones

- **Etiquetas de moda.** "Estética Y2K" o "vibe cinematográfica" no describen nada. Se desarma la etiqueta en decisiones.
- **Nombrar al autor como receta.** Se describe lo que hace el estilo, nunca se pide "al estilo de" un artista vivo.
- **Confundir estética con idea.** Si el análisis empieza a hablar de qué quiere decir la pieza, se cambió de skill.
- **ADN que trae el sujeto pegado.** Si el bloque de prompt menciona a la persona o el producto original, no es ADN, es copia.

## Auto-revisión antes de entregar

1. ¿Cada capa tiene decisiones que se pueden ejecutar, no impresiones?
2. ¿El ADN visual funciona pegado antes de un sujeto que no tiene nada que ver?
3. ¿Alguien que ve la referencia y la prueba lado a lado diría "misma familia" y no "misma imagen"?

## Lo que no hace

- No extrae la idea ni el mecanismo creativo. Para eso está Robar como Artista.
- No analiza hooks, retención ni comentarios de un video. Para eso está ¿Por Qué Se Hizo Viral?
- No reproduce la pieza ni sus textos. Describe, nombra y recombina.

Hecha por Brontis_.
