# Principios SOLID aplicados a SistemaTurnosMedicos

**Autor:** @nachonervi-design  
**Rol:** Especialista en Patrones Creacionales  
**Fecha:** Junio 2026  
**Asignatura:** Diseño Orientado a Objetos - Segundo Parcial

---

## 📋 Índice de Principios SOLID

Los principios SOLID son cinco principios de diseño orientados a objetos que ayudan a crear software más mantenible, flexible y escalable. En este documento se presenta la aplicación de cada principio al Sistema de Turnos Médicos.

### Principios

| # | Principio | Archivo | Descripción |
|---|-----------|---------|-------------|
| 1 | **SRP** - Single Responsibility Principle | [01-srp.md](./01-srp.md) | Cada clase debe tener una única responsabilidad |
| 2 | **OCP** - Open/Closed Principle | [02-ocp.md](./02-ocp.md) | Abierto para extensión, cerrado para modificación |
| 3 | **LSP** - Liskov Substitution Principle | [03-lsp.md](./03-lsp.md) | Las subclases deben ser sustituibles por sus superclases |
| 4 | **ISP** - Interface Segregation Principle | [04-isp.md](./04-isp.md) | Muchas interfaces específicas son mejores que una general |
| 5 | **DIP** - Dependency Inversion Principle | [05-dip.md](./05-dip.md) | Depender de abstracciones, no de implementaciones concretas |

---

## 🎯 Aplicación en el Sistema

Los principios SOLID se aplican de forma transversal en todo el diseño del Sistema de Turnos Médicos, complementándose con:

- **Patrones de Diseño:** [Patrón Builder](../patrones-diseno/patron-de-diseno-creacional.md) aplicado a la clase `Turno`
- **Diagrama de Clases Final:** [06-clases-diagrama-final.puml](../../diagramas/01-diagrama-clases/06-clases-diagrama-final.puml)
- **Tarjetas CRC:** [herramientas-agile/tarjetas-crc/](../../herramientas-agile/tarjetas-crc/)
- **Pilares POO:** [pilares-poo.md](../analisis-funcional/pilares-poo.md)

---

## 📊 Resumen de Aplicación

| Principio | Clases que lo Aplican | Beneficio Principal |
|-----------|----------------------|---------------------|
| **SRP** | UsuarioDelSistema, Turno, Agenda | Cohesión alta, mantenimiento fácil |
| **OCP** | UsuarioDelSistema, TurnoEstado | Extensibilidad sin romper código existente |
| **LSP** | Paciente, Medico, Secretaria | Sustitución segura en jerarquía de herencia |
| **ISP** | Interfaces de notificación, autenticación | Interfaces específicas para cada necesidad |
| **DIP** | Agenda, Turno, Secretaria | Desacoplamiento entre componentes |

---

## 🔗 Diagramas UML de los Principios

Cada principio tiene su propio diagrama de clases que ilustra su aplicación:

1. [01-solid-srp.puml](../../diagramas/01-diagrama-clases/01-solid-srp.puml) - SRP
2. [02-solid-ocp.puml](../../diagramas/01-diagrama-clases/02-solid-ocp.puml) - OCP
3. [03-solid-lsp.puml](../../diagramas/01-diagrama-clases/03-solid-lsp.puml) - LSP
4. [04-solid-isp.puml](../../diagramas/01-diagrama-clases/04-solid-isp.puml) - ISP
5. [05-solid-dip.puml](../../diagramas/01-diagrama-clases/05-solid-dip.puml) - DIP

---

**Documento generado por:** @nachonervi-design  
**Repositorio:** [SistemaTurnosMedicos](https://github.com/eternalnight04/SistemaTurnosMedicos)
