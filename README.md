# Super Secret Skills.

20 skills gratis para Claude Code, hechas para publicistas, creativos y gente de marketing. By Brontis.

Cada skill es un archivo `SKILL.md` con un método completo y una regla de oficio que no se negocia. Se instalan copiando y pegando en Claude Code, sin tocar la terminal.

## Cómo instalar una skill

1. Entra al sitio y pica **Instalar skill** en la que quieras.
2. Pega el texto en Claude Code y dale Enter. Claude crea el archivo por ti.
3. Pídela hablando normal: "pásalo por la Tijera", "dame cien malas ideas para una cafetería".

Si prefieres hacerlo a mano, copia la carpeta de la skill desde `skills/` a `~/.claude/skills/`.

## Qué hay en este repositorio

| Carpeta | Qué es |
|---|---|
| `skills/` | Las 20 skills, una carpeta por skill con su `SKILL.md`. Esto es lo que se instala. |
| `site/` | La plantilla del sitio, el script que lo arma y el filtro de tramado de las imágenes. |
| `art/` | Las escenas de cada skill: originales, tramadas, prompts y ajustes. |
| `docs/` | El sitio ya construido. GitHub Pages publica esta carpeta. |
| `la-lista.md` | La lista de las 20 con nombre, qué hace y regla de oficio. |

## Cómo se arma el sitio

El sitio se genera a partir de las skills, la lista y las imágenes tramadas. Después de editar cualquiera de esas cosas:

```bash
SITE_URL=https://adanbrontis-debug.github.io/super-secret-skills python3 -I site/build.py
```

Las imágenes se traman con `site/dither.py`: una escena en blanco y negro entra, y sale a dos tonos, negro más el tramo del arcoíris que le toca a esa skill según su número.

## Las 20

1. Cien Malas Ideas
2. Robar como Artista
3. ¿Ya Existe?
4. El Cementerio de Ideas
5. Hilo Fino
6. Tijera
7. El Bautizo
8. El Tropicalizador
9. Memeificador
10. El Director de Arte Invisible
11. Storyboard Express
12. El Gemelo
13. Disecar Referencias
14. Vende mejor.
15. El Cliente Imposible
16. Traductor de Feedback
17. Pocket Focus Group
18. ¿Por Qué Se Hizo Viral?
19. El Case Video
20. El Lunes

## Licencia

Las skills se comparten para que cualquiera las use, las adapte y las mejore. Si las compartes, menciona de dónde salieron.

Hecha por Brontis_.
