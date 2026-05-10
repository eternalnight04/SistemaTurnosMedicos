# Documentador y Coordinador de Repositorio - Documentación Copilot

## Rol Asignado

**Natalia Carreras** (Matrícula: 161517) | Documentadora y Coordinadora de Repositorio | Actividad Obligatoria N°2

---

## Descripción General de Tareas

Como Documentador y Coordinador, asumí la responsabilidad de:

1. **Coordinación de Integración:** Gestionar la integración de todas las ramas feature/ en develop
2. **Code Reviews:** Realizar mínimo 4 code reviews asistidos con Copilot validando coherencia con A1
3. **Gestión de PRs:** Revisar y aprobar todas las PRs antes de integración a develop
4. **Documentación:** Registrar prompts y validaciones en este archivo
5. **Estructura del Proyecto:** Mantener formato de entrega en markdown
6. **Actualización de README:** Integrar índices nuevos (diagramasUML, herramientas_agile)
7. **Changelog:** Mantener registro actualizado de cambios
8. **Rama Release:** Crear release/actividad-obligatoria-2 desde develop

---

## Code Reviews Ejecutados

### Review 1: PR #51 - Modelador de Diagramas de Casos de Uso (Tomás)

**Objetivo:** Validar que los 5 diagramas PlantUML representen correctamente los casos de uso de A1 con actores y relaciones apropiadas.

**Prompt Utilizado (Copilot Agent Mode):**
```
Eres un experto en diagramas UML y diseño orientado a objetos. 
Lee el archivo anexos/introduccion.md para comprender los 5 casos de uso del sistema.
Luego revisa los archivos PlantUML en diagramas/02-casos-de-uso/:
- 02-caso-uso-crear-turno.puml
- 02-caso-uso-reprogramar-turno.puml
- 02-caso-uso-cancelar-turno.puml
- 02-caso-uso-autorizar-sobreturno.puml
- 02-caso-uso-registrar-llegada.puml

Valida que:
1. Los actores principales (Paciente, Médico, Secretaria) estén presentes
2. Las relaciones (<<include>>, <<extend>>) sean correctas y coherentes
3. Cada diagrama tenga extensiones/inclusiones lógicas
4. Los nombres de casos de uso coincidan con A1
5. La estructura sea profesional y legible

Dame un resumen de validación y sugerencias si hay inconsistencias.
```

**Validaciones Realizadas:**
- ✅ 5 diagramas presentes con nomenclatura correcta (02-caso-uso-*.puml)
- ✅ Actores identificados correctamente (Paciente, Médico, Secretaria, Sistema)
- ✅ Relaciones de inclusión/extensión coherentes con flujos de negocio
- ✅ Exportación a PNG realizada sin errores
- ✅ Índices creados: diagramasUML.md + diagramas_de_casos_de_uso.md
- ✅ Documentación Copilot: ia/a2/modelador-diagramas-casos-uso.md (47 líneas)

**Decisiones de Coordinación:**
- Solicitado ajuste de extensions para "Registrar Llegada" → Aprobado y mergeado

**Resultado:** ✅ **APROBADO - PR #51 MERGEADA A DEVELOP**

---

### Review 2: Validación de PR #54 - CRC Tarjeta 1 Paciente (Santiago)

**Objetivo:** Validar que las 5 tarjetas CRC presenten correctamente clases, superclases, responsabilidades y colaboraciones.

**Prompt Utilizado (Copilot Agent Mode):**
```
Eres experto en análisis orientado a objetos y tarjetas CRC.
Lee anexos/introduccion.md para entender el dominio del sistema de turnos médicos.
Luego revisa las tarjetas CRC en herramientas-agile/tarjetas-crc/:
- 01-tarjeta-crc-paciente.md
- 02-tarjeta-crc-medico.md
- 03-tarjeta-crc-turno.md
- 04-tarjeta-crc-agenda.md
- 05-tarjeta-crc-secretaria.md

Valida que cada tarjeta contenga:
1. Nombre de clase correcto
2. Superclase/subclase (si existe herencia)
3. Pensamiento del objeto claro y conciso
4. Responsabilidades coherentes con el rol
5. Colaboraciones identificadas
6. Propiedades listadas

Verifica que el conjunto de 5 tarjetas cubra todas las clases principales del boceto de A1.
Dame un reporte de completitud y coherencia.
```

**Validaciones Realizadas:**
- ✅ 5 tarjetas CRC individuales en archivos separados
- ✅ Nomenclatura correcta: 01-tarjeta-crc-[nombre].md
- ✅ Todos los campos completados (nombre, superclase, pensamiento, responsabilidades, colaboraciones, propiedades)
- ✅ Índice general: herramientas_agile.md vincula todas las tarjetas
- ✅ Coherencia con boceto de clases A1
- ✅ Documentación Copilot: ia/a2/disenador-tarjetas-crc.md (25 líneas)

**Decisiones de Coordinación:**
- Validación cruzada: Tarjetas CRC vs Diagramas casos de uso → Coherencia confirmada
- Ajuste de colaboraciones entre Turno ↔ Agenda → Solicitud hecha y completada

**Resultado:** ✅ **APROBADO - PRs #54-61 MERGEADAS A DEVELOP**

---

### Review 3: PR #48 - Especialista en Escenarios (Natalia)

**Objetivo:** Validar que los 5 escenarios contengan los 16 campos requeridos completos y coherentes con A1.

**Prompt Utilizado (Copilot Agent Mode):**
```
Eres especialista en modelado de casos de uso y escenarios de negocio.
Lee anexos/introduccion.md para entender el sistema de gestión de turnos.
Revisa los 5 escenarios en diagramas/03-escenarios-casos-de-uso/:
- 03-crear-turno-flujo-principal.md
- 03-reprogramar-turno-flujo-alterno.md
- 03-cancelar-turno-flujo-principal.md
- 03-autorizar-sobreturno-flujo-principal.md
- 03-registrar-llegada-flujo-principal.md

Valida que cada escenario contenga:
1. Nombre del escenario descriptivo
2. ID única (03-001, 03-002, etc.)
3. Área del sistema
4. Actor(es) involucrado(s)
5. Descripción clara del propósito
6. Evento activador
7. Tipo de señal (externa/temporal)
8. Pasos desempeñados (flujo principal)
9. Precondiciones
10. Postcondiciones
11. Suposiciones
12. Requerimientos
13. Aspectos sobresalientes
14. Prioridad (Alta/Media/Baja)
15. Riesgo (Alto/Medio/Bajo)
16. Referencias a casos de uso primarios

Verifica coherencia con los diagramas de casos de uso y proporciona reporte de completitud.
```

**Validaciones Realizadas:**
- ✅ 5 escenarios en archivos individuales con nomenclatura correcta
- ✅ Los 16 campos completados en cada escenario
- ✅ Flujos principales coherentes y detallados
- ✅ Precondiciones/Postcondiciones bien definidas
- ✅ Prioridades y riesgos justificados
- ✅ Índice general: escenarios_de_casos_de_uso.md
- ✅ Documentación Copilot: ia/a2/especialista-escenarios.md (336 líneas, muy completo)

**Decisiones de Coordinación:**
- Validación contra A1: Todos los escenarios mapean a casos de uso documentados
- Esta PR fue mergeada early durante desarrollo (fue la primera en mergearse por orden cronológico)

**Resultado:** ✅ **APROBADO - PR #48 MERGEADA A DEVELOP**

---

### Review 4: PR #63 - Documentación Diseñador CRC (Santiago)

**Objetivo:** Validar que el archivo ia/a2/disenador-tarjetas-crc.md contenga documentación completa del proceso Copilot.

**Prompt Utilizado (Copilot Agent Mode):**
```
Revisa el archivo ia/a2/disenador-tarjetas-crc.md.
Verifica que documente completamente:
1. El prompt utilizado en Copilot Agent Mode
2. Los archivos de contexto referenciados (anexos/introduccion.md, excalidraw)
3. Los ajustes realizados al output de la IA
4. Decisiones de diseño tomadas
5. Una reflexión sobre la efectividad de Copilot

Valida que el archivo tenga entre 20-50 líneas con suficiente detalle.
Compara estructura con ia/a2/modelador-diagramas-casos-uso.md y 
ia/a2/especialista-escenarios.md para consistencia.
```

**Validaciones Realizadas:**
- ✅ Archivo existe: ia/a2/disenador-tarjetas-crc.md
- ✅ Nombre de archivo correcto (no "disenador-crc-cards.md")
- ✅ Contenido correcto: Documentación proceso Copilot (no resumen de CRC cards)
- ✅ Estructura: Prompt → Contexto → Ajustes → Decisiones → Reflexión
- ✅ Líneas: 25 líneas (dentro del rango esperado)
- ✅ Coherencia con otros archivos ia/a2/

**Decisiones de Coordinación:**
- Requirió corrección (fue intento #2 de Santiago)
- Primera versión tenía nombre incorrecto y contenido equivocado
- Segunda versión (PR #63) corregida exitosamente

**Resultado:** ✅ **APROBADO - PR #63 MERGEADA A DEVELOP**

---

## Resumen de Coordinación General

### PRs Gestionadas
| # | Tipo | Responsable | Estado | Nota |
|---|------|-------------|--------|------|
| #48 | Feature | Natalia (Especialista) | ✅ Mergeada | Escenarios - A1 |
| #51 | Feature | Tomás (Modelador) | ✅ Mergeada | Diagramas CU - A2 |
| #54-61 | Feature | Santiago (Diseñador) | ✅ Mergeada | CRC Tarjetas - A2 |
| #63 | Feature | Santiago (Diseñador) | ✅ Mergeada | Doc Diseñador - A2 |

### Issues Creadas y Cerradas
- Issue #47: A2 - Coordinación General de Entrega (se cierra con PR release)
- Issues individuales de cada rol (se cerraron al mergear PRs)

### Validaciones Clave Ejecutadas

1. **Coherencia A1 → A2:** Todos los artefactos A2 mapean correctamente a requisitos de A1
2. **Completitud:** 3 artefactos principales entregados por 3 roles
3. **Documentación Copilot:** 4 archivos ia/a2/ documentando procesos IA
4. **Estructura de Carpetas:** Cumplimiento total del formato requerido
5. **Changelog:** Actualizado en cada PR
6. **README:** Actualizado con índices nuevos y enlaces

---

## Decisiones de Diseño y Coordinación

1. **Orden de Merges:** Especialista → Modelador → Diseñador → Release
   - Justificación: Dependencias de validación (escenarios definen casos, diagramas los representan, CRC detalla clases)

2. **Duplicación de Rol:** Natalia asumió Especialista + Coordinadora
   - Necesidad: Continuidad coordinativa desde A1
   - Documentación: Registrada en changelog.md

3. **Template de PRs:** Feature template + Release template
   - Implementados en .github/PULL_REQUEST_TEMPLATE/
   - Automatizados para uso de todos los colaboradores

4. **Branch Protection:** develop protegida
   - Requiere aprobación de coordinador antes de merge
   - master protegida: solo desde release/ con LGTM profesor

---

## Reflexión sobre el Proceso

### Fortalezas del Uso de Copilot
- ✅ Validación rápida de coherencia entre artefactos
- ✅ Checklists automáticos de completitud
- ✅ Sugerencias de mejora basadas en estándares UML
- ✅ Acceleró el proceso de code review

### Desafíos Encontrados
- ❌ Primera versión de PR #63 (Santiago) requirió corrección
- ❌ Nombres de archivos críticos: necesitó claridad sobre nomenclatura

### Recomendaciones para A3
1. Clarificar naming conventions al inicio del trabajo
2. Template checklist para cada rol
3. Reunión inicial con Copilot para alineación

---

## Archivos de Referencia

- [Introducción Sistema](../../anexos/introduccion.md)
- [Diagramas de Casos de Uso](../../diagramas/02-casos-de-uso/diagramas_de_casos_de_uso.md)
- [Tarjetas CRC](../../herramientas-agile/herramientas_agile.md)
- [Escenarios](../../diagramas/03-escenarios-casos-de-uso/escenarios_de_casos_de_uso.md)
- [Changelog](../../changelog.md)

---

**Generado por:** Natalia Carreras (Coordinadora)  
**Fecha:** 17 de Abril de 2026  
**Estado:** Completado | Listo para Release