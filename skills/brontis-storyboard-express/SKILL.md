---
name: brontis-storyboard-express
description: 'Pasa un guion de spot o video a storyboard descrito: cuadros numerados con encuadre, acción, duración, audio y un prompt de imagen por cuadro, listos para generar con IA. Incluye la prueba de que la historia se entienda sin audio. Trigger cuando el usuario diga "storyboard express", "/storyboard", "pásalo a storyboard", "hazme el story", "cuadros del guion", "frames para el spot", "storyboard con IA", "necesito el story para la junta". NO usar para escribir el guion, para prompts de video en movimiento ni para diseñar la presentación.'
---

# Storyboard Express

Una skill de Brontis_ para que el guion llegue a la junta con imágenes y no con imaginación.

## Regla de oficio

**Si no se entiende sin audio, el cuadro está mal.**

La mayoría de la gente ve los videos con el sonido apagado, y el cliente ve el storyboard sin locutor. Un cuadro que solo funciona porque alguien lo explica no está contando nada. Esta skill obliga a que cada cuadro diga su parte con la imagen, y deja al audio el trabajo de sumar, no de rescatar.

## Input

- El guion: con video y audio separados o como texto corrido.
- Duración total del spot.
- Formato final: 16:9, 9:16, 1:1.
- Personajes o producto con descripción fija, si existen. Si hay una biblia de El Gemelo, se usa.

Si el guion no trae duración, se asume 30 segundos y se dice.

## Proceso

1. **Partir el guion en momentos.** Un momento es lo que cambia en la cabeza del espectador. Un spot de 30 segundos suele tener entre 8 y 14 cuadros.
2. **Repartir el tiempo.** Cada cuadro lleva duración en segundos. La suma tiene que dar el total exacto. Los primeros tres segundos y el cierre de marca se protegen siempre.
3. **Elegir encuadre por cuadro.** Tamaño de plano y ángulo. Variar el tamaño entre cuadros seguidos: dos planos medios iguales en fila se leen como error.
4. **Describir la acción visible.** Lo que la cámara ve, no lo que el personaje piensa. "Duda" no se ve. "Detiene la mano a medio camino de la perilla" sí.
5. **Separar el audio.** Locución, diálogo, música y efecto van en su propia línea. Nunca adentro de la acción.
6. **Correr la prueba sin audio.** Leer solo encuadres y acciones, de corrido. Anotar cada cuadro donde la historia se cae y rehacerlo con imagen, no con un súper.
7. **Escribir el prompt de imagen en inglés** por cuadro, como cuadro fijo: encuadre y lente, sujeto con descripción fija, acción congelada en su momento más claro, luz, estilo del story.

## Estilo del story

Se elige uno para todo el storyboard y se repite igual en cada prompt:

- **Boceto de lápiz:** para junta interna, se ve en proceso y nadie se enamora del casting.
- **Fotograma realista:** para cliente que necesita ver la película, con aviso de que no es la foto final.
- **Ilustración plana a color:** para animación o cuando importa más el ritmo que el realismo.

## Output

```
STORYBOARD EXPRESS · [título del spot]
Duración: [segundos] · Formato: [proporción] · Cuadros: [número] · Estilo: [uno]

CUADRO 01 · 0:00 a 0:03 · [3s]
Encuadre: [plano y ángulo.]
Acción: [lo que se ve.]
Audio: [locución, diálogo, música o efecto. Vacío si no hay.]
Prompt: [en inglés.]

CUADRO 02 · ...

PRUEBA SIN AUDIO
Se entiende: [sí o no, en una frase de qué cuenta la historia muda.]
Cuadros que fallaron y cómo se arreglaron: [número y cambio.]
```

## Anti-patrones

- **El cuadro que piensa.** Acciones internas que ninguna cámara puede ver.
- **El súper salvavidas.** Resolver con texto en pantalla lo que la imagen no logró contar.
- **Packshot de cinco segundos.** El cierre de marca se gana, no se estira.
- **Tiempos que no suman.** Si los cuadros dan 34 segundos, el spot no cabe.
- **Personaje distinto en cada cuadro.** Si no se repite la descripción fija, el modelo inventa otra persona.

## Auto-revisión antes de entregar

1. ¿Las duraciones suman el total exacto?
2. Si le enseño solo las imágenes a alguien ajeno, ¿me cuenta la historia de regreso?
3. ¿El producto o la marca aparece en un cuadro donde la imagen lo justifica, no solo al final?

## Lo que no hace

- No escribe ni corrige el guion.
- No escribe prompts de video con movimiento.
- No diseña el deck de presentación.

Hecha por Brontis_.
