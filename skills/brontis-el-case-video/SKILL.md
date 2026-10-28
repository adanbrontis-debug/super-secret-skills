---
name: brontis-el-case-video
description: 'Arma el guion de un case video de dos minutos para festivales y premios, con estructura por segundos (contexto, problema, idea, ejecución, resultados, cierre), columnas de imagen y voz, y reglas para que los resultados sean creíbles y no inflados. Trigger cuando el usuario diga "el case video", "/case", "case para Cannes", "video caso", "case study para premios", "arma el case", "guion del case", "inscribir a festivales". NO usar para calificar si la pieza merece premio, para escribir spots ni para la retro interna de la campaña.'
---

# El Case Video

Una skill de Brontis_ para contar una campaña en dos minutos a alguien que ya vio doscientas hoy.

## Regla de oficio

**El jurado vota en el minuto uno.**

El jurado no ve el case completo con la misma atención. Si al segundo sesenta no entendió el problema y la idea, el resto es decorado. Esta skill pone la idea en una frase antes de la mitad, deja la ejecución para probarla y trata los resultados como evidencia, no como fuegos artificiales.

## Input

- La campaña: qué se hizo, dónde y cuándo.
- El problema real de negocio o de comunicación.
- Material disponible: piezas, fotos, video, reacciones, notas de prensa.
- Resultados con su fuente. Si no hay, se dejan huecos marcados.
- Categoría del festival, si se sabe. Cambia qué se enfatiza.

## Proceso

### Paso 1 · La frase de la idea
Antes de escribir una sola toma, la idea en una frase de máximo quince palabras. Si no sale, el case no está listo y se dice.

### Paso 2 · El reloj de 120 segundos

| Tiempo | Bloque | Lo que tiene que lograr |
|---|---|---|
| 0:00 a 0:10 | Contexto | Una tensión humana o cultural que cualquiera entienda. La marca todavía no aparece. |
| 0:10 a 0:25 | Problema | El obstáculo concreto. Si hay un dato, uno solo. |
| 0:25 a 0:45 | Idea | La frase de la idea dicha con todas sus letras antes del segundo 45. |
| 0:45 a 1:20 | Ejecución | Cómo se vivió. Imágenes de la pieza real y de la gente usándola, no de la agencia celebrando. |
| 1:20 a 1:45 | Resultados | Tres resultados máximo, el más fuerte primero. |
| 1:45 a 2:00 | Cierre | Una línea que redondea la idea y el logo. Nada de agradecimientos. |

Si el case es de 90 segundos, se recorta la ejecución, nunca la idea.

### Paso 3 · Reglas de resultados creíbles

- **Cada número tiene fuente.** Medición del cliente, estudio, plataforma o medio. Si no la tiene, no entra.
- **Comparar contra algo.** Contra el objetivo, el año pasado o la categoría. Un número solo no dice nada.
- **Conducta antes que alcance.** Ventas, registros, uso, cambio de opinión pesan más que impresiones.
- **Nada de equivalencia publicitaria.** "Tantos millones en medios ganados" es la cifra que más desconfianza genera.
- **Un número héroe.** El que el jurado va a repetir en la sala. Va grande y solo en pantalla.
- **Nunca inventar ni redondear hacia arriba.** Si falta un dato, se escribe `[DATO PENDIENTE: qué medir y de dónde]`.

### Paso 4 · Escribir en dos columnas
Imagen a la izquierda, voz o súper a la derecha. La voz no describe lo que se ve. Se escribe para leerse en voz alta en el tiempo asignado: unas dos o tres palabras por segundo.

## Output

```
EL CASE VIDEO · [campaña] · [duración]
La idea en una frase: [máximo quince palabras]
Categoría: [si aplica]

TIEMPO      IMAGEN                         VOZ / SÚPER
0:00-0:10   [qué se ve]                    [qué se dice]
0:10-0:25   ...                            ...
0:25-0:45   ...                            [aquí se dice la idea]
0:45-1:20   ...                            ...
1:20-1:45   [número héroe en pantalla]     ...
1:45-2:00   [cierre + logo]                [línea final]

RESULTADOS Y FUENTES
1. [resultado] · fuente: [...] · comparado contra: [...]
2. ...

RESULTADOS DESCARTADOS
[Qué se dejó fuera por vanidoso o sin fuente.]
```

## Anti-patrones

- **Arrancar con el logo.** El jurado deja de creer en el segundo uno.
- **La montaña de cifras.** Ocho números en pantalla se leen como inseguridad.
- **Impresiones como logro.** Que mucha gente pudo verlo no significa que algo cambió.
- **El testimonio fabricado.** Reacciones actuadas o citas inventadas descalifican el caso entero.
- **La voz épica.** Música de tráiler y "en un mundo donde..." ya son parodia.

## Auto-revisión antes de entregar

1. ¿La idea se dice completa antes del segundo 45?
2. ¿Cada resultado tiene fuente y punto de comparación?
3. ¿Si quito la música y la voz, las imágenes todavía cuentan el caso?

## Lo que no hace

- No inventa resultados ni testimonios. Marca los huecos y dice qué falta medir.
- No califica si la campaña merece metal.
- No hace el análisis interno de qué salió mal.

Hecha por Brontis_.
