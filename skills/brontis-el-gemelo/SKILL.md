---
name: brontis-el-gemelo
description: 'Construye la biblia de un personaje para generarlo con IA sin que cambie de cara entre imágenes o tomas. Separa un canon congelado (rasgos que nunca cambian, descritos siempre con las mismas palabras exactas) de módulos variables (vestuario, pose, expresión, escenario) y entrega una hoja de referencia lista para generar. Trigger cuando el usuario diga "el gemelo", "/gemelo", "biblia de personaje", "que no le cambie la cara", "personaje consistente", "character sheet", "mascota de la marca con IA", "el mismo personaje en varias tomas". NO usar para inventar la idea del personaje desde cero (para eso está Cien Malas Ideas) ni para imágenes sueltas sin personaje fijo (para eso está El Director de Arte Invisible).'
---

# El Gemelo

Una skill de Brontis_ para que el personaje de la toma uno sea el mismo de la toma veinte.

## Regla de oficio

**Primero se congela el canon, luego se juega.**

Los modelos no recuerdan a nadie. Cada vez que generas, el personaje nace de nuevo a partir de las palabras que le diste. Si cambias "ojos color miel" por "ojos cafés claros", cambiaste de persona. La consistencia no sale de la herramienta: sale de repetir exactamente lo mismo, siempre, y de saber qué partes se pueden mover sin romper al personaje.

## Input

- Quién es el personaje: humano, mascota, objeto con cara, criatura.
- Para qué se va a usar: campaña de imágenes, video, redes, empaque.
- Referencias visuales o una descripción, aunque sea floja.
- Lo que ya se generó y sí gustó, si existe. Eso manda sobre la descripción.

Si el personaje todavía no tiene forma, se proponen tres siluetas en una frase cada una y se elige antes de construir la biblia.

## Proceso

1. **Elegir la silueta.** Lo que se reconoce en negro, a contraluz. Si la silueta no es distinguible, ningún detalle lo va a salvar.
2. **Congelar el canon.** Entre seis y diez rasgos que nunca cambian: proporción, forma de la cara o del cuerpo, color exacto de piel, pelaje o material, ojos, pelo, una marca distintiva. Cada rasgo se escribe una sola vez, en inglés, y esa frase ya no se toca.
3. **Escribir la frase canon.** Todos los rasgos congelados unidos en un solo bloque de texto. Ese bloque se pega idéntico en cada prompt, al principio, sin parafrasear.
4. **Definir los módulos variables.** Cuatro cajones: vestuario, pose, expresión y escenario. Cada uno con tres a cinco opciones descritas también con palabras fijas.
5. **Marcar las zonas prohibidas.** Lo que nunca se pone al personaje porque lo deforma: accesorios que tapan el rasgo distintivo, ángulos donde pierde la silueta, estilos que le cambian la proporción.
6. **Armar la hoja de referencia.** Un prompt para una lámina con el personaje de frente, perfil, tres cuartos y espalda, fondo neutro, misma luz. Esa imagen se vuelve la referencia de todo lo que sigue.
7. **Probar con tres combinaciones** de módulos muy distintas y revisar si sigue siendo el mismo.

## Ajustes por familia de modelo

- **Modelos con referencia de imagen o de personaje:** se sube la hoja de referencia y aun así se pega la frase canon. Las dos juntas rinden más que cualquiera sola.
- **Modelos de video:** se genera primero el cuadro fijo con el personaje correcto y se anima desde ahí. Nunca se le pide al video que invente la cara.
- **Modelos sin referencia de imagen:** la frase canon es todo lo que hay. Se protege como contraseña.

## Output

```
EL GEMELO · [nombre del personaje]

SILUETA
[Una frase.]

CANON CONGELADO (no se edita, no se parafrasea)
1. [rasgo en inglés]
...
FRASE CANON: [bloque completo en inglés, para pegar idéntico.]

MÓDULOS VARIABLES
Vestuario: A [..] · B [..] · C [..]
Pose: A [..] · B [..] · C [..]
Expresión: A [..] · B [..] · C [..]
Escenario: A [..] · B [..] · C [..]

ZONAS PROHIBIDAS
[Lo que lo rompe.]

HOJA DE REFERENCIA
Prompt: [en inglés.]

FÓRMULA DE USO
[FRASE CANON] + [vestuario] + [pose] + [expresión] + [escenario] + [luz y encuadre]
Ejemplo: [un prompt armado con la fórmula.]
```

## Anti-patrones

- **El sinónimo creativo.** Reescribir el canon "para que suene mejor". Cada palabra distinta es una persona distinta.
- **Canon de veinte rasgos.** Demasiados detalles y el modelo empieza a soltar algunos al azar.
- **Rasgos que no se ven.** "Valiente" o "simpático" no son canon. Van, si acaso, en expresión.
- **Variar todo a la vez.** Cambiar vestuario, escenario y estilo en la misma imagen y luego preguntarse por qué ya no se parece.
- **Parecido a alguien real.** El personaje no se construye sobre la cara de una persona existente.

## Auto-revisión antes de entregar

1. ¿La frase canon es idéntica en la hoja de referencia y en el ejemplo?
2. ¿Puedo reconocer al personaje solo por su silueta y un rasgo?
3. ¿Algún módulo variable contradice el canon? Si sí, el módulo se va.

## Lo que no hace

- No inventa el concepto del personaje desde cero. Para eso está Cien Malas Ideas.
- No escribe las tomas de video. Para pasar un guion a cuadros está Storyboard Express.
- No garantiza consistencia perfecta: la reduce mucho. Siempre se revisa con ojo humano.

Hecha por Brontis_.
