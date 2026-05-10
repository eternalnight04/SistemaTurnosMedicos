# Principio de Responsabilidad Única (SRP)

## 1. Qué es la Responsabilidad Única

El Principio de Responsabilidad Única (SRP - Single Responsibility Principle) establece que **una clase debe tener una única razón para cambiar**, es decir, debe tener una única responsabilidad o motivo para modificarse.

Una clase con una sola responsabilidad es:
- **Más fácil de entender**: su propósito es claro y delimitado
- **Más fácil de mantener**: los cambios son localizados
- **Más fácil de probar**: una responsabilidad = pruebas enfocadas
- **Más reutilizable**: clases cohesivas son componentes independientes

## 2. Problemas de Violar SRP

Cuando una clase tiene múltiples responsabilidades, puede sufrir de:

- **Acoplamiento alto**: cambios en una responsabilidad afectan a otras
- **Difícil de probar**: necesita testear múltiples aspectos en una sola clase
- **Baja cohesión**: métodos no relacionados en la misma clase
- **Difícil de reutilizar**: la clase hace demasiadas cosas para usarla en otros contextos

### Ejemplo de violación en Sistema de Turnos:

```java
class Turno {
    private Paciente paciente;
    private Especialista especialista;
    private LocalDateTime horario;
    
    // Responsabilidad 1: Gestionar datos del turno
    public void agendarTurno() { }
    public void cancelarTurno() { }
    
    // Responsabilidad 2: Persistencia en base de datos
    public void guardarEnBD() { }
    public void cargarDeBD() { }
    
    // Responsabilidad 3: Validar reglas de negocio
    public boolean esValido() { }
    public void validarDisponibilidad() { }
    
    // Responsabilidad 4: Generar reportes
    public String generarReporte() { }
    public void exportarCSV() { }
}
```

Esta clase `Turno` viola SRP porque tiene 4 responsabilidades diferentes.

## 3. Análisis de Responsabilidades en Sistema de Turnos

En el Sistema de Turnos Médicos, podemos identificar las siguientes responsabilidades principales:

- **Paciente**: gestionar datos personales y médicos del paciente
- **Especialista**: gestionar información del profesional médico
- **Turno**: representar la cita médica y sus estados
- **Agenda**: organizar y coordinar turnos
- **ControladorTurnos**: orquestar las operaciones de turnos
- **Notificador**: comunicar cambios a pacientes y especialistas
- **Repositorio/Persistencia**: guardar y recuperar datos

Cada una debe tener **una única responsabilidad** y no más.

## 4. Aplicación de SRP al Sistema

### Antes (Violando SRP):
```java
class Turno {
    // Datos
    private Paciente paciente;
    private Especialista especialista;
    private LocalDateTime horario;
    private EstadoTurno estado;
    
    // Métodos de gestión
    public void agendar() { }
    public void cancelar() { }
    
    // Métodos de validación
    public boolean puedeCancelarse() { }
    
    // Métodos de persistencia
    public void guardar() { }
    
    // Métodos de notificación
    public void notificarCambios() { }
}
```

### Después (Aplicando SRP):

**Clase Turno** - Responsabilidad: Representar un turno y su estado
```java
public class Turno {
    private Paciente paciente;
    private Especialista especialista;
    private LocalDateTime horario;
    private EstadoTurno estado;
    
    public EstadoTurno getEstado() { return estado; }
    public void cambiarEstado(EstadoTurno nuevoEstado) { }
    public LocalDateTime getHorario() { return horario; }
}
```

**Clase GestorTurnos** - Responsabilidad: Orquestar operaciones de turnos
```java
public class GestorTurnos {
    private RepositorioTurnos repositorio;
    private NotificadorTurnos notificador;
    
    public void agendar(Turno turno) {
        repositorio.guardar(turno);
        notificador.notificarAgendamiento(turno);
    }
    
    public void cancelar(Turno turno) {
        turno.cambiarEstado(EstadoTurno.CANCELADO);
        repositorio.actualizar(turno);
        notificador.notificarCancelacion(turno);
    }
}
```

**Clase RepositorioTurnos** - Responsabilidad: Persistencia de datos
```java
public class RepositorioTurnos {
    public void guardar(Turno turno) { /* SQL */ }
    public Turno obtener(long id) { /* SQL */ }
    public void actualizar(Turno turno) { /* SQL */ }
    public void eliminar(long id) { /* SQL */ }
}
```

**Clase NotificadorTurnos** - Responsabilidad: Enviar notificaciones
```java
public class NotificadorTurnos {
    private INotificador notificador;
    
    public void notificarAgendamiento(Turno turno) {
        String mensaje = "Su turno ha sido agendado para " + turno.getHorario();
        notificador.notificar(mensaje, turno.getPaciente());
    }
    
    public void notificarCancelacion(Turno turno) {
        String mensaje = "Su turno ha sido cancelado";
        notificador.notificar(mensaje, turno.getPaciente());
    }
}
```

**Clase ValidadorTurnos** - Responsabilidad: Validar reglas de negocio
```java
public class ValidadorTurnos {
    public boolean puedeAgendarse(Turno turno) { }
    public boolean puedeCancelarse(Turno turno) { }
    public boolean horarioDisponible(LocalDateTime horario) { }
}
```

## 5. Beneficios de Aplicar SRP

Al dividir responsabilidades:

1. **Mantenibilidad mejorada**: cambios en persistencia no afectan lógica de negocio
2. **Testabilidad**: cada clase se prueba de forma aislada y enfocada
3. **Reusabilidad**: `RepositorioTurnos` puede usarse desde múltiples gestores
4. **Flexibilidad**: cambiar base de datos solo requiere cambiar `RepositorioTurnos`
5. **Colaboración**: cada desarrollador puede trabajar en una clase/responsabilidad

## 6. Checklist para Identificar Violaciones de SRP

Para saber si una clase viola SRP, pregúntate:

- ¿Tiene más de una razón para cambiar?
- ¿Tiene métodos que no usan los mismos atributos?
- ¿Puedo describir la clase en una sola frase sin usar "y"?
- ¿Necesito importar muchas dependencias externas?
- ¿Qué clases dependen de esta? ¿Son por diferentes razones?

Si contestas "sí" a varias preguntas, probablemente violes SRP.

## 7. Resumen

El Principio de Responsabilidad Única es fundamental para escribir código mantenible. En el Sistema de Turnos Médicos, separar claramente las responsabilidades de gestión, persistencia, validación y notificación resulta en un diseño más robusto, flexible y fácil de mantener.
