---
name: brontis-el-bautizo
description: 'Propone nombres para un producto, campaña, proyecto o marca por territorios nombrados (descriptivo, evocador, inventado, juego de palabras, prestado, compuesto), los filtra con pruebas nombradas (pronunciación, deletreo por teléfono, otros idiomas y regiones hispanohablantes, malas lecturas, connotaciones feas) y revisa con búsqueda web si los finalistas ya existen como marca y si dominios y redes parecen tomados. Trigger cuando el usuario diga "el bautizo", "/bautizo", "necesito un nombre", "ponle nombre a", "¿cómo le llamamos?", "naming para", "ideas de nombre", "bautiza este proyecto". NO usar como búsqueda legal de marca registrada, para escribir taglines ni para diseñar el logo.'
---

# El Bautizo

Una skill de Brontis_ para que el nombre no necesite padrino que lo explique.

## Regla de oficio

**Un nombre que hay que explicar ya perdió.**

El nombre se dice en voz alta, se escribe mal en un chat, se busca en el celular y se le cuenta a alguien en una fiesta. Si en cualquiera de esos momentos necesita una nota al pie, ya perdió. Un buen nombre no tiene que decirlo todo: tiene que sonar bien, recordarse rápido y no traer sorpresas en otro país. Esta skill propone mucho, filtra con crueldad y revisa en internet antes de que alguien se enamore.

## Input

- **Qué se bautiza:** producto, campaña, proyecto, marca o plataforma.
- **Qué hace o promete**, en una o dos frases.
- **Personalidad:** tres adjetivos o una referencia de tono.
- Opcional: países donde va a vivir, idiomas obligatorios, palabras prohibidas, nombres de la competencia, si necesita dominio.

Si falta qué hace, se pregunta una vez. Sin eso solo salen nombres bonitos y vacíos.

## Proceso

1. **Territorios.** Entre cuatro y seis nombres por territorio:
   - **Descriptivo.** Dice lo que es. Claro, poco memorable, fácil de registrar mal.
   - **Evocador.** Una palabra real que sugiere la sensación o el beneficio.
   - **Inventado.** Una palabra nueva que suena a algo. Hay que poder pronunciarla a la primera.
   - **Juego de palabras.** Doble sentido, fusión o rima. El más peligroso, el más divertido.
   - **Prestado.** Viene de otro mundo: un lugar, un oficio, un personaje, un objeto, otro idioma.
   - **Compuesto.** Dos palabras que juntas significan algo nuevo.
2. **Primer filtro, las pruebas.** Cada nombre pasa por:
   - **Prueba de la boca.** ¿Se pronuncia igual quien lo lee por primera vez?
   - **Prueba del teléfono.** Si se lo dictas a alguien, ¿lo escribe bien sin deletrear?
   - **Prueba de la vuelta al mundo.** ¿Significa algo en inglés, portugués u otros idiomas relevantes? ¿Y en las regiones de habla hispana, donde una palabra inocente en un país es grosería en otro?
   - **Prueba del mal pensado.** ¿Se puede leer mal, partir mal o volver albur?
   - **Prueba del vecino incómodo.** ¿Suena a algo feo, a un escándalo, a otra categoría o a la competencia?
3. **Finalistas.** Quedan entre tres y cinco, idealmente de territorios distintos.
4. **Revisión en internet.** Para cada finalista, usar WebSearch para buscar el nombre solo y con la categoría: marcas, productos o empresas que ya lo usen. Revisar con búsqueda o WebFetch si el dominio .com y el del país parecen tomados y si hay cuentas con ese nombre en las redes principales. Reportar lo que se vio, con link, y marcar como "no verificado" lo que no se pudo revisar.
5. **Recomendación.** Uno favorito, con su porqué, y uno de respaldo.

## Output

```
EL BAUTIZO · [qué se bautiza]

LO QUE TIENE QUE CARGAR EL NOMBRE: [una frase]

TERRITORIOS
Descriptivo: [nombre], [nombre], ...
Evocador: ...
Inventado: ...
Juego de palabras: ...
Prestado: ...
Compuesto: ...

LOS QUE NO PASARON (los más tentadores)
[Nombre] · reprobó [prueba]: [por qué, en una línea]

FINALISTAS
1 · [NOMBRE] · territorio [x]
    Por qué funciona: [una frase]
    Pruebas: boca [ok/ojo] · teléfono [ok/ojo] · vuelta al mundo [ok/ojo] · mal pensado [ok/ojo] · vecino [ok/ojo]
    En internet: [qué se encontró, con link, o "nada evidente"]
    Dominio: [parece libre / tomado / no verificado] · Redes: [parece libre / tomado / no verificado]
2 · ...

EL FAVORITO: [nombre] · [porqué en una frase] · Respaldo: [nombre]
Ojo: esto no sustituye una búsqueda legal de marca registrada.
```

## Anti-patrones

- **El nombre con instructivo.** Si necesita "es que viene de...", se va o se defiende con algo mejor que la etimología.
- **Todos del mismo territorio.** Seis evocadores no son opciones, son sinónimos.
- **La moda del momento.** Quitarle vocales, terminar en "-ify" o pegar "ly" envejece rápido.
- **Inventar disponibilidad.** Nunca decir que un dominio o marca está libre sin haberlo revisado. Si no se pudo, se dice.
- **Ignorar el español de otros países.** Lo que en un lado es tierno en otro es grosería.

## Auto-revisión antes de entregar

1. ¿Puedo decir cada finalista en voz alta sin explicarlo?
2. ¿Revisé de verdad en internet cada finalista y puse lo que vi?
3. ¿Los finalistas vienen de al menos dos territorios distintos?
4. ¿Está visible la advertencia de que no es búsqueda legal?

## Lo que no hace

- No hace búsqueda legal de marca registrada. Para eso hay abogados y registros oficiales.
- No escribe taglines ni copy de lanzamiento.
- No diseña logos ni identidad visual.

Hecha por Brontis_.
