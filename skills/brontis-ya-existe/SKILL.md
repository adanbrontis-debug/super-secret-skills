---
name: brontis-ya-existe
description: 'Busca en internet campañas, piezas y proyectos parecidos a una idea y dice qué tan cerca está de algo que ya se hizo, con links reales. Busca por mecanismo y no solo por palabras clave, en español e inglés, separa parecido de mecanismo y parecido de forma, da un veredicto con escala (Libre, Pariente lejano, Primo, Gemelo) y si se parece mucho propone cómo alejarla. Trigger cuando el usuario diga "ya existe", "/ya-existe", "¿esto ya se hizo?", "¿alguien ya hizo esto?", "busca si hay algo parecido", "checa que no sea refrito", "antes de presentarla revisa", "¿es original?". NO usar para generar ideas desde cero (eso es Cien Malas Ideas), para adaptar una referencia que ya se conoce (eso es Robar como Artista) ni como búsqueda legal de propiedad intelectual.'
---

# ¿Ya Existe?

Una skill de Brontis_ para enterarte antes que el cliente de que tu idea ya ganó un león hace diez años.

## Regla de oficio

**Si lo pensaste en cinco minutos, alguien más también.**

Las ideas no se patentan en la cabeza. Si una idea salió fácil, lo más probable es que salió fácil para otros, en otro país, en otro año, con otra marca. No pasa nada: pasa algo malo solo si te enteras en la junta. Esta skill busca a los parientes de tu idea antes de que lleguen solos, y separa la coincidencia de forma, que se arregla con dirección de arte, de la coincidencia de mecanismo, que obliga a repensar.

## Input

- **La idea**, en una o varias frases. Mejor si dice qué pasa, no solo cómo se ve.
- Opcional: categoría, país, medio y para qué marca es.
- Opcional: referencias que el usuario ya sospecha. Se revisan primero.

Si la idea viene en puro adjetivo ("algo emotivo con abuelitos"), se pide en una línea qué pasa exactamente.

## Proceso

1. **Destilar.** Escribir la idea en una frase de hechos y, aparte, su **mecanismo**: la operación que la hace funcionar, sin marca ni medio. Ejemplo: "una marca de pan regala el pan que sobró a quien llegue después de cerrar" tiene como mecanismo "convertir el desperdicio de la marca en premio para el cliente tardío".
2. **Armar las búsquedas.** Entre seis y diez, mezclando tres tipos:
   - **Por mecanismo:** describen lo que pasa ("brand turns leftover product into reward", "marca regala lo que no vendió").
   - **Por forma:** el medio y la ejecución ("vending machine campaign", "activación con máquina expendedora").
   - **Por vitrina:** la idea más palabras como "campaign", "case study", "Cannes Lions", "D&AD", "Ojo de Iberoamérica", "caso".
   Siempre en español y en inglés. Si la categoría es fuerte en otro idioma, se agrega una búsqueda ahí.
3. **Buscar y leer.** Usar WebSearch para cada búsqueda y WebFetch para abrir los resultados que parezcan cercanos. No se juzga un caso por su titular: se lee qué hizo de verdad.
4. **Clasificar cada hallazgo** en dos ejes: ¿comparte el mecanismo? ¿comparte la forma?
5. **Dar veredicto** con la escala de abajo, según el hallazgo más cercano.
6. **Si es Primo o Gemelo, proponer cómo alejarla:** tres giros concretos que cambian el mecanismo, no solo el color.

## La escala

- **Libre.** No apareció nada con el mismo mecanismo. Puede haber cosas con forma parecida, sin pena.
- **Pariente lejano.** Hay piezas que tocan el mismo territorio o insight, pero hacen otra cosa con él.
- **Primo.** Mismo mecanismo con otra forma, o misma forma con otro mecanismo. Se puede presentar, pero alguien en la sala lo va a decir.
- **Gemelo.** Mismo mecanismo y forma muy parecida. Presentarla así es regalar la objeción.

## Output

```
¿YA EXISTE? · [la idea en pocas palabras]

LA IDEA: [frase de hechos]
EL MECANISMO: [la operación, sin marca ni medio]

VEREDICTO: [Libre / Pariente lejano / Primo / Gemelo]
[Una o dos frases de por qué.]

LO QUE ENCONTRÉ
1 · [Nombre del caso] · [marca, año, país si se sabe]
    [Qué hizo, en una frase de hechos.]
    Mecanismo: [igual / parecido / distinto] · Forma: [igual / parecida / distinta]
    Link: [URL real]
2 · ...

CÓMO ALEJARLA (solo si es Primo o Gemelo)
- [Giro 1: qué cambia del mecanismo]
- [Giro 2]
- [Giro 3]

BÚSQUEDAS QUE HICE: [lista corta, en los dos idiomas]
Ojo: no encontrar algo no garantiza que no exista.
```

## Anti-patrones

- **Inventar casos o links.** Si no hay link que se haya abierto o visto en resultados, el caso no va. Cero campañas "que suenan a que existieron".
- **Buscar solo palabras clave.** "Campaña abuelitos pan" encuentra lo obvio. El mecanismo encuentra al gemelo.
- **Confundir territorio con mecanismo.** Que otra marca también hable de familia no hace Gemelo a nadie.
- **El veredicto tibio.** Decir "hay cosas parecidas" sin nombrar el nivel de la escala no ayuda a decidir.
- **Alejar con maquillaje.** Cambiar el medio o la paleta no aleja un Gemelo. Se cambia lo que pasa.

## Auto-revisión antes de entregar

1. ¿Cada link se vio de verdad en esta sesión?
2. ¿Hice búsquedas por mecanismo en español y en inglés, no solo por forma?
3. ¿El veredicto coincide con el hallazgo más cercano, y no con el promedio?
4. Si no encontré nada, ¿lo dije así, con la advertencia?

## Lo que no hace

- No es una búsqueda legal de propiedad intelectual ni de derechos.
- No califica si la idea es buena. Una idea Libre puede ser mala y un Primo puede ser mejor que el original.
- No genera ideas nuevas desde cero. Para eso está Cien Malas Ideas.
- No adapta una referencia a otro brief. Para eso está Robar como Artista.

Hecha por Brontis_.
