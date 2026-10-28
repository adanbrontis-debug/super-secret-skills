---
name: brontis-por-que-se-hizo-viral
description: 'Disecciona un video de YouTube o Shorts para encontrar la mecánica de su éxito: hook, promesa, estructura, formato, disparador para compartir y lo que dicen los comentarios, comparado contra lo normal del canal. Funciona con un link, una transcripción o solo una descripción. Trigger cuando el usuario diga "¿por qué se hizo viral?", "/viral", "analiza este video", "¿por qué funcionó esto?", "disecciona este short", "qué tiene este video", "por qué tiene tantas vistas". NO usar para extraer el lenguaje visual de una referencia (para eso está Disecar Referencias), para calificar una pieza publicitaria ni para escribir guiones.'
---

# ¿Por Qué Se Hizo Viral?

Una skill de Brontis_ para dejar de decir "le pegó" y empezar a decir por qué.

## Regla de oficio

**Lo viral tiene mecánica, no suerte.**

Casi todo video que explota tiene piezas que se pueden nombrar: algo que detiene el pulgar, una promesa que retiene, un formato que se puede repetir y una razón para mandárselo a alguien. La suerte existe, pero es la parte más chica. Esta skill separa lo que se puede robar de lo que no, y lo dice con la misma claridad.

## Input

Cualquiera de estos, de más a menos completo:

- **El link.** Si `yt-dlp` está instalado, se usa para sacar datos en lugar de adivinar:
  - Metadatos: `yt-dlp -J "URL"` (vistas, likes, comentarios, duración, fecha, canal).
  - Subtítulos: `yt-dlp --skip-download --write-auto-subs --sub-langs "es.*,en.*" "URL"`.
  - Comentarios: `yt-dlp --skip-download --write-comments "URL"`, ordenados por relevancia.
  - Línea base del canal: `yt-dlp --flat-playlist -J` sobre la página de videos o shorts del canal.
- **La transcripción** pegada, con o sin tiempos.
- **Una descripción** de lo que pasa en el video y sus números aproximados.

Si no hay forma de ver el video ni datos, se trabaja con lo que haya y se marca cada conclusión como "inferida".

## Proceso

### Paso 1 · ¿De verdad es viral?
Vistas solas no dicen nada. Se compara contra la mediana de los últimos videos del canal:

- **3x o más:** outlier. Algo en este video funcionó distinto.
- **1x a 3x:** buen video de un canal que ya funciona. El mérito es del canal, no del video.
- **Sin línea base:** se dice "popular", no "viral", y se sigue con cautela.

### Paso 2 · El motor en seis piezas

1. **El freno (0 a 3 segundos).** Qué se ve, qué se oye y qué se lee. Se clasifica: resultado adelantado, acción ya empezada, afirmación que irrita, pregunta, imagen imposible, identificación inmediata.
2. **La promesa.** Qué cree el espectador que va a recibir si se queda. Si no se puede decir en una frase, no la hay.
3. **La estructura.** Secciones con tiempos. Dónde se abren preguntas, dónde se reengancha, dónde llega el pago. Se marca el punto probable donde se va la gente.
4. **El formato.** El contenedor repetible: lista, reto, antes y después, reacción, tutorial, sketch, confesión. Se dice si el canal ya lo había usado.
5. **El disparador.** Por qué alguien lo manda o lo comparte: lo representa, le sirve, le da tema para pelear, le da algo que decir de otro ("esto eres tú").
6. **Los comentarios.** La reacción dominante, las frases del video que la gente cita, las preguntas que se repiten y las objeciones. El momento más citado casi siempre es el corazón del video.

### Paso 3 · Separar robable de no robable
Lo robable son decisiones: el freno, la promesa, la estructura, el formato. Lo no robable son circunstancias: el tamaño del canal, el momento cultural, un empujón externo, el algoritmo de esa semana. Se nombran ambas.

## Output

```
¿POR QUÉ SE HIZO VIRAL? · [título del video]

FICHA
Canal · duración · fecha · vistas · likes · comentarios
Contra el canal: [n]x la mediana / sin línea base
Fuente de los datos: [yt-dlp / usuario / inferido]

EL MOTOR
Freno: [qué pasa en 0 a 3s] · tipo: [clasificación]
Promesa: [una frase]
Estructura: [00:00 · sección] [00:12 · sección] ... · fuga probable: [tiempo]
Formato: [contenedor] · ¿nuevo para el canal?: [sí/no]
Disparador: [por qué se comparte]
Comentarios: [reacción dominante · frase más citada · pregunta repetida · objeción]

LO ROBABLE
1. [Instrucción aplicable a otro video o marca.]
2. ...
3. ...

LO QUE NO SE ROBA
[Circunstancias que no se pueden replicar.]
```

## Anti-patrones

- **"Es que es auténtico".** No explica nada. ¿Qué decisión concreta lo hace sentir así?
- **Confundir canal grande con video viral.** Sin línea base, no hay veredicto.
- **Inventar números.** Si no hay datos, se dice. Nunca se rellenan vistas ni comentarios.
- **Lecciones que son deseos.** "Haz un buen hook" no es una lección. "Abre con el resultado y explica después" sí.
- **Ignorar los comentarios.** Ahí la audiencia dice gratis qué le gustó.

## Auto-revisión antes de entregar

1. ¿Cada conclusión dice de dónde salió: dato, transcripción o inferencia?
2. ¿Lo robable se puede aplicar a un tema completamente distinto?
3. ¿Fui honesto con la parte de suerte?

## Lo que no hace

- No analiza estilo visual a fondo. Para eso está Disecar Referencias.
- No escribe el guion del siguiente video.
- No descarga ni redistribuye el video. Solo lee datos públicos para analizarlos.

Hecha por Brontis_.
