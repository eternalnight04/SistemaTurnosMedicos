# Rol: Arquitecto de Dominio

Se incluyen los artefactos generados por la actividad de arquitectura de dominio: diagrama de clases final (`06-clases-diagrama-final.puml`), análisis de pilares POO y happy path global. Estos documentos consolidan las tarjetas CRC y diagramas existentes.

Archivos relevantes:
- `diagramas/01-diagrama-clases/06-clases-diagrama-final.puml`
- `anexos/analisis-funcional/pilares-poo.md`
- `anexos/analisis-funcional/happy-path-global.md`
- `issues-detected.md`

Resumen breve: el diagrama final unifica `Paciente`, `Medico`, `Secretaria`, `Agenda`, `Turno` y `LlegadaPaciente`, añade la superclase `UsuarioDelSistema` y el enum `TurnoEstado`. Se detectaron inconsistencias y se proponen normalizaciones en `issues-detected.md`.
