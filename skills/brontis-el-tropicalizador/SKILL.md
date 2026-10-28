---
name: brontis-el-tropicalizador
description: 'Adapta una campaña, guion o copy hecho para un país o región a otro mercado (España a México, Estados Unidos a Latinoamérica, CDMX a Monterrey o a Colombia). Revisa en capas nombradas: idioma, cultura, humor, gestos, colores y símbolos, fechas, casting y asuntos sensibles, y entrega una tabla de cambios con el porqué más una lista de "esto allá significa otra cosa". Trigger cuando el usuario diga "el tropicalizador", "/tropicalizador", "tropicalízalo", "adáptalo a México", "esto viene de España", "localiza esta campaña", "cómo funcionaría en Colombia", "pásalo a otro mercado", "versión para Latam". NO usar para traducir palabra por palabra, para adaptar a cada red social (eso es Hilo Fino) ni para recortar (eso es Tijera).'
---

# El Tropicalizador

Una skill de Brontis_ para que la campaña no llegue al otro país hablando con acento de doblaje.

## Regla de oficio

**Traducir no es adaptar.**

Una campaña traducida dice las mismas palabras. Una campaña adaptada provoca la misma reacción. En España "coger el autobús" es inocente; en México es otra cosa. Un pulgar arriba es saludo en un país y grosería en otro. El chiste de fútbol que mata en Buenos Aires no existe en Monterrey, donde el clásico es otro. Esta skill no busca sinónimos: busca que la idea sobreviva al viaje, aunque para eso haya que cambiarle la ropa, el chiste y hasta la fecha de estreno.

## Input

- La pieza: guion, copy, key visual descrito, storyboard, campaña completa.
- **Mercado de origen y mercado de destino.** Sin los dos no se arranca. Si falta uno, se pregunta en una línea. "Latam" no es un mercado; si dicen Latam, se pregunta por qué países empezar.
- El público objetivo en destino, si cambia respecto al original.
- Lo intocable: tagline global, nombre de producto, legales, elementos de marca.

## Proceso

Antes de tocar nada, se escribe en una línea **qué reacción busca la pieza original**. Esa reacción es lo que tiene que llegar intacto. Después, ocho capas en orden.

1. **Capa del idioma.** Modismos, groserías involuntarias, falsos amigos, tuteo o ustedeo, vosotros que no existen, diminutivos. Se revisa también el registro: lo que en origen suena casual puede sonar fresa o naco en destino.
2. **Capa de las referencias.** Celebridades, programas, comida, marcas locales, lugares, dichos. Si la referencia no existe en destino, se busca su equivalente funcional, no su traducción.
3. **Capa del humor.** Ironía, albur, autodesprecio, exageración. Cada país se ríe distinto. Si el chiste depende de un juego de palabras, casi siempre hay que escribir otro chiste que logre lo mismo.
4. **Capa del cuerpo.** Gestos, saludos, distancia entre personas, contacto físico, manos en la imagen. Un gesto inocente en origen puede ser ofensivo en destino.
5. **Capa de colores y símbolos.** Colores asociados a partidos, equipos, luto o religión. Números de mala suerte, animales con doble lectura, banderas, escudos.
6. **Capa del calendario.** Temporadas invertidas entre hemisferios, días festivos, regreso a clases, quincenas, aguinaldo, fechas comerciales que en destino no existen o caen otro mes.
7. **Capa del casting y el contexto.** Quién sale, cómo se ve, cómo habla, dónde vive, qué casa tiene, qué coche maneja. Si el casting de origen se lee extranjero o aspiracional de más en destino, se dice.
8. **Capa de lo delicado.** Política, religión, violencia, migración, clasismo, racismo, temas regionales. Lo que en origen es neutro en destino puede estar en la nota roja de esta semana.

Cada hallazgo lleva un **nivel de confianza**. Si es alto, se adapta. Si es medio o bajo, se marca **"validar con alguien local"** y se dice qué preguntarle. La skill sabe mucho, pero no vive allá.

## Output

```
EL TROPICALIZADOR · [pieza] · [origen] → [destino]

Reacción que tiene que llegar: [una línea.]

TABLA DE CAMBIOS
| Capa | Original | Adaptación | Por qué | Confianza |
|---|---|---|---|---|
| Idioma | "..." | "..." | [...] | alta |
| Humor | [...] | [...] | [...] | media · validar |

ESTO ALLÁ SIGNIFICA OTRA COSA
- [palabra, gesto o símbolo]: en [origen] significa [...]; en [destino] se lee [...].

VALIDAR CON ALGUIEN LOCAL
- [punto] → pregunta concreta: [...]

LO QUE NO SE TOCÓ Y POR QUÉ
- [elemento]: viaja bien porque [...].

PIEZA ADAPTADA
[texto o guion completo ya tropicalizado]
```

Si el usuario pide formato corto, se entrega solo la tabla de cambios y la lista de "esto allá significa otra cosa".

## Anti-patrones

- **El español neutro.** Quitarle todo el sabor para que funcione en todos lados. No funciona en ninguno.
- **El disfraz folclórico.** Meter mariachi, tacos o sombrero para "hacerlo mexicano". Eso es caricatura, no adaptación.
- **El sinónimo como solución.** Cambiar "ordenador" por "computadora" y dar por adaptado un guion cuyo chiste no se entiende.
- **Inventar certezas.** Afirmar cómo se usa una palabra en Barranquilla sin estar seguro. Si hay duda, se marca para validar.
- **Ignorar regiones.** México no es CDMX. Colombia no es Bogotá. Si la pieza va a una región, se adapta a esa región.

## Auto-revisión antes de entregar

1. ¿Alguien de destino que nunca vio el original diría que la pieza se hizo para él?
2. ¿Revisé las ocho capas, aunque alguna haya salido limpia?
3. ¿Cada cambio tiene un porqué que no sea "suena mejor"?
4. ¿Marqué para validación todo lo que no sé con certeza?

## Lo que no hace

- No traduce entre idiomas distintos al español como trabajo principal; si la pieza viene en inglés, la adapta, pero no sustituye a un traductor profesional.
- No adapta el copy a cada red social. Para eso está Hilo Fino.
- No recorta textos. Para eso está Tijera.
- No reemplaza la validación de alguien que vive en el mercado de destino.

Hecha por Brontis_.
