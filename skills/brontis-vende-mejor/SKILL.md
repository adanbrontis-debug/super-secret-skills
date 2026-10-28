---
name: brontis-vende-mejor
description: 'Prepara la defensa de una idea creativa antes de presentarla: mapea los miedos del cliente (riesgo, costo, jefe, marca, tiempo) y arma para cada uno un argumento, una prueba y una respuesta corta, defendiendo el problema que la idea resuelve y no la idea. Trigger cuando el usuario diga "vende mejor", "/vende-mejor", "blinda esta idea", "cómo defiendo esta idea", "qué me van a objetar", "prepara la defensa", "el cliente va a decir que es muy arriesgado", "argumentos para vender la idea", "me van a matar la idea". NO usar para estructurar la presentación, para ensayar en vivo (eso es El Cliente Imposible) ni para interpretar comentarios que ya llegaron (eso es Traductor de Feedback).'
---

# Vende mejor.

Una skill de Brontis_ para defender una idea sin suplicar por ella.

## Regla de oficio

**Defiende el problema que resuelve, no la idea.**

Cuando defiendes la idea, la conversación es sobre gustos y el cliente siempre gana en gustos: es su dinero. Cuando defiendes el problema, la conversación es sobre negocio y ahí la idea es solo la mejor herramienta disponible. "Es que está muy bonita" es rogar. "Tu gente dejó de abrir los correos de promoción y esto les llega por otro lado" es vender. Si el cliente mata la idea pero sigue de acuerdo con el problema, perdiste una batalla, no la cuenta.

## Input

- La idea, explicada como se la vas a contar al cliente.
- El problema o el brief que la originó.
- Quién decide y quién influye: puestos, historial, qué les han aprobado o rechazado antes.
- Lo que ya se sabe que preocupa al cliente, si se sabe.

Si no está claro el problema que resuelve la idea, la skill se detiene ahí y lo pregunta. Sin problema no hay defensa, solo cariño.

## Los cinco miedos

Casi toda objeción de cliente es uno de estos cinco miedos disfrazado.

1. **Riesgo.** "¿Y si sale mal?" Miedo a la crítica en redes, a la prensa, a que nadie entienda.
2. **Costo.** "¿Y si no vale lo que cuesta?" No solo dinero: horas de su equipo, permisos, producción.
3. **Jefe.** "¿Cómo se lo explico a arriba?" El cliente en la sala casi nunca es el que decide al final. Hay que darle las palabras para vender hacia adentro.
4. **Marca.** "¿Esto somos nosotros?" Miedo a romper los lineamientos, a parecer otra marca, a que el equipo global se enoje.
5. **Tiempo.** "¿Llegamos?" Fechas de lanzamiento, aprobaciones legales, temporada.

## Proceso

1. **Escribir el problema en una frase** que el cliente firmaría sin pensarlo. Esa frase es el ancla de toda la defensa.
2. **Conectar idea y problema** en una cadena de tres eslabones: el problema, por qué lo de siempre no lo resuelve, por qué esta idea sí.
3. **Mapear los miedos.** Para cada uno de los cinco: qué tan probable es que salga con este cliente (alto, medio, bajo) y cómo lo va a decir textualmente.
4. **Armar la respuesta a cada miedo** con tres piezas: un argumento que regresa al problema, una prueba (dato, precedente, piloto, plan B) y una versión corta de una frase para decir en la sala.
5. **Preparar la concesión.** Qué se puede ceder sin que la idea muera, y qué no se negocia. Saber esto antes de entrar evita ceder lo esencial por nervios.
6. **Escribir el guion para el jefe.** Tres frases que el cliente puede repetir arriba sin nosotros presentes.

## Output

```
VENDER SIN ROGAR · [idea]

EL PROBLEMA (el ancla): [una frase]
LA CADENA: [problema] → [por qué lo de siempre falla] → [por qué esto sí]

MAPA DE MIEDOS
[Miedo] · Probabilidad: [alta/media/baja]
  Cómo lo va a decir: "[frase textual probable]"
  Argumento: [regresa al problema]
  Prueba: [dato, precedente o plan B]
  En la sala: "[respuesta de una frase]"
(los cinco, ordenados de más a menos probable)

LO QUE SE PUEDE CEDER: [lista corta]
LO QUE NO SE NEGOCIA: [una o dos cosas, con el porqué]

PARA QUE LO VENDA ARRIBA
"[tres frases que el cliente puede repetir]"
```

## Anti-patrones

- **Defender con adjetivos.** "Es muy disruptiva" no responde ningún miedo.
- **Contestar el miedo equivocado.** Si el cliente dice "es cara" y lo que teme es a su jefe, bajar el costo no cierra nada.
- **Ganar la discusión, perder al cliente.** Humillar una objeción en la sala crea un enemigo en el comité.
- **Datos inventados.** Una prueba falsa descubierta mata la idea y la relación. Si no hay dato, se dice y se propone cómo conseguirlo.
- **Ceder todo a la primera.** Si todo se puede negociar, la idea no tenía columna.

## Auto-revisión antes de entregar

1. ¿Cada respuesta regresa al problema o alguna está defendiendo el gusto?
2. ¿El miedo al jefe tiene guion propio? Es el que más ideas mata y el que menos se prepara.
3. ¿Está claro qué no se negocia y por qué?

## Lo que no hace

- No estructura la presentación.
- No ensaya la junta en vivo. Para eso está El Cliente Imposible.
- No interpreta comentarios que ya llegaron. Para eso está Traductor de Feedback.
- No evalúa si la idea es buena.

Hecha por Brontis_.
