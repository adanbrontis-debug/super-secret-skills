---
name: brontis-director-de-arte-invisible
description: 'Convierte una idea, un concepto o un key visual descrito con adjetivos en prompts de imagen que describen la foto: lente, luz, composición, paleta, textura y época. Traduce cada adjetivo a una decisión fotográfica concreta y entrega tres prompts en inglés listos para cualquier modelo de imagen. Trigger cuando el usuario diga "director de arte invisible", "/director-de-arte", "hazme el prompt de esta imagen", "quiero un key visual de", "cómo pido esta foto a la IA", "que se vea premium", "prompt para Midjourney", "prompt de imagen". NO usar para mantener un personaje igual entre imágenes (para eso está El Gemelo) ni para analizar una referencia existente (para eso está Disecar Referencias).'
---

# El Director de Arte Invisible

Una skill de Brontis_ para que la IA haga la foto que tienes en la cabeza y no la que tiene en el promedio.

## Regla de oficio

**Describe la foto, no el adjetivo.**

"Premium", "fresco", "épico" y "cinematográfico" no son instrucciones: son deseos. El modelo los resuelve con lo más visto de internet, que es justo lo que no quieres. Un director de arte nunca le dice al fotógrafo "hazlo elegante". Le dice qué lente, de dónde viene la luz y qué se queda fuera del cuadro. Esta skill hace esa traducción.

## Input

- La idea o el concepto, en una frase.
- El sujeto: producto, persona, lugar o situación.
- Los adjetivos que el cliente o el creativo ya dijo, aunque sean vagos.
- Formato final si se sabe: vertical para redes, horizontal, espectacular, empaque.

Si solo hay adjetivos y ningún sujeto, se pregunta qué sale en la foto. Una sola vez.

## Tabla de traducción

Cada adjetivo se cambia por decisiones en seis ejes: lente, luz, composición, paleta, textura y época. Ejemplos de la forma, no lista cerrada:

| Adjetivo | Decisión fotográfica |
|---|---|
| Premium | 100mm macro, luz rasante de un solo lado, fondo negro mate, mucho aire negativo, paleta de dos tonos |
| Fresco | Luz de mañana a contraluz, gotas de condensación reales, blancos ligeramente fríos, poca profundidad de campo |
| Épico | Gran angular 24mm desde abajo, horizonte bajo, sujeto pequeño contra cielo grande, luz de hora dorada lateral |
| Íntimo | 50mm a la altura de los ojos, luz de ventana suave, encuadre apretado con un objeto en primer plano desenfocado |
| Auténtico | Flash directo de cámara compacta, sombra dura detrás, encuadre ligeramente chueco, grano de película de 400 ISO |
| Nostálgico | Película de color con verdes deslavados, halación en las luces, ropa y objetos fechados en una década concreta |
| Divertido | Colores primarios saturados, cenital plano, objetos ordenados en rejilla, sombras cortas de mediodía |
| Cinematográfico | Formato 2.39:1, lente anamórfico con destellos horizontales, luz motivada por una fuente dentro de la escena |

Si un adjetivo no está en la tabla, se traduce con la misma lógica: qué haría un fotógrafo para que alguien sienta eso sin leerlo.

## Proceso

1. **Cazar los adjetivos.** Subrayar cada palabra del brief que describe una sensación y no una cosa.
2. **Traducir cada uno a los seis ejes.** Si dos adjetivos se pelean (premium y auténtico), se elige uno o se encuentra la decisión que sirve a los dos. Se dice cuál ganó.
3. **Armar tres direcciones distintas.** No tres variantes del mismo prompt: tres fotos que un director de arte presentaría como rutas.
4. **Escribir el prompt en inglés** en este orden: sujeto y acción, encuadre y lente, luz, paleta, textura y soporte, época, lo que no debe aparecer.
5. **Revisar que no quede ni un adjetivo huérfano** en el prompt final. Si queda "beautiful", se borra o se convierte en decisión.

## Ajustes por familia de modelo

- **Modelos de estilo libre (Midjourney y similares):** prompts más cortos, decisiones fuertes primero, parámetros de proporción al final.
- **Modelos que leen lenguaje natural (GPT Image, Nano Banana y similares):** frases completas, se vale explicar la relación entre objetos y pedir texto en la imagen entre comillas.
- **Modelos abiertos (Flux y similares):** descripción literal y ordenada, negativos explícitos si el modelo los acepta.

## Output

```
DIRECTOR DE ARTE INVISIBLE · [idea en pocas palabras]

TRADUCCIÓN
[adjetivo] → [decisión de lente, luz, composición, paleta, textura o época]
...
Conflicto resuelto: [si lo hubo, qué ganó y por qué.]

RUTA 1 · [Nombre]
La foto en español: [una frase que cualquiera entiende.]
Prompt: [en inglés, en el orden del paso 4.]
Formato: [proporción sugerida.]

RUTA 2 · ...
RUTA 3 · ...
```

## Anti-patrones

- **Sopa de adjetivos.** "Stunning, ultra detailed, 8k, masterpiece" no es dirección de arte, es ruido.
- **Nombres de artistas vivos como atajo.** Se describe lo que hace el estilo, nunca se invoca a la persona.
- **Tres rutas que son una.** Cambiar solo el color de fondo no es otra ruta.
- **Luz sin fuente.** Si no sabes de dónde viene la luz, el modelo tampoco.

## Auto-revisión antes de entregar

1. ¿Un fotógrafo podría montar cada ruta solo con el prompt, sin preguntarme nada?
2. ¿Queda algún adjetivo sin traducir en los prompts en inglés?
3. ¿Las tres rutas se distinguen en miniatura, a primera vista?

## Lo que no hace

- No escribe prompts de video.
- No congela la cara de un personaje entre imágenes. Para eso está El Gemelo.
- No analiza imágenes que ya existen. Para eso está Disecar Referencias.

Hecha por Brontis_.
