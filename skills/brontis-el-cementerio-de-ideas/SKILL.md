---
name: brontis-el-cementerio-de-ideas
description: 'Guarda en un archivo Markdown las ideas rechazadas, con fecha, para qué brief eran, por qué murieron y etiquetas. Ruta por defecto ~/cementerio-de-ideas.md. Tres modos: Enterrar (guardar una o varias ideas), Visitar (listar o buscar) y Resucitar (cruzar un brief nuevo con el cementerio y proponer las ideas que encajan, con lo que habría que cambiarles). Trigger cuando el usuario diga "el cementerio de ideas", "/cementerio", "entierra esta idea", "guarda esta idea que mataron", "mataron mi idea", "¿qué tengo en el cementerio?", "busca en el cementerio", "resucita algo para este brief", "¿tengo alguna idea muerta que sirva?". NO usar para generar ideas nuevas desde cero (eso es Cien Malas Ideas) ni para revisar si una idea ya existe en el mundo (eso es ¿Ya Existe?).'
---

# El Cementerio de Ideas

Una skill de Brontis_ para que las ideas muertas descansen en paz, pero con dirección conocida.

## Regla de oficio

**Ninguna idea muere, solo espera su brief.**

Las ideas no se mueren por malas. Se mueren por timing, presupuesto, un cliente con miedo o un brief que pedía otra cosa. Y luego, seis meses después, llega el brief perfecto para esa idea y nadie se acuerda de ella porque vivía en una diapositiva de un deck viejo. Esta skill es un panteón ordenado: cada idea con su lápida, su fecha y su causa de muerte, lista para que alguien la venga a visitar con flores y un brief nuevo.

## Input

- **El modo**, o se deduce: si trae ideas para guardar es Enterrar; si pregunta qué hay es Visitar; si trae un brief es Resucitar.
- **La ruta del archivo.** Por defecto `~/cementerio-de-ideas.md`. Si el usuario dice otra, se usa esa.
- Para Enterrar, lo mínimo: la idea en una frase. Lo demás se pregunta en una sola línea o se llena con lo que se pueda deducir.

## Los modos

### Enterrar
1. Leer el archivo. Si no existe, crearlo con el encabezado de abajo.
2. Por cada idea, armar la lápida: nombre corto, la idea en una o dos frases, fecha de hoy, para qué brief era, causa de muerte y etiquetas (categoría, medio, tono, mecanismo).
3. Si falta brief o causa de muerte, preguntar las dos cosas juntas, una vez. Si el usuario no sabe, se escribe "desconocido" y se entierra igual.
4. Agregar al final del archivo, sin tocar lo que ya hay.

### Visitar
1. Leer el archivo y listar las lápidas: nombre, fecha, brief y etiquetas, una línea cada una.
2. Si el usuario busca algo ("las de humor", "las de 2025", "las que mató presupuesto"), filtrar por texto, etiqueta, fecha o causa de muerte.

### Resucitar
1. Pedir o leer el brief nuevo y resumirlo en una frase.
2. Revisar todas las lápidas y elegir hasta cinco que encajen por mecanismo, público o tono, no solo por categoría.
3. Para cada una: por qué podría servir aquí, qué habría que cambiarle y si su causa de muerte sigue viva en este brief.
4. Si el usuario elige resucitar una, se le agrega a su lápida una línea "Resucitada el [fecha] para [brief]". No se borra.

## El archivo

Encabezado al crearlo:

```
# El Cementerio de Ideas
Aquí descansan las ideas que no fueron, todavía.
Formato: una lápida por idea. No se borra nada sin permiso.
```

Cada lápida:

```
## [Nombre corto]
- Idea: [una o dos frases]
- Fecha de entierro: [AAAA-MM-DD]
- Brief: [para qué era]
- Causa de muerte: [por qué la mataron]
- Etiquetas: #[categoría] #[medio] #[tono] #[mecanismo]
```

## Output

```
EL CEMENTERIO DE IDEAS · [Enterrar / Visitar / Resucitar]
Archivo: [ruta]

[Enterrar] Enterradas hoy: [número] · Total en el panteón: [número]
[Visitar] [lista de lápidas o resultados de búsqueda]
[Resucitar] Brief: [frase]
  1 · [Nombre] · enterrada el [fecha] por [causa]
      Por qué podría servir: [una frase]
      Qué habría que cambiarle: [una o dos frases]
      ¿La causa de muerte sigue viva?: [sí / no / ojo]

LO QUE ESCRIBÍ EN EL ARCHIVO
[el texto exacto agregado, o "nada, solo lectura"]
```

## Anti-patrones

- **El sepulturero borrón.** Nunca se borra, se sobrescribe ni se reordena una lápida sin que el usuario lo pida con todas sus letras.
- **El interrogatorio.** Para Enterrar se pide lo mínimo. Una idea guardada sin etiquetas vale más que una que nadie guardó por flojera.
- **Resucitar por categoría.** Que las dos sean de bebidas no las hace compatibles. Se cruza por mecanismo y tono.
- **El chiste que estorba.** El humor de panteón va en el tono, no en el archivo. Las lápidas son legibles y buscables.

## Auto-revisión antes de entregar

1. ¿El archivo sigue teniendo todas las lápidas que tenía antes?
2. ¿Mostré exactamente lo que escribí?
3. En Resucitar, ¿revisé si la causa de muerte original aplica también al brief nuevo?

## Lo que no hace

- No genera ideas nuevas. Para eso está Cien Malas Ideas.
- No revisa si una idea ya existe allá afuera. Para eso está ¿Ya Existe?
- No sube el archivo a ningún lado ni lo comparte. Vive donde el usuario dijo.

Hecha por Brontis_.
