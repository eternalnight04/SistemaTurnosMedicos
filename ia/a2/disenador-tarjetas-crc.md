# Diseñador de Tarjetas CRC - Documentación Copilot

## Prompt utilizado

Se utilizó Copilot Agent Mode con este prompt:

```
Analizando anexos/introduccion.md y el boceto de clases de A1, 
genera 5 tarjetas CRC para Paciente, Médico, Turno, Agenda y Secretaria.
Cada tarjeta debe incluir: nombre, responsabilidades, colaboraciones, propiedades.
```

## Archivos de contexto
- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw

## Iteraciones con Copilot

**Iteración 1:** Generación inicial de 5 tarjetas CRC
- Output: Estructura base con nombre, responsabilidades (3-4 por clase), colaboraciones

**Iteración 2:** Validación y coherencia
- Ajuste: Mejorar completitud de colaboraciones
- Ajuste: Alineación de responsabilidades con casos de uso

**Iteración 3:** Output final
- Iteraciones totales: 3 ciclos de generación y validación

## Ajustes realizados manualmente por clase

### Paciente
- Se agregaron responsabilidades: solicitar turno, autenticarse, gestionar datos personales
- Colaboradores: Sistema, Turno, Secretaria
- Superclase definida: UsuarioDelSistema

### Médico
- Se corrigieron responsabilidades relacionadas a gestión de agenda
- Se agregó superclase explícita: UsuarioDelSistema
- Validación: propiedades alineadas con atributos del boceto

### Turno
- Responsabilidades validadas contra flujos de casos de uso
- Se mantuvo estructura ya coherente

### Agenda
- Se validó relación con Médico y Turno
- Propiedades confirmed

### Secretaria
- Se agregó superclase: UsuarioDelSistema
- Se expandieron responsabilidades para incluir autorización de sobreturnos
- Se agregó colaboración con LlegadaPaciente

## Decisiones de diseño
- 5 clases clave reflejan actores principales y entidades de negocio del sistema
- Jerarquía de herencia: Paciente, Médico y Secretaria heredan de UsuarioDelSistema
- Colaboraciones alineadas explícitamente con flujos de casos de uso de A1
- LlegadaPaciente se decidió como nueva entidad para separar planificación (Turno) de realidad física (registro de llegada)

## Reflexión
Copilot generó estructuras base de calidad, pero requirió validación manual contra el dominio del problema (consulta médica, roles reales, requisitos de negocio) para asegurar coherencia OO completa. La iteración fue importante para refinar colaboraciones y jerarquía de herencia. El trabajo demuestra que la IA es generadora de opciones pero la validación semántica y de dominio requiere revisión experta.
