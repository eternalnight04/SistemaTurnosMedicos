# Documentación: Especialista en Segregación de Interfaces (ISP)

## Prompt Utilizado en Copilot Agent Mode

```
Lees el siguiente contexto:
- anexos/introduccion.md (requisitos funcionales y no funcionales del sistema de turnos médicos)
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw (clases actuales: Paciente, Médico, Turno, Secretaria, Agenda)
- herramientas-agile/tarjetas-crc/ (responsabilidades de cada clase)

Tu tarea es:
1. Identificar responsabilidades en las clases actuales que podrían abstraerse en interfaces cohesivas
2. Detectar posibles "interfaces gordas" que obligarían a implementar métodos no utilizados
3. Proponer interfaces segregadas y específicas al dominio del sistema de turnos
4. Criar un diagrama UML PlantUML que muestre las interfaces propuestas y cómo las clases existentes las implementan
5. Generar un análisis técnico que explique por qué esta segregación de interfaces mejora el diseño

Revisa críticamente tu resultado:
- ¿Cada interfaz es cohesiva (agrupa métodos relacionados)?
- ¿Cada clase implementa solo las interfaces que necesita?
- ¿No hay métodos inútiles forzados en ninguna clase?
- ¿Las interfaces son específicas al dominio del sistema de turnos (no genéricas)?

Output esperado:
- Descripción de cada interfaz propuesta
- Justificación de por qué se segregan así
- Análisis de cómo esto mejora testabilidad y extensibilidad
```

---

## Archivos de Contexto Referenciados

1. **anexos/introduccion.md**
   - Proporcionó requisitos funcionales (RF01-RF05): crear, cancelar, reprogramar turnos; visualizar agenda; gestionar disponibilidad
   - Proporcionó requisitos no funcionales: no-superposición, trazabilidad, control de acceso diferenciado, extensibilidad
   - Contexto: Sistema de turnos médicos con actores: Paciente, Médico, Secretaria

2. **diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw**
   - Clases actuales: Paciente, Médico, Turno, Secretaria, Agenda
   - Relaciones: Paciente solicita Turno, Médico atiende, Secretaria gestiona, Agenda contiene Turnos

3. **herramientas-agile/tarjetas-crc/**
   - Responsabilidades de Paciente: solicitar turnos, cancelar, reprogramar
   - Responsabilidades de Médico: consultar agenda, atender pacientes, registrar observaciones
   - Responsabilidades de Secretaria: crear turnos, autorizar sobreturnos, registrar llegadas, gestionar agenda
   - Responsabilidades de Turno: registrar solicitud, asignar turno, modificar estado
   - Responsabilidades de Agenda: contener turnos, permitir consultas

---

## Output Obtenido de Copilot

Copilot generó el siguiente análisis:

### Interfaces Segregadas Propuestas:

1. **ICreadorTurnos**
   - Métodos: CrearTurno(), CancelarTurno(), ReprogramarTurno()
   - Implementada por: Paciente (crea/cancela/reprograma sus propios turnos), Secretaria (crea turnos para pacientes)
   - Razón: Operaciones de creación y modificación de turnos

2. **IGestorAgenda**
   - Métodos: ConsultarDisponibilidad(), ObtenerTurnosDelDia(), VerificarConflicto()
   - Implementada por: Médico (consulta su propia agenda), Secretaria (consulta agendas para crear turnos)
   - Razón: Operaciones de consulta y verificación de disponibilidad

3. **IGestorTurnosPersonales** (refinamiento)
   - Métodos: MisTurnos(), VerEstadoTurno()
   - Implementada por: Paciente (visualiza sus propios turnos)
   - Razón: Consultas específicas del paciente sobre sus turnos

4. **IAutorizador**
   - Métodos: AutorizarSobreturno(), TieneAutorizacion()
   - Implementada por: Secretaria (solo ella autoriza excepciones)
   - Razón: Operaciones de autorización que requieren validación

5. **IRegistrador**
   - Métodos: RegistrarLlegada(), RegistrarObservaciones(), ObtenerHistorial()
   - Implementada por: Médico (registra observaciones), Secretaria (registra llegadas)
   - Razón: Operaciones de logging y auditoría

---

## Ajustes Realizados al Output

### 1. **Separación de IGestorAgenda en dos contextos**

**Output inicial:** Una sola interfaz `IGestorAgenda` para consultar disponibilidad

**Ajuste:** Se refinó para considerar que:
- El Médico necesita ver su PROPIA agenda → método `MisTurnoDelDia()`
- La Secretaria necesita ver la agenda de OTROS → método `ConsultarDisponibilidadMedico()`

**Resultado:** Se propusieron dos interfaces en lugar de una, mejorando cohesión

### 2. **Corrección: No forzar IRegistrador en Paciente**

**Output inicial:** Proponía que Paciente implementara IRegistrador

**Ajuste:** Se descartó porque:
- Un Paciente NO registra llegadas (lo hace la Secretaria)
- Un Paciente NO registra observaciones (lo hace el Médico)
- Esto violaría ISP, forzando métodos inútiles

**Resultado:** Paciente NO implementa IRegistrador

### 3. **Refinamiento de cohesión en IRegistrador**

**Output inicial:** Mezclaba "registrar llegadas" con "registrar observaciones"

**Ajuste:** Se mantuvo como una sola interfaz porque:
- Aunque son diferentes, ambas son "operaciones de logging" de turnos
- La alternativa sería crear `IRegistradorLlegadas` + `IRegistradorObservaciones`, pero sería sobre-ingenierización
- Un solo IRegistrador mantiene balance entre segregación y mantenibilidad

**Resultado:** Una interfaz IRegistrador cohesiva pero no trivial

---

## Análisis Técnico Final

### Problema Resuelto por ISP

**Sin ISP** (interfaz gorda):
```csharp
public interface IGestorTurnosOmnipotente {
    // 15+ métodos mezclados
    void CrearTurno(...);
    void CancelarTurno(...);
    void ConsultarAgenda(...);
    void AutorizarSobreturno(...); // ❌ Paciente no debería implementar
    void RegistrarLlegada(...);   // ❌ Médico no debería implementar
}

public class Paciente : IGestorTurnosOmnipotente {
    // Se ve obligado a implementar 15 métodos, de los cuales solo usa 3-4
}
```

**Con ISP** (interfaces segregadas):
```csharp
public class Paciente : ICreadorTurnos, IGestorTurnosPersonales {
    // Implementa EXACTAMENTE 5 métodos que realmente necesita
}
```

### Beneficios Materializados

1. ✅ **Claridad:** Cada interfaz tiene un propósito claro y específico
2. ✅ **Flexibilidad:** Nuevos actores (Administrativo, Recepcionista) pueden implementar combinaciones diferentes
3. ✅ **Testabilidad:** Mocks pequeños y enfocados para cada interfaz
4. ✅ **Mantenibilidad:** Cambios en una interfaz no afectan clases que no la implementan
5. ✅ **Extensibilidad:** Agregar `INotificador` en el futuro no requiere rediseñar todo

### Mapeo de Responsabilidades

| Clase | ICreadorTurnos | IGestorAgenda | IAutorizador | IRegistrador | IGestorTurnosPersonales |
|-------|---|---|---|---|---|
| Paciente | ✅ | ❌ | ❌ | ❌ | ✅ |
| Médico | ❌ | ✅ | ❌ | ✅ | ❌ |
| Secretaria | ✅ | ✅ | ✅ | ✅ | ❌ |

---

## Decisiones de Diseño Documentadas

1. **¿Por qué no separar ConsultarAgenda en dos interfaces (MiAgenda vs AgendaOtros)?**
   - Porque ambas son "consultas de agenda" con el mismo concepto
   - Sobre-segregación reduciría mantenibilidad
   - El parámetro (medico: Médico) diferencia el contexto

2. **¿Por qué Secretaria implementa 4 interfaces?**
   - Es el actor más complejo del sistema
   - Tiene 4 responsabilidades claramente diferenciadas
   - ISP no prohíbe implementar múltiples interfaces

3. **¿Por qué crear IGestorTurnosPersonales separada de ICreadorTurnos?**
   - ICreadorTurnos: MODIFICAR mis turnos
   - IGestorTurnosPersonales: CONSULTAR mis turnos
   - Separar lectura de escritura sigue el principio CQRS y mejora testabilidad

---

## Conclusión

El análisis asistido por Copilot resultó en **5 interfaces segregadas y cohesivas** que:
- Mapean perfectamente las responsabilidades del dominio
- Evitan obligar a implementar métodos inútiles
- Mejoran la extensibilidad del sistema
- Facilitan las pruebas unitarias
- Mantienen el balance entre segregación y mantenibilidad

Esta aplicación de ISP, junto con las otras disciplinas SOLID, resultará en un diseño orientado a objetos de calidad profesional.
