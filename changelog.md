# Changelog

Este archivo se actualiza con cada Pull Request para registrar avances y correcciones.

---

## [Released - Actividad Obligatoria N°2] - 2026-04-17

Consolidación de diseño refinado mediante tarjetas CRC, diagramas de casos de uso y escenarios detallados. Utilización de Copilot Agent Mode en cada rol con documentación completa del proceso.

**Nota Importante:** Durante la reasignación de roles para A2, Claudia abandonó el grupo. Como consecuencia, Natalia asumió dos roles simultáneamente: Especialista en Escenarios de Casos de Uso + Documentadora y Coordinadora de Repositorio. A pesar de esta sobrecarga, Natalia completó exitosamente ambas responsabilidades sin comprometer la calidad de la entrega.

### Added

#### 📋 Especialista en Escenarios de Casos de Uso - Natalia Carreras

- [feature/especialista-escenarios-casos-uso] **Creación de 5 escenarios de casos de uso completos** (03-crear-turno-flujo-principal.md, 03-reprogramar-turno-flujo-alterno.md, 03-cancelar-turno-flujo-principal.md, 03-autorizar-sobreturno-flujo-principal.md, 03-registrar-llegada-flujo-principal.md) con los 16 campos requeridos cada uno:
  - ID única, Área, Actor(es), Descripción, Evento activador, Tipo de señal
  - Pasos desempeñados (ruta principal), Precondiciones, Poscondiciones
  - Suposiciones, Requerimientos, Aspectos sobresalientes, Prioridad, Riesgo
  - Carpeta: diagramas/03-escenarios-casos-de-uso/
  - Índice: diagramas/03-escenarios-casos-de-uso/escenarios_de_casos_de_uso.md
  - Documentación Copilot: ia/a2/especialista-escenarios.md (336 líneas - muy completa)
  - PR: (#48) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/48)
  - @nataliacarreras96git (Especialista en Escenarios de Casos de Uso)

#### 📊 Modelador de Diagramas de Casos de Uso - Tomás Torres

- [feature/modelador-diagramas-casos-uso] **Generación de 5 diagramas PlantUML de casos de uso**:
  - 02-caso-uso-crear-turno.puml / .png
  - 02-caso-uso-reprogramar-turno.puml / .png
  - 02-caso-uso-cancelar-turno.puml / .png
  - 02-caso-uso-autorizar-sobreturno.puml / .png
  - 02-caso-uso-registrar-llegada.puml / .png
  - Cada diagrama incluye actores principales (Paciente, Médico, Secretaria, Sistema)
  - Relaciones correctas: asociaciones, inclusiones (<<include>>), extensiones (<<extend>>)
  - Carpeta: diagramas/02-casos-de-uso/
  - Índices: diagramas/diagramasUML.md (general) + diagramas/02-casos-de-uso/diagramas_de_casos_de_uso.md (específico)
  - Documentación Copilot: ia/a2/modelador-diagramas-casos-uso.md (47 líneas)
  - PR: (#51) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/51)
  - @TomasTorres27 (Modelador de Diagramas de Casos de Uso)
  - Correcciones aplicadas: PNG extensions (.png.png → .png), folder structure (ia/a2/ia/a2/ → ia/a2/), índices creados

#### 🎯 Diseñador de Tarjetas CRC - Santiago Ferreyra

- [feature/disenador-tarjetas-crc-paciente] **Tarjeta CRC: Paciente** - Clase principal que representa a los usuarios del sistema con responsabilidades de autenticación y gestión de turnos propios. PR: (#54) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/54) - @ferreyrasantiagojoaquin-lab

- [feature/disenador-tarjetas-crc-medico] **Tarjeta CRC: Médico** - Profesional que gestiona su agenda y atiende pacientes. Responsabilidades de validación y gestión de turnos. PR: (#60) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/60) - @ferreyrasantiagojoaquin-lab

- [feature/disenador-tarjetas-crc-turno] **Tarjeta CRC: Turno** - Entidad central del dominio que representa la cita médica con atributos temporales y de estado. PR: (#61) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/61) - @ferreyrasantiagojoaquin-lab

- [feature/disenador-tarjetas-crc-agenda] **Tarjeta CRC: Agenda** - Gestiona la disponibilidad temporal del médico y organiza los turnos asignados. PR: (#57) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/57) - @ferreyrasantiagojoaquin-lab

- [feature/disenador-tarjetas-crc-secretaria] **Tarjeta CRC: Secretaria** - Actor que administra turnos, autoriza sobreturno y registra llegadas de pacientes. PR: (#58) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/58) - @ferreyrasantiagojoaquin-lab

- [feature/disenador-tarjetas-crc-index] **Índice de Tarjetas CRC** - Se crea herramientas-agile/herramientas_agile.md vinculando las 5 tarjetas. PR: (#59) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/59) - @ferreyrasantiagojoaquin-lab

  **Resumen Diseñador CRC (Santiago):**
  - 5 tarjetas CRC completas (nombre, superclase/subclase, pensamiento del objeto, responsabilidades, colaboraciones, propiedades)
  - Carpeta: herramientas-agile/tarjetas-crc/
  - Índice: herramientas-agile/herramientas_agile.md
  - PRs: #54, #60, #61, #57, #58, #59 (todas mergeadas a develop)

- [feature/disenador-tarjetas-crc-documentation] **Documentación del proceso Copilot para Diseñador CRC**:
  - Archivo: ia/a2/disenador-tarjetas-crc.md (25 líneas)
  - Incluye prompts utilizados, archivos de contexto, ajustes realizados, decisiones de diseño, reflexión
  - PR: (#63) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/63)
  - @ferreyrasantiagojoaquin-lab (Diseñador de Tarjetas CRC)
  - Correcciones aplicadas: Se requirió iteración (nombre y contenido corregidos en 2do intento)

#### 👥 Documentador y Coordinador de Repositorio - Natalia Carreras

- [feature/doc-coord-repo-A2-README] **Actualización completa de README.md**:
  - Información general mejorada (tabla con Materia, Carrera, Profesor, Cuatrimestre)
  - Tabla de integrantes con Rol A1 y Rol A2 actualizada
  - Secciones separadas para A1 y A2 con objetivos específicos
  - Artefactos principales con enlaces directos a índices
  - Documentación Copilot (enlaces a ia/a2/)
  - Estructura de carpetas del proyecto documentada
  - Metodología de trabajo explicada
  - Guía de navegación para usuario final

- [feature/doc-coord-repo-A2-documentation] **Documentación del proceso de Coordinación**:
  - Archivo: ia/a2/documentador-coordinador.md (~200 líneas)
  - 4 Code Reviews ejecutados con Copilot Agent Mode:
    1. PR #51 (Tomás - Diagramas): Validación de 5 diagramas UML
    2. PRs #54-61 (Santiago - CRC): Validación de 5 tarjetas CRC
    3. PR #48 (Natalia - Escenarios): Validación de 5 escenarios completos
    4. PR #63 (Santiago - Doc CRC): Validación de documentación Copilot
  - Cada review incluye: prompt Copilot, validaciones realizadas, decisiones de coordinación
  - Resumen de PRs gestionadas, issues creadas/cerradas, validaciones clave ejecutadas
  - Reflexión sobre fortalezas, desafíos y recomendaciones

- [feature/doc-coord-repo-A2-release] **Creación de rama release/actividad-obligatoria-2**:
  - Rama creada desde develop después de mergear todas las PRs
  - Contiene todos los cambios de A2 listos para entrega
  - Commits: README.md, changelog.md, ia/a2/documentador-coordinador.md

  **Resumen Documentador y Coordinador (Natalia):**
  - Coordinó integración de 4 PRs principales (48, 51, 54-61, 63)
  - Ejecutó 4+ code reviews con Copilot validando coherencia A1 → A2
  - Documentó prompts y procesos en ia/a2/documentador-coordinador.md
  - Actualizó README.md e integró índices nuevos
  - Actualizó changelog.md con todas las contribuciones
  - Creó rama release/actividad-obligatoria-2 para entrega final

### Changed

- [release/actividad-obligatoria-2] **Preparación de rama release para entrega**:
  - Rama creada desde develop
  - Integración de todos los cambios A2 listos para evaluación profesor
  - README.md completamente reescrito
  - changelog.md actualizado con sección [Released - A2]
  - Todos los artefactos accesibles y bien documentados
  - @nataliacarreras96git (Coordinadora)

---

## [Unreleased]

---

## [Release Actividad Obligatoria N°1] - 2026-03-26

Se consolidan todos los cambios realizados en la rama develop para la entrega final del trabajo práctico.

### Added

- [feature/modelador-casos-uso] Documentación de 5 casos de uso completos (UC-01 a UC-05) a partir de fuentes de dominio. PR: (#6) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/6) - @ademarco97 (Modelador)
- [feature/analista-requerimientos] Definición de requisitos funcionales y no funcionales del sistema. PR: (#8) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/8) - @nachonervi-design (Analista)
- [feature/diseniador-clases-add-boceto-inicial] Creación del diagrama de clases en formatos .excalidraw, .png y .puml. PR: (#9) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/9) - @LuchoBarrionuevo13 (Diseñador)
- [feature/doc-coord-repo-update-readme-md] Creación del README, introducción POO y anexos. PR: (#12) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/12) - @nataliacarreras96git (Documentadora)
- [feature/casos-uso-completos-g4] Completar 5 casos de uso (CU-01 a CU-05) con flujos principal y alternativo, actores y decisiones específicas del dominio. PR: (#34) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/34) - @TomasTorres27 (Diseñador de Clases Iniciales)
- [feature/casos-uso-g6-contenido-g4] Aporte de contenido de casos de uso del Grupo 6 adaptado al dominio de Sistema de Turnos Médicos (CU-01 a CU-05) con actores reales, flujos principal y alternativo. PR: (#36) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/36) - @ferreyrasantiagojoaquin-lab (Modelador)
- [feature/diagrama-mejorado-g4] Revisión y mejora del diagrama de clases en Excalidraw realizado por Natalia. Validación de entidades, relaciones y atributos según especificación del sistema de turnos médicos. PR:(https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/35) - @nataliacarreras96git (Coordinadora)

### Changed

- [feature/doc-coord-repo-update-readme-md] Actualización del README e introducción para mejorar claridad. PR: (#12) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/12) - @nataliacarreras96git (Documentadora)
- [feature/estructura-carpetas] Reorganización de carpetas (anexos/ y diagramas/). PR: (#10) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/10) - @nataliacarreras96git (Documentadora)
- [feature/normalizacion-nombres] Renombrado de carpetas a minúsculas (Diagramas → diagramas, 01-Diagrama-Clases → 01-diagrama-clases). PR: (#11) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/11) - @nataliacarreras96git (Documentadora)
- [feature/diagrama-mejorado-g4] Revisión y mejora del diagrama de clases en Excalidraw realizado por Natalia. Validación de entidades, relaciones y atributos según especificación del sistema de turnos médicos. PR: (#35) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/35) - @nataliacarreras96git (Coordinadora)

### Fixed

- [fix/revert-pr-14] Revert de PR #14 - Merge sin aprobación según corrección del profesor. Corrección de procedimiento GitFlow. - @nataliacarreras96git (Coordinadora)
- [fix/revert-pr-23] Revert de PR #23 - Merge sin aprobación según corrección del profesor. Corrección de procedimiento GitFlow. - @nataliacarreras96git (Coordinadora)
- [feature/doc-coord-correccion-changelog-a1] Corrección de changelog.md - formato exacto según especificación del profesor y agregación de entradas faltantes. PR: (#31) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/31) - @nataliacarreras96git (Documentadora y Coordinadora)
- [feature/doc-coord-correccion-readme-rnf] Corrección del README (tabla integrantes con Rol y matrículas actualizadas) e introduccion.md (Polimorfismo en lenguaje natural + 5 RNFs específicos). PR: (#32) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/32) - @nataliacarreras96git (Documentadora y Coordinadora)
- [fix/changelog-completo-todos-los-pr] Agregación de entradas faltantes en changelog: reverts de PR #14 y #23, y correcciones de PR #31 y #32. PR: (#33) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/33) - @nataliacarreras96git (Documentadora y Coordinadora)
- [fix/casos-uso-completos-g4] Corrección de 5 casos de uso completos (CU-01: Crear Turno, CU-02: Reprogramar, CU-03: Cancelar, CU-04: Autorizar Sobreturno, CU-05: Registrar Llegada) con actores, flujos principal y alternativo, precondiciones y postcondiciones. PR: (#34) (https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/34) - @TomasTorres27 (Diseñador)
- [fix/correccion-completa-actividad-1] Correcciones finales para la entrega: Agregar diagrama de clases (01-boceto-inicial.excalidraw y .png), enlace NotebookLM en anexos/introduccion.md, eliminar introduccion.md de raíz (versión correcta en anexos/), arreglar encoding UTF-8 en anexos/anexos.md. PR: [#42](https://github.com/nataliacarreras96git/SistemaTurnosMedicos/pull/42) - @nataliacarreras96git (Coordinadora)

