---
name: brontis-memeificador
description: 'Adapta un mensaje o campaña de marca a formatos de meme. Explica la estructura de cada formato (qué hace cada panel o línea y por qué es gracioso), la respeta, propone varias versiones en formatos distintos con descripción de imagen y texto exacto, y filtra por vigencia porque los memes caducan rápido. Trigger cuando el usuario diga "memeificador", "/memeificador", "hazlo meme", "vuélvelo meme", "memes para la marca", "ideas de memes", "cómo lo meto en un meme", "contenido memero", "versión meme de la campaña". NO usar para copy de redes en general (eso es Hilo Fino), para entender por qué algo se hizo viral (eso es ¿Por Qué Se Hizo Viral?) ni para humor ofensivo.'
---

# Memeificador

Una skill de Brontis_ para que la marca entre al meme sin que el meme la escupa.

## Regla de oficio

**El meme se respeta o te come.**

Un meme es un formato con reglas tan estrictas como un soneto. Cada panel tiene un trabajo, cada línea tiene un ritmo, y la gente que lo usa todos los días nota de inmediato cuando alguien lo usa mal. Una marca que rompe la estructura, explica el chiste o llega tres meses tarde no hace un meme: hace un anuncio con fuente Impact. La marca no es el chiste. La marca es la que entendió el chiste.

## Input

- El mensaje o la campaña: qué quiere decir la marca, en una o dos frases.
- La marca, su tono y lo que nunca diría.
- El público: quién lo va a ver y en qué app.
- Formatos preferidos, si los hay. Si no, se eligen.

Si el mensaje no tiene una verdad reconocible para el público (una situación, una molestia, un gusto compartido), se dice antes de empezar. Sin verdad compartida no hay meme, solo hay marca hablando sola.

## Proceso

### Paso 1 · La verdad memeable
Encontrar la situación cotidiana que el público reconoce y que se conecta con la marca. No el beneficio del producto: la experiencia humana alrededor. "Abrir el refri tres veces esperando que aparezca algo nuevo" es memeable. "Sabor intenso" no.

### Paso 2 · Elegir formatos que le queden
Tres a cinco formatos distintos en estructura, no en apariencia: uno de comparación, uno de reacción, uno de escalada, uno de texto puro, etc. Para cada formato se escribe su **mecánica**: qué hace cada panel o línea y por qué la combinación da risa. Si no se puede explicar la mecánica en dos líneas, no se domina el formato y no se usa.

### Paso 3 · Llenar respetando la estructura
El texto entra en el molde sin deformarlo. Si el formato pide dos opciones y una reacción, son dos opciones y una reacción. Si el remate va en el último panel, va ahí. La marca aparece como contexto, objeto o pista, casi nunca como sujeto del chiste.

### Paso 4 · Filtro de vigencia
Los memes caducan en semanas. Se marca cada formato como **clásico** (lleva años vivo y aguanta), **vigente probable** o **riesgo de muerto**. Siempre se le pide al usuario que confirme que el formato sigue circulando antes de producir; si hay búsqueda web disponible, se sugiere revisar cuándo fue la última vez que se usó en su red.

### Paso 5 · Filtro de riesgo
Se revisa que ninguna versión use la cara de una persona real sin derechos, que no se burle de grupos, tragedias o personas concretas, y que no dependa de un meme con origen polémico.

## Output

```
MEMEIFICADOR · [marca o mensaje]

La verdad memeable: [una línea.]

[1] FORMATO: [nombre descriptivo del formato]
Mecánica: [qué hace cada panel o línea y por qué es gracioso.]
Imagen: [descripción de lo que se ve, panel por panel. Si usa personas, ilustración o casting propio.]
Texto exacto:
  Panel 1: "..."
  Panel 2: "..."
Dónde aparece la marca: [...]
Vigencia: [clásico / vigente probable / riesgo de muerto]

[2] ...
[3] ...

────────────
ANTES DE PUBLICAR
- Confirma que estos formatos siguen vivos en [red]: [lista].
- Derechos de imagen: [qué se tiene que producir o licenciar.]
```

## Anti-patrones

- **La marca como protagonista.** El meme donde el producto es el héroe que salva el día. Nadie lo comparte.
- **Explicar el meme.** Un caption que aclara el chiste lo mata. Si necesita explicación, no funciona.
- **Formatos muertos.** Usar el meme que todos dejaron de usar. Peor que no hacer meme.
- **Romper la estructura.** Agregar un panel, cambiar el orden, meter el logo en el remate.
- **Humor ofensivo.** Burlarse de gente, físicos, tragedias o grupos. Ni para "ser auténticos".
- **Caras ajenas.** Usar la foto de una persona real, viral o famosa, sin derechos. Se recrea con casting propio o ilustración.

## Auto-revisión antes de entregar

1. ¿Una persona que no sigue a la marca lo compartiría con un amigo sin sentir que comparte publicidad?
2. ¿Cada versión respeta la mecánica que yo mismo expliqué?
3. ¿Los formatos son distintos en estructura, no solo en imagen?
4. ¿Avisé cuáles pueden estar muertos y pedí confirmación?

## Lo que no hace

- No garantiza que un formato siga vivo. Eso lo confirma el usuario.
- No escribe el copy de cada red. Para eso está Hilo Fino.
- No analiza por qué un meme pegó. Para eso está ¿Por Qué Se Hizo Viral?
- No genera las imágenes; las describe para que alguien las produzca.

Hecha por Brontis_.
