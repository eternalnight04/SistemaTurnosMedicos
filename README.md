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

| Nombre y Apellido | Matrícula | Usuario GitHub | Rol A1 | Rol A2 | Rol A3
|---|---|---|---|---|
| Carreras, Natalia | 161517 | @nataliacarreras96git | Documentadora y Coordinadora | Especialista en Escenarios + Documentadora y Coordinadora | Especialista en Diagramas de Actividades - Casos de Uso 3, 4 y 5 
| Neicuan, Alejo |159810 | @ANeicuan |Diseñador de Clases Iniciales + Documentador y coordinador del repositorio | Especialista en escenarios de casos de uso | Especialista en Diagramas de Actividades - Casos de Uso 1 y 2
| Nestmann, Sofia| 160130 |@sofinestt | Analista de Requerimentos|  Modelador de diagramas de Casos de Uso + Documentador y coordinador del repositorio |Especialista en diagramas de Secuencias 

---

## Actividad Obligatoria N°3: Análisis y Diseño Inicial

### Objetivo
 Profundizar en la dinámica del sistema mediante:

1.Diagramas de Actividades
2.Diagramas de Secuencia
3.Integración de artefactos previos
4.Trazabilidad entre requisitos, escenarios y diseño UML

La actividad continúa el trabajo realizado en A1 y A2 utilizando los escenarios, casos de uso y tarjetas CRC como contexto de diseño.


### Artefactos Entregados

Artefactos Entregados
📊 Diagramas de Actividades
Ruta: diagramas/04-diagramas-actividades/
📈 Diagramas de Secuencia
Ruta: diagramas/05-diagramas-secuencia/
🤖 Documentación del Uso de IA
Ruta: ia/a3/
📚 Índice General de Diagramas UML
Ruta: diagramas/diagramasUML.md

---

## Actividad Obligatoria N°3:Refinamiento del Diseño y Modelado

### Objetivo

Profundizar en la comprensión de la dinámica del sistema de gestión de turnos mediante el modelado de flujos de trabajo e interacciones entre objetos, utilizando como base los artefactos desarrollados en las Actividades Obligatorias N°1 y N°2.

Para ello, se trabajó sobre cuatro ejes principales:

Diagramas de Actividades - Modelado de los flujos de trabajo de cada caso de uso mediante actividades, decisiones, bifurcaciones y swimlanes.
Diagramas de Secuencia - Representación temporal de las interacciones entre actores y objetos del sistema.
Trazabilidad entre Artefactos - Integración coherente entre escenarios, casos de uso, tarjetas CRC y diagramas UML.
Documentación del uso de IA - Registro del proceso de generación y refinamiento de diagramas utilizando GitHub Copilot como herramienta de asistencia.

### Artefactos Principales

📊 Diagramas de Actividades
Índice General: diagramas/diagramasUML.md
Índice Específico: diagramas/04-diagramas-actividades/diagramas_de_actividades.md
Carpeta: diagramas/04-diagramas-actividades/
5 diagramas PlantUML con flujos de actividades, decisiones, bifurcaciones y swimlanes que representan responsabilidades entre actores y componentes del sistema.

📈 Diagramas de Secuencia
Índice General: diagramas/diagramasUML.md
Índice Específico: diagramas/05-diagramas-secuencia/diagramas_de_secuencias.md
Carpeta: diagramas/05-diagramas-secuencia/
5 diagramas PlantUML que representan interacciones temporales entre actores y objetos mediante mensajes, participantes y flujo cronológico de ejecución.

🤖 Documentación del Uso de IA
Carpeta: ia/a3/
Registro del proceso de generación y refinamiento de diagramas utilizando GitHub Copilot.
Incluye prompts utilizados, archivos de contexto referenciados, iteraciones realizadas y ajustes aplicados sobre las respuestas generadas por IA.

### Documentación del Proceso con Copilot Agent Mode

Cada integrante documentó su uso de Copilot, archivos de contexto y ajustes realizados:

- [🤖 Especialista en Diagramas de Actividades - Casos de Uso 1 y 2](ia/a3/esp-actividades-1-2.md) - Alejo
- [🤖  Especialista en Diagramas de Actividades - Casos de Uso 3, 4 y 5: ](ia/a3/esp-actividades-3-4-5.md) - Natalia 
- [🤖 Especialista en Diagramas de Secuencia](ia/a3/esp-secuencia.md.md) - Sofia
- [🤖 Documentador y Coordinador](ia/a2/documentador-coordinador.md) - Todos 

---

## Estructura de Carpetas del Proyecto

```
SistemaTurnosMedicos/ 
├── README.md (actualizado) 
├── changelog.md (actualizado) 
├── .github/ 
│   └── PULL_REQUEST_TEMPLATE/ 
│       
├── feature-template.md       
│       
└── release-template.md        
├── diagramas/ 
│   ├── diagramasUML.md (actualizado) 
│   ├── 01-diagrama-clases/ 
│   │   ├── 01-boceto-inicial.puml  
│   │   ├── 01-boceto-inicial.png  
│   │   ├── 01-solid-01-srp.puml 
│   │   ├── 01-solid-01-srp.png 
│   │   ├── 01-solid-02-ocp.puml 
│   │   ├── 01-solid-02-ocp.png 
│   │   ├── 01-solid-03-lsp.puml 
│   │   ├── 01-solid-03-lsp.png 
│   │   ├── 01-solid-04-isp.puml  
│   │   ├── 01-solid-04-isp.png 
│   │   ├── 01-solid-05-dip.puml 
│   │   └── 01-solid-05-dip.png 
│   ├── 02-casos-de-uso/ 
│   │   ├── diagramas_de_casos_de_uso.md  
│   │   ├── 02-caso-uso-nombre-caso-de-uso-01.puml  
│   │   ├── 02-caso-uso-nombre-caso-de-uso-01.png  
│   │   ├── 02-caso-uso-nombre-caso-de-uso-02.puml  
│   │   ├── 02-caso-uso-nombre-caso-de-uso-02.png 
│   │   └── ... (hasta 5 casos de uso) 
│   ├── 03-escenarios-casos-de-uso/ 
│   │   ├── escenarios_de_casos_de_uso.md  
│   │   ├── 03-nombre-caso-de-uso-nombre-escenario-01.md  
│   │   ├── 03-nombre-caso-de-uso-nombre-escenario-02.md 
│   │   ├── 03-nombre-caso-de-uso-nombre-escenario-03.md 
│   │   ├── 03-nombre-caso-de-uso-nombre-escenario-04.md 
│   │   └── 03-nombre-caso-de-uso-nombre-escenario-05.md 
│   ├── 04-diagramas-actividades/ 
│   │   ├── diagramas_de_actividades.md (nuevo - índice) 
│   │   ├── 04-actividad-nombre-caso-uso-01.puml 
│   │   ├── 04-actividad-nombre-caso-uso-01.png 
│   │   ├── 04-actividad-nombre-caso-uso-02.puml  
│   │   ├── 04-actividad-nombre-caso-uso-02.png  
│   │   ├── 04-actividad-nombre-caso-uso-03.puml  
│   │   ├── 04-actividad-nombre-caso-uso-03.png  
│   │   ├── 04-actividad-nombre-caso-uso-04.puml 
│   │   ├── 04-actividad-nombre-caso-uso-04.png 
│   │   ├── 04-actividad-nombre-caso-uso-05.puml 
│   │   └── 04-actividad-nombre-caso-uso-05.png 
│   └── 05-diagramas-secuencia/ 
│       
├── diagramas_de_secuencias.md (nuevo - índice) 
│       
│       
│       
│       
│       
│       
│       
│       
│       
│       
├── 05-secuencia-nombre-caso-uso-nombre-escenario-01.puml 
├── 05-secuencia-nombre-caso-uso-nombre-escenario-01.png 
├── 05-secuencia-nombre-caso-uso-nombre-escenario-02.puml  
├── 05-secuencia-nombre-caso-uso-nombre-escenario-02.png  
├── 05-secuencia-nombre-caso-uso-nombre-escenario-03.puml 
├── 05-secuencia-nombre-caso-uso-nombre-escenario-03.png 
├── 05-secuencia-nombre-caso-uso-nombre-escenario-04.puml  
├── 05-secuencia-nombre-caso-uso-nombre-escenario-04.png 
├── 05-secuencia-nombre-caso-uso-nombre-escenario-05.puml 
└── 05-secuencia-nombre-caso-uso-nombre-escenario-05.png  
├── herramientas-agile/ 
│   ├── herramientas_agile.md 
│   └── tarjetas-crc/ 
│       
├── tarjetas_crc.md 
│       
│       
│       
│       
│       
│       
├── 01-tarjeta-crc-nombre-clase1.md 
├── 02-tarjeta-crc-nombre-clase2.md 
├── 03-tarjeta-crc-nombre-clase3.md 
├── 04-tarjeta-crc-nombre-clase4.md 
└── 05-tarjeta-crc-nombre-clase5.md 
└── ... (todas las tarjetas CRC de cada clase) 
├── ia/ 
│   ├── a2/ 
│   │   ├── disenador-tarjetas-crc.md 
│   │   ├── modelador-diagramas-casos-uso.md 
│   │   ├── especialista-escenarios.md 
│   │   └── documentador-coordinador.md 
│   └── a3/ 
│       
├── esp-actividades-1-2.md 
│       
│       
│       
├── esp-actividades-3-4-5.md 
├── esp-secuencia.md 
└── documentador-coordinador.md 
└── anexos/ 
├── anexos.md 
├── introduccion.md 
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
