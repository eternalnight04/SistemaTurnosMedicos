# SistemaTurnosMedicos - Diseño Orientado a Objetos

## Información General

| Aspecto | Detalle |
|---------|---------|
| **Materia** | Diseño Orientado a Objetos (DOO) |
| **Carrera** | Tecnicatura Universitaria en Programación de Sistemas |
| **Profesor** | Lic. Matias Velasquez |
| **Cuatrimestre** | 1er Cuatrimestre 2026 |
| **Repositorio** | SistemaTurnosMedicos (GitHub) |

---

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar el **diseño orientado a objetos** de un sistema para la **gestión de turnos de un consultorio médico**, aplicando progresivamente los principios y artefactos de la programación orientada a objetos.

Partiendo del análisis de información deliberadamente dispersa (mails, audios, notas y transcripciones), identificamos requisitos funcionales y no funcionales, modelamos casos de uso, diseñamos un boceto inicial de clases, y refinamos el diseño mediante tarjetas CRC, diagramas de casos de uso y escenarios detallados.

---

## Integrantes del Equipo

| Nombre y Apellido | Matrícula | Usuario GitHub | Rol A1 | Rol A2 |
|---|---|---|---|---|
| Carreras, Natalia | 161517 | @nataliacarreras96git | Documentadora y Coordinadora | Especialista en Escenarios + Documentadora y Coordinadora |
| Ferreyra Santiago, Joaquín | 161304 | @ferreyrasantiagojoaquin-lab | Analista de Requerimientos | Diseñador de Tarjetas CRC |
| Torres, Tomás | 157744 | @TomasTorres27 | Diseñador de Clases Iniciales | Modelador de Diagramas de Casos de Uso |

---

## Actividad Obligatoria N°1: Análisis y Diseño Inicial

### Objetivo

- Analizar información proporcionada por el cliente
- Identificar requisitos funcionales y no funcionales
- Modelar casos de uso relevantes del sistema
- Diseñar un boceto inicial de clases del dominio
- Aplicar fundamentos de Programación Orientada a Objetos
- Utilizar GitHub con GitFlow como metodología colaborativa

### Artefactos Entregados

- [📋 Introducción - Requisitos, Casos de Uso y Fundamentos](anexos/introduccion.md)
- [📎 Anexos y Documentación Complementaria](anexos/anexos.md)
- [📊 Boceto Inicial de Clases (Diagrama Excalidraw)](diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw)

---

## Actividad Obligatoria N°2: Refinamiento del Diseño y Modelado

### Objetivo

Refinar el diseño del sistema de gestión de turnos profundizando en el modelado orientado a objetos mediante tres artefactos concretos:

1. **Tarjetas CRC** - Análisis de responsabilidades y colaboraciones entre clases
2. **Diagramas de Casos de Uso** - Representación visual de interacciones del sistema (PlantUML)
3. **Escenarios de Casos de Uso** - Descripción detallada del flujo de interacción

### Artefactos Principales

#### 📑 Tarjetas CRC
- **Índice General:** [Herramientas Agile - Tarjetas CRC](herramientas-agile/herramientas_agile.md)
- **Carpeta:** [herramientas-agile/tarjetas-crc/](herramientas-agile/tarjetas-crc/)
- Análisis de 5 clases: responsabilidades, superclases/subclases, colaboraciones y propiedades

#### 📊 Diagramas de Casos de Uso
- **Índice General:** [Diagramas UML](diagramas/diagramasUML.md)
- **Índice Específico:** [Diagramas de Casos de Uso](diagramas/02-casos-de-uso/diagramas_de_casos_de_uso.md)
- **Carpeta:** [diagramas/02-casos-de-uso/](diagramas/02-casos-de-uso/)
- 5 diagramas PlantUML con actores y relaciones (asociaciones, inclusiones, extensiones)

#### 📋 Escenarios de Casos de Uso
- **Índice General:** [Escenarios de Casos de Uso](diagramas/03-escenarios-casos-de-uso/escenarios_de_casos_de_uso.md)
- **Carpeta:** [diagramas/03-escenarios-casos-de-uso/](diagramas/03-escenarios-casos-de-uso/)
- 5 escenarios detallados (16 campos cada uno): ID, área, actores, descripción, flujo, pre/postcondiciones, prioridad, riesgo

### Documentación del Proceso con Copilot Agent Mode

Cada integrante documentó su uso de Copilot, archivos de contexto y ajustes realizados:

- [🤖 Diseñador de Tarjetas CRC](ia/a2/disenador-tarjetas-crc.md) - Santiago
- [🤖 Modelador de Diagramas](ia/a2/modelador-diagramas-casos-uso.md) - Tomás
- [🤖 Especialista en Escenarios](ia/a2/especialista-escenarios.md) - Natalia
- [🤖 Documentador y Coordinador](ia/a2/documentador-coordinador.md) - Natalia

---

## Estructura de Carpetas del Proyecto

```
SistemaTurnosMedicos/
├── README.md (este archivo)
├── changelog.md (registro de cambios y contribuciones)
├── .github/
│   └── PULL_REQUEST_TEMPLATE/
│       ├── feature-template.md
│       └── release-template.md
├── ia/
│   └── a2/
│       ├── disenador-tarjetas-crc.md
│       ├── modelador-diagramas-casos-uso.md
│       ├── especialista-escenarios.md
│       └── documentador-coordinador.md
├── diagramas/
│   ├── diagramasUML.md (índice general A2)
│   ├── 01-diagrama-clases/
│   │   ├── 01-boceto-inicial.excalidraw
│   │   └── 01-boceto-inicial.png
│   ├── 02-casos-de-uso/ (A2)
│   │   ├── diagramas_de_casos_de_uso.md (índice)
│   │   ├── 02-caso-uso-crear-turno.puml
│   │   ├── 02-caso-uso-crear-turno.png
│   │   ├── 02-caso-uso-reprogramar-turno.puml
│   │   ├── 02-caso-uso-reprogramar-turno.png
│   │   ├── 02-caso-uso-cancelar-turno.puml
│   │   ├── 02-caso-uso-cancelar-turno.png
│   │   ├── 02-caso-uso-autorizar-sobreturno.puml
│   │   ├── 02-caso-uso-autorizar-sobreturno.png
│   │   ├── 02-caso-uso-registrar-llegada.puml
│   │   └── 02-caso-uso-registrar-llegada.png
│   └── 03-escenarios-casos-de-uso/ (A2)
│       ├── escenarios_de_casos_de_uso.md (índice)
│       ├── 03-crear-turno-flujo-principal.md
│       ├── 03-reprogramar-turno-flujo-alterno.md
│       ├── 03-cancelar-turno-flujo-principal.md
│       ├── 03-autorizar-sobreturno-flujo-principal.md
│       └── 03-registrar-llegada-flujo-principal.md
├── herramientas-agile/ (A2)
│   ├── herramientas_agile.md (índice)
│   └── tarjetas-crc/
│       ├── 01-tarjeta-crc-paciente.md
│       ├── 02-tarjeta-crc-medico.md
│       ├── 03-tarjeta-crc-turno.md
│       ├── 04-tarjeta-crc-agenda.md
│       └── 05-tarjeta-crc-secretaria.md
└── anexos/
    ├── anexos.md
    └── introduccion.md
```

---

## Metodología de Trabajo

- **Control de Versiones:** Git con GITFLOW
- **Ramas:**
  - `master` - Rama de producción (protegida)
  - `develop` - Rama de integración (protegida)
  - `feature/*` - Ramas de desarrollo individual
  - `release/*` - Ramas de entrega
  - `fix/*` - Ramas para correcciones
  
- **Herramientas:** GitHub, VS Code, PlantUML, Copilot Agent Mode
- **Comunicación:** Slack + Weekly Meetings

---

## Cómo Navegar este Repositorio

### Para Actividad Obligatoria N°1:
1. Comienza con [Anexos](anexos/anexos.md) para contexto general
2. Lee [Introducción](anexos/introduccion.md) para requisitos y casos de uso
3. Consulta [Boceto de Clases](diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw)

### Para Actividad Obligatoria N°2:
1. Accede a [Diagramas UML](diagramas/diagramasUML.md) para visiones generales
2. Revisa [Tarjetas CRC](herramientas-agile/herramientas_agile.md) para análisis de responsabilidades
3. Estudia [Escenarios](diagramas/03-escenarios-casos-de-uso/escenarios_de_casos_de_uso.md) para flujos detallados
4. Consulta [Documentación Copilot](ia/a2/) para entender el proceso de diseño

---

## Entrega y Evaluación

- **Fecha Límite:** 16 de abril, 23:55 (ya finalizada)
- **Formato:** Pull Request desde `release/actividad-obligatoria-2` hacia `master`
- **Criterios:** 2,5 puntos por rol (total 10 puntos) según desempeño individual
- **Documentación Obligatoria:** Cada rol debe documentar el uso de Copilot en `ia/a2/`

---

## Registro de Cambios

Ver [changelog.md](changelog.md) para el historial completo de contribuciones por integrante y PR asociadas.
