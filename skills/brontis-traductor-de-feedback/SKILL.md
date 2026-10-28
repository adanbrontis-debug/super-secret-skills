---
name: brontis-traductor-de-feedback
description: 'Traduce comentarios vagos de cliente ("hazlo más pop", "le falta algo", "no me late") en instrucciones que el equipo sí puede ejecutar. Usa un diccionario de frases de cliente con el miedo probable detrás de cada una, y entrega cambios concretos más las preguntas de aclaración para mandar de vuelta. Trigger cuando el usuario diga "traductor de feedback", "/feedback", "qué quiso decir el cliente", "me dijeron que le falta algo", "tradúceme estos comentarios", "no entiendo el feedback", "el cliente dijo que lo hiciera más", "cómo aterrizo estos cambios". NO usar para preparar la defensa antes de presentar (eso es Vende mejor.) ni para ensayar la junta (eso es El Cliente Imposible).'
---

# Traductor de Feedback

Una skill de Brontis_ para entender qué quiso decir el cliente cuando dijo "más pop".

## Regla de oficio

**Detrás de cada comentario vago hay un miedo concreto.**

El cliente no habla en vago por fastidiar. Habla en vago porque siente algo que no sabe nombrar, o porque no quiere decir de frente lo que le preocupa. Ejecutar el comentario al pie de la letra produce otra ronda. Encontrar el miedo y resolverlo produce la aprobación. "Más grande el logo" casi nunca es sobre el logo.

## Input

- Los comentarios del cliente, tal cual llegaron: correo, notas de junta, mensajes, audio transcrito.
- La pieza o la idea sobre la que comentaron.
- Contexto si existe: quién dijo qué, en qué ronda van, qué se aprobó antes.

Si los comentarios vienen de varias personas, se separan por persona. Dos comentarios contradictorios de dos personas no son un problema creativo, son un problema de quién decide.

## El diccionario

Lecturas probables, no verdades. Se confirman con preguntas.

| Lo que dice | Miedo probable | Lo que suele pedir de verdad |
|---|---|---|
| "Hazlo más pop" | Que se vea viejo o aburrido | Más color, ritmo más rápido, referencias actuales |
| "Le falta algo" | Que no se entienda o no se recuerde | Un remate, un momento claro, más presencia de producto |
| "No me late" | Algo choca con su idea de la marca y no sabe qué | Encontrar el elemento exacto que choca |
| "Más grande el logo" | Que la gente no sepa de quién es el anuncio | Marca integrada antes, no logo más grande |
| "Que sea más emotivo" | Que se sienta frío o corporativo | Una persona concreta, un detalle humano |
| "Muy arriesgado" | Su jefe, la prensa o las redes | Plan de contención, precedente, prueba piloto |
| "¿Y si probamos otra cosa?" | No sabe defenderlo hacia arriba | Argumentos para vender adentro, no otra ruta |
| "Más premium" | Que se vea barato | Menos elementos, más aire, mejor tipografía |
| "Que se entienda más" | Que el público no capte la idea | Una idea menos, no un texto más |
| "Me gusta, pero..." | El "pero" es lo único que importa | Atender solo lo que viene después del pero |
| "Mi equipo no está convencido" | Alguien con poder dijo que no | Saber quién y qué dijo exactamente |
| "Algo más disruptivo" | Que se parezca a la competencia | Diferenciarse de una pieza concreta del rival |

Si una frase no está en el diccionario, se lee igual: qué siente, qué teme, qué cambio mínimo lo calma.

## Proceso

1. **Separar** cada comentario en una línea, citado textual, con quién lo dijo.
2. **Clasificar.** Concreto (se ejecuta tal cual), vago (se traduce) o contradictorio (se escala).
3. **Traducir** los vagos con el diccionario: miedo probable y cambio propuesto.
4. **Escribir el cambio ejecutable.** Una instrucción que un diseñador o un editor pueda hacer sin preguntar nada. Con verbo, objeto y medida: "subir el producto al segundo 3", no "darle más presencia".
5. **Escribir las preguntas de aclaración** para mandar al cliente. Cerradas, con opciones, máximo cinco. "¿Te refieres a A o a B?" se contesta. "¿Qué quisiste decir?" no.
6. **Detectar lo que no hay que cambiar.** Comentarios que, ejecutados, matan la idea. Se marcan para defenderlos.

## Output

```
TRADUCTOR DE FEEDBACK · [pieza] · Ronda [número]

[1] "[comentario textual]" · [quién]
    Tipo: [concreto / vago / contradictorio]
    Miedo probable: [cuál]
    Cambio ejecutable: [verbo + objeto + medida]
    Confianza: [alta / media / baja]

[2] ...

────────────
PREGUNTAS PARA EL CLIENTE (para copiar y pegar)
1. ¿[pregunta cerrada con opciones]?
...

NO TOCAR: [comentario] → por qué ejecutarlo mata la idea
CONTRADICCIONES: [quién dijo qué] → quién tiene que decidir
```

## Anti-patrones

- **Obedecer literal.** Hacer el logo más grande porque lo pidieron, sin preguntar por qué.
- **Burlarse del comentario.** El cliente siente algo real aunque lo diga mal. La traducción respeta eso.
- **Cambios sin medida.** "Darle más vida" no es una instrucción, es otro comentario vago.
- **Preguntas abiertas.** Mandar "¿qué quisiste decir?" garantiza otra semana de silencio.
- **Resolver contradicciones a escondidas.** Si dos personas piden lo opuesto, se dice.

## Auto-revisión antes de entregar

1. ¿Cada cambio ejecutable se puede hacer sin volver a preguntar?
2. ¿Las preguntas se contestan con una palabra o una elección?
3. ¿Marqué al menos un comentario para defender, o todos parecían razonables de verdad?

## Lo que no hace

- No prepara la defensa antes de presentar. Para eso está Vende mejor.
- No ensaya juntas. Para eso está El Cliente Imposible.
- No reescribe el copy. Para recortarlo está Tijera.

Hecha por Brontis_.
