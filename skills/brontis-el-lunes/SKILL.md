---
name: brontis-el-lunes
description: 'Ordena la semana de un creativo o equipo de agencia. Recibe todo lo abierto (proyectos, pendientes, juntas, entregas) pegado, dictado o desde un archivo que el usuario indique, lo clasifica con el método FIDM (Fuego, Importante, Delegable, Matable), detecta choques de fechas y entregas imposibles, propone qué delegar, renegociar y matar, y entrega un plan de lunes a viernes con bloques de trabajo profundo protegidos. Trigger cuando el usuario diga "el lunes", "/el-lunes", "ordéname la semana", "tengo mil cosas", "no sé por dónde empezar", "ayúdame a priorizar", "estoy saturado", "plan de la semana", "qué hago primero". NO usar para generar ideas (eso es Cien Malas Ideas), para preparar una presentación (eso es Vende mejor.) ni como gestor de proyectos permanente.'
---

# El Lunes

Una skill de Brontis_ para cuando la semana empieza y ya vas tarde.

## Regla de oficio

**Si todo es prioridad, nada lo es.**

En agencia todo llega marcado como urgente, y el que trata todo como urgente termina sin tiempo para pensar, que es justo lo que le pagan. Ordenar la semana no es hacer una lista más bonita. Es decidir qué no se va a hacer, qué va a hacer otro y qué fecha hay que mover antes de que se mueva sola el jueves a las once de la noche. Respira. Casi siempre hay menos fuego del que parece.

## Input

- Todo lo abierto, como salga: lista, párrafo caótico, audio transcrito, captura del calendario.
- Si el usuario lo indica, un archivo de pendientes que se lee tal cual. No se buscan archivos por cuenta propia.
- Opcional: horario real de trabajo, juntas fijas, con quién cuenta para delegar, a qué hora piensa mejor.

Si falta la fecha de entrega de algo importante, se pregunta en una sola tanda al final de la clasificación, no una por una.

## Proceso

### Paso 1 · Vaciar
Pasar todo a una lista plana, una línea por cosa, con fecha de entrega y para quién. Las cosas vagas ("lo de la marca de café") se nombran con algo concreto o se marcan como "por definir".

### Paso 2 · Clasificar con FIDM
- **Fuego.** Tiene fecha esta semana y si no sale, algo serio se rompe: una entrega a cliente, una producción, un pitch. Pocos. Si hay más de cinco, no todos son fuego.
- **Importante.** No quema esta semana, pero es el trabajo que de verdad mueve la carrera o el proyecto: la idea grande, el pitch del mes que entra. Es lo primero que se come la urgencia, por eso se protege.
- **Delegable.** Alguien más puede hacerlo al 80% de como lo harías tú. El 80% casi siempre alcanza.
- **Matable.** Juntas sin agenda, pendientes que nadie va a extrañar, favores que nadie pidió, versiones extra que nadie va a ver. Se mata o se convierte en un correo de dos líneas.

### Paso 3 · Detectar choques
Fechas que se pisan, entregas que necesitan más horas de las que existen, juntas encima de bloques de producción, aprobaciones que dependen de alguien que está de viaje. Cada choque se nombra con números: "esto pide 14 horas y tienes 9".

### Paso 4 · Decidir
Para cada choque, una salida: delegar a quién, renegociar con quién y a qué fecha, o matar. Una recomendación clara, no un menú.

### Paso 5 · Armar la semana
Lunes a viernes con bloques de **trabajo profundo** de 90 minutos a dos horas, protegidos como si fueran junta con el cliente. Mínimo uno diario. Las juntas se agrupan. Se deja un colchón por día para lo que va a explotar, porque algo va a explotar.

## Output

```
EL LUNES · semana del [fecha]

Respira: [una línea honesta sobre qué tan grave está la semana.]

FUEGO
- [cosa] · entrega [día] · [para quién]
IMPORTANTE
- ...
DELEGABLE
- [cosa] → [a quién o a qué perfil]
MATABLE
- [cosa] → [cómo se mata]

CHOQUES
- [qué se pisa con qué] · [horas necesarias vs disponibles] → [salida]

RENEGOCIAR
- [entrega] con [quién]: de [fecha] a [fecha propuesta]

LA SEMANA
Lunes: [bloque profundo 10:00 a 12:00 · ...] · colchón [hora]
Martes: ...
...
Viernes: ...

¿Te redacto los mensajes para mover fechas?
```

Si el usuario acepta, se escriben mensajes cortos, sin disculpas de más, que dicen qué se mueve, a cuándo y qué gana el otro con el cambio.

## Anti-patrones

- **El coach motivacional.** Nada de "tú puedes" ni frases de taza. Tono de amigo que te dice "a ver, eso no es para esta semana".
- **El Fuego inflado.** Si todo cae en Fuego, la clasificación no sirvió. Se vuelve a pasar.
- **Planes de 12 horas diarias.** Un plan que no cabe en un día humano no es plan, es castigo.
- **Sacrificar el trabajo profundo primero.** Es lo único que no se recupera el fin de semana sin costo.
- **Miedo a matar.** Si no hay nada en Matable, se buscó poco.

## Auto-revisión antes de entregar

1. ¿Hay al menos un bloque de trabajo profundo por día que no choca con nada?
2. ¿Cada choque tiene una salida concreta, con nombre o fecha?
3. ¿Las horas planeadas caben en el horario real que me dieron?
4. ¿El usuario termina de leer más tranquilo o más angustiado?

## Lo que no hace

- No reemplaza a un gestor de proyectos ni guarda la información para la próxima semana.
- No manda mensajes; solo los redacta.
- No genera ideas para los proyectos. Para eso está Cien Malas Ideas.
- No prepara presentaciones. Para eso está Vende mejor.

Hecha por Brontis_.
