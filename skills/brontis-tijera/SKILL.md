---
name: brontis-tijera
description: 'Recorta cualquier copy a la mitad, o a la extensión que se pida, sin perder la idea. Trabaja en pasadas nombradas (relleno, redundancia, adjetivos, voz pasiva, rodeos, la frase favorita) y entrega el conteo de palabras de cada una. Trigger cuando el usuario diga "tijera", "/tijera", "córtalo a la mitad", "está muy largo", "recórtalo", "hazlo más corto", "quítale paja", "déjalo en X palabras", "no cabe", "sintetiza este texto". NO usar para escribir copy desde cero (para copy de redes está Hilo Fino) ni para cambiar la idea del texto.'
---

# Tijera

Una skill de Brontis_ para que un texto diga lo mismo con la mitad de palabras.

## Regla de oficio

**Cada palabra paga renta o se va.**

Un copy largo casi nunca es largo porque tenga mucho que decir. Es largo porque nadie se atrevió a cortar. Cada palabra ocupa espacio en la cabeza del lector, y el lector no tiene paciencia. Si una palabra no aporta información, ritmo o tono, no se queda por cortesía. Lo que se corta no se pierde: se deja de estorbar.

## Input

- El texto.
- La meta: la mitad por defecto, o un número exacto de palabras o caracteres.
- Dónde vive: espectacular, cuerpo de anuncio, correo, post, guion, presentación. Cambia lo que se puede sacrificar.
- Lo intocable, si existe: legales, nombre del producto, una frase aprobada por el cliente.

Si no se dice la meta, se corta a la mitad. Si el texto ya es corto, se avisa y se corta de todos modos lo que sobre.

## Proceso

Antes de cortar, se escribe en una línea **qué dice el texto**. Esa línea es lo único que no se puede perder. Después, seis pasadas en orden. Cada una tiene su conteo.

1. **Pasada del relleno.** Fuera muletillas y arranques vacíos: "cabe mencionar que", "es importante destacar", "en este sentido", "sin duda alguna", "hoy en día", "el día de hoy". Fuera el saludo y la despedida si no hacen falta.
2. **Pasada del eco.** Si algo se dice dos veces con distintas palabras, se queda la versión más concreta. Incluye los pares inútiles: "único y exclusivo", "rápido y ágil", "calidad y excelencia".
3. **Pasada de los adjetivos.** Cada adjetivo se pone a prueba: si se quita, ¿cambia lo que el lector entiende? Si no cambia, se va. "Increíble", "innovador", "único" y "completo" casi nunca sobreviven. Un dato concreto le gana a tres adjetivos.
4. **Pasada de los verbos de cartón.** "Realizar una compra" es "comprar". "Llevar a cabo" es "hacer". "Se ofrece la posibilidad de" es "puedes". La voz pasiva pasa a activa.
5. **Pasada del rodeo.** Frases enteras que preparan lo que viene en vez de decirlo. Se empieza por lo importante y se borra el calentamiento. Muchas veces el texto mejora si se borra el primer párrafo completo.
6. **Pasada de la frase favorita.** Se identifica la frase de la que el autor está más orgulloso y se pregunta si el texto funciona sin ella. Si funciona, se va. Si no, se queda y se le corta un tercio.

Si después de las seis pasadas no se llegó a la meta, se revisa qué idea secundaria se puede sacrificar y se le pregunta al usuario cuál, en una línea.

## Output

```
TIJERA · [de dónde viene el texto]

Lo que dice: [una línea.]
Meta: [número de palabras o la mitad]

ANTES ([número] palabras)
[texto original]

DESPUÉS ([número] palabras · [porcentaje] menos)
[texto recortado]

LAS PASADAS
Relleno: -[número] · [ejemplo de lo cortado]
Eco: -[número] · [ejemplo]
Adjetivos: -[número] · [ejemplo]
Verbos de cartón: -[número] · [ejemplo]
Rodeo: -[número] · [ejemplo]
Frase favorita: [cuál era y qué pasó con ella]

Lo que se sacrificó: [ideas secundarias que salieron, si alguna.]
```

Si el usuario pide formato corto, se entrega solo el texto recortado con el conteo antes y después.

## Anti-patrones

- **El telegrama.** Quitar artículos y conectores hasta que el texto suena a robot. Cortar no es mutilar: el texto tiene que seguir leyéndose como lo escribió una persona.
- **El sinónimo corto.** Cambiar palabras por otras más cortas no es cortar. Se cortan ideas sobrantes, no letras.
- **Cortar el tono.** Si el texto era cálido o tenía humor, la versión corta también. La voz no es relleno.
- **Tocar lo intocable.** Legales, nombres y frases aprobadas no se mueven sin avisar.
- **Cambiar la idea.** Si lo que dice el texto cambió, no fue un recorte, fue una reescritura.

## Auto-revisión antes de entregar

1. ¿La línea de "lo que dice" se cumple igual en la versión corta?
2. Leída en voz alta, ¿suena natural o suena a telegrama?
3. ¿Queda alguna palabra que pueda quitar sin que nadie lo note? Si sí, se quita.

## Lo que no hace

- No escribe copy nuevo. Para adaptar un mensaje a redes está Hilo Fino.
- No ajusta guiones a duración por segundos.
- No traduce comentarios del cliente sobre el texto. Para eso está Traductor de Feedback.

Hecha por Brontis_.
