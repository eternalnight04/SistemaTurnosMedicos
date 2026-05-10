# Principio Abierto/Cerrado (OCP)

## 1. Qué es el Principio Abierto/Cerrado

El Principio Abierto/Cerrado (OCP - Open/Closed Principle) establece que **las clases deben estar abiertas para extensión pero cerradas para modificación**.

Esto significa:
- **Abierto para extensión**: podemos añadir nuevas funcionalidades sin cambiar código existente
- **Cerrado para modificación**: el código existente no debe ser modificado para soportar nuevas funcionalidades

Se logra mediante:
- Herencia y polimorfismo
- Interfaces y clases abstractas
- Composición y delegación
- Patrones de diseño (Strategy, Decorator, Factory, etc.)

## 2. Problema de Violar OCP

Cuando un sistema no es abierto para extensión, cada nueva funcionalidad requiere modificar código existente:

```java
// ❌ VIOLA OCP
class NotificadorTurnos {
    public void notificar(String tipo, String mensaje, Paciente paciente) {
        if (tipo.equals("EMAIL")) {
            // Lógica para enviar email
            System.out.println("Enviando email a " + paciente.getEmail());
        } else if (tipo.equals("SMS")) {
            // Lógica para enviar SMS
            System.out.println("Enviando SMS a " + paciente.getTelefono());
        } else if (tipo.equals("WHATSAPP")) {
            // Lógica para enviar WhatsApp
            System.out.println("Enviando WhatsApp a " + paciente.getTelefono());
        }
        // Cada nuevo tipo requiere modificar esta clase ❌
    }
}
```

**Problema**: Para añadir un nuevo canal de notificación (Telegram, Push, etc.), hay que modificar `NotificadorTurnos`.

## 3. Análisis de Puntos de Extensión en Sistema de Turnos

El Sistema de Turnos Médicos tiene varios puntos que necesitan ser abiertos para extensión:

### Notificaciones
- Actualmente: Email
- Futuro: SMS, WhatsApp, Push, Telegram

### Tipos de Turnos
- Actualmente: Presencial
- Futuro: Telemedicina, Urgencia, Domiciliario

### Persistencia
- Actualmente: Base de datos relacional
- Futuro: NoSQL, API externa, caché

### Validaciones
- Actualmente: horarios disponibles
- Futuro: conflictos con otros turnos, capacidad de consultorios

## 4. Aplicación de OCP al Sistema

### Solución para Notificaciones (Usar Interfaces):

**Interfaz Notificador** - Abierta para extensión:
```java
public interface INotificador {
    void notificar(String mensaje, Paciente paciente);
}
```

**Implementaciones concretas** - Cerradas para modificación:
```java
public class NotificadorEmail implements INotificador {
    @Override
    public void notificar(String mensaje, Paciente paciente) {
        System.out.println("Enviando email a " + paciente.getEmail());
        // Lógica SMTP
    }
}

public class NotificadorSMS implements INotificador {
    @Override
    public void notificar(String mensaje, Paciente paciente) {
        System.out.println("Enviando SMS a " + paciente.getTelefono());
        // Lógica SMS API
    }
}

public class NotificadorWhatsApp implements INotificador {
    @Override
    public void notificar(String mensaje, Paciente paciente) {
        System.out.println("Enviando WhatsApp a " + paciente.getTelefono());
        // Lógica WhatsApp API
    }
}

// Futura extensión sin modificar código existente:
public class NotificadorTelegram implements INotificador {
    @Override
    public void notificar(String mensaje, Paciente paciente) {
        // Nueva implementación
    }
}
```

**Gestor de Notificaciones** - Cerrado para modificación:
```java
public class GestorNotificaciones {
    private INotificador notificador;
    
    public GestorNotificaciones(INotificador notificador) {
        this.notificador = notificador;
    }
    
    public void notificarAgendamiento(Turno turno) {
        String mensaje = "Su turno ha sido agendado";
        notificador.notificar(mensaje, turno.getPaciente());
    }
}
```

**Uso**:
```java
// Email
INotificador notificador = new NotificadorEmail();
GestorNotificaciones gestor = new GestorNotificaciones(notificador);
gestor.notificarAgendamiento(turno);

// Cambiar a SMS sin modificar GestorNotificaciones
notificador = new NotificadorSMS();
gestor = new GestorNotificaciones(notificador);
```

### Solución para Tipos de Turnos:

**Clase abstracta/Interfaz**:
```java
public interface ITurno {
    LocalDateTime getHorario();
    Paciente getPaciente();
    Especialista getEspecialista();
    void cancelar();
}
```

**Implementaciones**:
```java
public class TurnoPresencial implements ITurno {
    // Implementación específica para presencial
}

public class TurnoTelemedicina implements ITurno {
    // Implementación específica para telemedicina
}

public class TurnoUrgencia implements ITurno {
    // Implementación específica para urgencia
}
```

### Solución para Persistencia (Repository Pattern):

**Interfaz Repository** - Abierta para extensión:
```java
public interface IRepositorioTurnos {
    void guardar(Turno turno);
    Turno obtener(long id);
    List<Turno> obtenerTodos();
    void actualizar(Turno turno);
    void eliminar(long id);
}
```

**Implementaciones**:
```java
public class RepositorioTurnosSQL implements IRepositorioTurnos {
    // Implementación con SQL/JDBC
}

public class RepositorioTurnosNoSQL implements IRepositorioTurnos {
    // Implementación con MongoDB/Firebase
}

public class RepositorioTurnosAPI implements IRepositorioTurnos {
    // Implementación con API externa
}
```

## 5. Beneficios de Aplicar OCP

1. **Menos modificaciones**: agregar funcionalidad no requiere cambiar código existente
2. **Menos riesgo**: cambios localizados en nuevas clases, no en código probado
3. **Mayor modularidad**: componentes independientes y reutilizables
4. **Código más limpio**: evita condicionales complejos (if-else, switch)
5. **Facilita testing**: nuevas implementaciones se prueban de forma aislada

## 6. Patrones de Diseño que Implementan OCP

- **Strategy**: seleccionar algoritmo en runtime
- **Decorator**: añadir funcionalidad dinámicamente
- **Factory**: crear objetos sin especificar clases concretas
- **Observer**: notificaciones desacopladas
- **Template Method**: define estructura, subclases implementan pasos

## 7. Resumen

El Principio Abierto/Cerrado guía el diseño hacia sistemas extensibles. En el Sistema de Turnos Médicos, usar interfaces para notificadores, tipos de turnos y persistencia permite que nuevas funcionalidades se añadan sin modificar código existente, resultando en un sistema más robusto y mantenible.
