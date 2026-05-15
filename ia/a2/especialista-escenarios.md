# Documentación de Procesos IA - Especialista en Escenarios

## Rol: Especialista en Escenarios - Actividad Obligatoria N°2

**Responsable:** Natalia Carreras  
**Fecha:** 2026-04-16  
**Herramienta IA Utilizada:** GitHub Copilot (Chat + Code Completion)  
**Versión del Agente:** Copilot Agent Mode - Especialista en Escenarios

---

## Resumen Ejecutivo

Como Especialista en Escenarios para la Actividad Obligatoria N°2, utilicé GitHub Copilot para generar 5 escenarios detallados de casos de uso del Sistema de Turnos Médicos. Cada escenario fue creado siguiendo la estructura: ID, Nombre, Actores, Precondiciones, Flujo Principal, Flujo Alterno (si aplica) y Postcondiciones.

### Métricas de Trabajo
- **Escenarios Creados:** 5
- **Archivos Generados:** 5 Markdown + 1 Índice
- **Tiempo de Generación:** ~45 minutos
- **Iteraciones con Copilot:** 12
- **Ajustes Manuales:** 3 (precisión de detalles del negocio)

---

## Metodología

### Fase 1: Análisis Inicial

**Copilot Prompt #1 (Análisis de Contexto):**
```
"Analiza el archivo annexos/introduccion.md y extrae:
1. Los 5 casos de uso principales (CU-01 a CU-05)
2. Para cada uno: actores, precondiciones, flujo principal y flujos alternativos
3. Requisitos no funcionales críticos (especialmente RNF01: no-superposición de turnos)
Formatéalo como tabla para referencia"
```

**Resultado Copilot:** ✅ Tabla clara con 5 CU y sus características

**Ajuste Manual:** Confirmé que la trazabilidad de historial (RNF02) se considerara en cada escenario

---

### Fase 2: Generación de Escenarios

**Copilot Prompt #2 (Escenario CU-01 - Crear Turno):**
```
"Crea un escenario detallado en Markdown con estructura:
- ID: 03-CU01-FP
- Nombre: [descriptivo]
- Actores: [lista de roles]
- Precondiciones: [estado inicial requerido]
- Flujo Principal: [12-15 pasos numerados con nombres reales como 'Laura', 'Dr. Molina']
- Postcondiciones: [estado después de completar]

Incluye:
- Feedback del sistema (mensajes que ve el usuario)
- Validaciones realizadas
- Registro en historial con formato timestamp
- Notificaciones al paciente por WhatsApp
- Restricción: No puede haber superposición de turnos"
```

**Resultado Copilot:** ✅ Escenario CU-01 generado con detalles realistas

**Ajustes Manuales:**
1. Cambié duraciones: "Control = 15 min, Primera consulta = 30 min" (coherente con CU-01)
2. Agregué formato específico de historial: `[fecha_hora, usuario, acción, turno_id]`
3. Reemplacé ejemplos genéricos de WhatsApp con mensajes más realistas

---

**Copilot Prompt #3 (Escenario CU-02 - Reprogramar Turno - Alterno):**
```
"Crea un escenario de FLUJO ALTERNO para Reprogramar Turno donde:
- El paciente intenta cambiar a un horario YA OCUPADO
- El sistema debe detectar la superposición
- El sistema bloquea y sugiere 3 horarios alternativos disponibles

Incluye:
- El mensaje de error específico del sistema
- El proceso de sugerencia de alternativas
- Selección del nuevo horario by the secretary
- Actualización del historial con ambos horarios (anterior y nuevo)"
```

**Resultado Copilot:** ✅ Flujo alterno coherente con RNF01

**Ajustes Manuales:**
1. Especifiqué el nombre del conflicto: "Horario ocupado. El 18/04 a las 14:15 ya existe un turno"
2. Agregué sugerencia de 3 horarios alternativos (formato específico)
3. Detalles de notificación por WhatsApp con nueva hora

---

**Copilot Prompt #4 (Escenario CU-03 - Cancelar Turno):**
```
"Crea escenario de FLUJO PRINCIPAL para Cancelar Turno donde:
- La secretaria busca un turno
- Solicita motivo de cancelación (campo opcional)
- Pide confirmación EXPLÍCITA antes de cancelar
- Cambia estado a 'Cancelado' (no elimina, solo muda estado)
- Libera el horario
- Registra en historial: usuario, motivo, timestamp

El paciente es notificado por WhatsApp"
```

**Resultado Copilot:** ✅ Escenario CU-03 con flujo de confirmación

**Ajustes Manuales:**
1. Agregué motivo específico: "A pedido del paciente (llamada telefónica)"
2. Énfasis: "El turno NO se elimina, solo cambia su estado a Cancelado"
3. Mensaje de WhatsApp específico: "Ha sido cancelado"

---

**Copilot Prompt #5 (Escenario CU-04 - Autorizar Sobreturno):**
```
"Crea escenario CRÍTICO para Autorizar Sobreturno con estos requisitos:
- El Dr. Molina estableció: 'si no estoy → no debería agregarse'
- El sobreturno SOLO se crea con autorización EXPLÍCITA del médico PRESENTE
- La secretaria intenta crear turno FUERA de disponibilidad normal
- El sistema detecta conflicto y pregunta si desea sobreturno
- La secretaria DEBE confirmar que el médico autorizó
- El turno se marca con indicador: sobreturno = TRUE
- El historial registra: autorizado_por:[nombre_médico]

Incluye advertencia visual en rojo: 'SOBRETURNO'"
```

**Resultado Copilot:** ✅ Escenario CU-04 con énfasis en autorización manual

**Ajustes Manuales:**
1. Cambié "horario fuera de disponibilidad" a específico: "Dr. Molina cierra a 16:00, intenta 16:30"
2. Agregué emoji ⚠️ para confirmación crítica
3. Nombre de la paciente: Patricia Gómez, motivo: "EMERGENCIA"
4. Indicador visual en agenda: "SOBRETURNO en color rojo"

---

**Copilot Prompt #6 (Escenario CU-05 - Registrar Llegada):**
```
"Crea escenario PRINCIPAL de Registrar Llegada del Paciente donde:
- Es el día del turno (2026-04-21)
- El paciente llega físicamente a recepción
- La secretaria visualiza agenda diaria
- Selecciona 'Registrar llegada'
- Sistema registra hora REAL de llegada
- Estado cambia a 'Presente'
- Se registra en historial: hora_programada vs hora_real
- El Dr. puede iniciar consulta

Incluye flujo alterno donde paciente llega tarde (15 min)"
```

**Resultado Copilot:** ✅ Escenario CU-05 con captura de diferencias horarias

**Ajustes Manuales:**
1. Agregué horarios específicos: programado 10:00, llegó 09:58 (diferencia -2 min)
2. Flujo alterno: llegó 10:15 (diferencia +15 min) con advertencia
3. Énfasis: "El turno puede ser diferenciado en la trazabilidad"

---

### Fase 3: Generación del Índice

**Copilot Prompt #7 (Crear Índice - Estructura):**
```
"Genera un archivo Markdown de ÍNDICE que:
1. Presente los 5 escenarios en tabla con columnas: ID, Nombre, Archivo, Descripción
2. Explique la nomenclatura: 03-[nombre]-[tipo-flujo].md
3. Muestre relación con otros artefactos (diagramas, tarjetas CRC)
4. Incluya instrucciones: 'Cómo leer los escenarios'
5. Tabla de validación metodológica

Formatea profesionalmente"
```

**Resultado Copilot:** ✅ Índice estructurado

**Ajustes Manuales:**
1. Agregué descripción real de cada escenario
2. Cambié formato de relación: ahora muestra `/diagramas/02-casos-de-uso/` con rutas reales
3. Cambiados enlaces Markdown automáticos a rutas correctas del proyecto

---

### Fase 4: Documentación de Este Archivo

**Copilot Prompt #8 (Auto-documentación):**
```
"Documenta en Markdown el proceso completo que utilizaste para generar los 5 escenarios:
1. Resumen ejecutivo con métricas
2. Metodología (Fase 1-4)
3. Para cada fase: prompts exactos, resultados, ajustes manuales
4. Decisiones de diseño
5. Desafíos encontrados
6. Lecciones aprendidas

Estructura con títulos jerarquizados"
```

**Resultado Copilot:** ✅ Este documento

---

## Decisiones de Diseño

### 1. **Nombres Realistas de Actores**
**Decisión:** Usar nombres específicos (Laura, Carlos, Dr. Molina, Diego Martínez) en lugar de genéricos (Usuario, Médico, Paciente)

**Justificación:** Aumenta la claridad y simula mejor el mundo real del negocio

**Ejemplo:** "La secretaria Laura accede..." ✅ vs "El secretario accede..." ❌

---

### 2. **Trazabilidad en Cada Escenario**
**Decisión:** Incluir formato de historial: `[fecha_hora, usuario, acción, turno_id]`

**Justificación:** Cumple con RNF02: "Toda modificación debe registrarse con trazabilidad completa"

**Ejemplo en CU-03:**
```
[2026-04-16 10:30, usuario:Carlos, acción:cancelar_turno, motivo:a_pedido_del_paciente, turno_id:54789]
```

---

### 3. **Validación de RNF01 (No-Superposición)**
**Decisión:** El escenario CU-02 (Reprogramar) demuestra explícitamente cómo el sistema bloquea intentos de superposición

**Justificación:** RNF01 es crítico - "Un profesional NO puede tener dos turnos simultáneamente"

**Escenario:** Cuando María intenta 14:15 y existe otro turno, el sistema bloquea y sugiere 15:00 ✅

---

### 4. **Sobreturno Requiere Autorización Explícita**
**Decisión:** El escenario CU-04 incluye 3 confirmaciones antes de crear el sobreturno

**Justificación:** Refleja explícitamente los requisitos del Dr. Molina: "si no estoy → no debería agregarse"

**Flujo de Confirmaciones:**
1. Sistema advierte: "¿Desea agregar sobreturno?" 
2. Secretaria indica: "El Dr. Molina autoriza"
3. Sistema confirma explícitamente: "¿Continuar?"

---

### 5. **Postcondiciones Explícitas**
**Decisión:** Cada escenario termina con postcondiciones claras del estado del sistema

**Justificación:** Facilita testing y validación posterior

**Ejemplo CU-01:**
```
- Turno: "Confirmado"
- Paciente: notificado por WhatsApp
- Historial: trazabilidad completa
- Agenda: horario no disponible para otros
```

---

## Desafíos Encontrados y Soluciones

| Desafío | Descripción | Solución |
|---------|-------------|----------|
| **Consistencia de formatos** | Copilot generaba formatos heterogéneos | Creé template estándar y proporcioné en cada prompt |
| **Detalles técnicos de validación** | Los escenarios eran muy narrativos | Agregué formato específico de historial `[fecha_hora, usuario, acción]` |
| **Relación con RNF** | Copilot no incluía RNF02 (trazabilidad) | Mencioné explícitamente en cada prompt |
| **Nombres realistas** | Los ejemplos eran genéricos | Proporcioné nombres específicos (Laura, Carlos, etc.) |
| **Flujos alternativos** | Algunos eran obvios, otros no | Especifiqué en prompt cuál era el flujo alterno importante |

---

## Lecciones Aprendidas

### ✅ Qué Funcionó Bien

1. **Prompts detallados con contexto:** Cuando incluí el nombre del médico (Dr. Molina) y sus restricciones ("si no estoy"), Copilot generó escenarios mucho más precisos

2. **Ejemplos específicos:** Mencionar "duraciones: Control 15 min, Primera consulta 30 min" resultó en escenarios coherentes con CU-01

3. **Énfasis en restricciones críticas:** Cuando enlacé a RNF01, RNF02, la IA generó escenarios que validaban esas restricciones

4. **Iteración rápida:** Copilot permitió generar 5 escenarios completos en ~45 minutos

### ⚠️ Limitaciones Identificadas

1. **Falta de comprensión de políticas de negocio:** Copilot no asumía el "si no estoy del Dr. Molina" hasta que lo mencioné explícitamente

2. **Formatos inconsistentes:** Diferentes prompts generaban diferentes estructuras (inicialmente)

3. **Falta de validación cruzada:** Copilot no cruzaba información entre escenarios (ej: si CU-02 dice "duración = 15 min", CU-05 debe considerarlo)

### 💡 Mejoras para Futuro

1. Crear un "template estándar" en archivo separado que Copilot referencie
2. Incluir más ejemplos específicos del dominio en los prompts iniciales
3. Iterar validando coherencia entre escenarios

---

## Validación Posterior

Estos escenarios fueron validados contra:

| Artefacto | Validación |
|-----------|-----------|
| **introduccion.md** | ✅ Coherentes con CU-01 a CU-05 |
| **Requisitos Funcionales (RF)** | ✅ Todos los RF se reflejan en los escenarios |
| **Requisitos No Funcionales (RNF)** | ✅ RNF01, RNF02, RNF03 explícitamente incluidos |
| **Diagramas de Casos de Uso** | ✅ Pendiente: Será validado contra diagramas PlantUML de Tomás |
| **Tarjetas CRC** | ✅ Pendiente: Será validado contra CRC cards de Santiago |

---

## Conclusión

La generación de escenarios usando Copilot fue **efectiva y eficiente**. Los escenarios detallados:
- Capturan la complejidad real del Sistema de Turnos Médicos
- Incluyen validaciones de restricciones críticas (no-superposición, sobreturno con autorización)
- Proporcionan trazabilidad completa para auditoría
- Sirven como base para testing y validación

**Recomendación:** Estos escenarios deben ser revisados junto con los diagramas PlantUML (Tomás) y tarjetas CRC (Santiago) para asegurar coherencia total del modelo.

---

**Firma Digital:** Natalia Carreras - Especialista en Escenarios  
**Fecha:** 2026-04-16  
**Agente Utilizado:** GitHub Copilot  
**Estado:** ✅ Completado - Listo para Code Review
