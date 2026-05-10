# Principio de Sustitución de Liskov (LSP)

## 1. Qué es el Principio de Sustitución de Liskov

El Principio de Sustitución de Liskov (LSP - Liskov Substitution Principle) establece que **los objetos de clases derivadas deben poder reemplazar a los objetos de la clase base sin alterar las propiedades deseables del programa**.

En otras palabras: **si S es un subtipo de T, entonces los objetos de tipo T pueden ser reemplazados por objetos de tipo S sin que el programa pierda las propiedades correctas que se esperan de T**.

Esto asegura que:
- Las subclases respeten el contrato de la clase base
- El comportamiento sea predecible y consistente
- El polimorfismo funcione correctamente

## 2. Problema de Violar LSP

Una violación clásica es el ejemplo del Rectángulo y Cuadrado:

```java
// ❌ VIOLA LSP
class Rectangulo {
    protected int ancho;
    protected int alto;
    
    public void setAncho(int ancho) {
        this.ancho = ancho;
    }
    
    public void setAlto(int alto) {
        this.alto = alto;
    }
    
    public int getArea() {
        return ancho * alto;
    }
}

class Cuadrado extends Rectangulo {
    @Override
    public void setAncho(int lado) {
        this.ancho = lado;
        this.alto = lado;  // Fuerza que sean iguales
    }
    
    @Override
    public void setAlto(int lado) {
        this.ancho = lado;
        this.alto = lado;  // Fuerza que sean iguales
    }
}

// Uso que viola LSP:
public void procesarRectangulo(Rectangulo r) {
    r.setAncho(5);
    r.setAlto(10);
    assert r.getArea() == 50;  // ❌ Falla si r es un Cuadrado (área sería 100)
}
```

**Problema**: No podemos sustituir `Rectangulo` por `Cuadrado` sin que el programa se comporte diferente.

## 3. Análisis de Jerarquías en Sistema de Turnos

En el Sistema de Turnos Médicos, tenemos varias jerarquías que deben respetar LSP:

### Jerarquía de Turnos
- **Turno** (base)
  - TurnoPresencial
  - TurnoTelemedicina
  - TurnoUrgencia
  - TurnoDomiciliario

Cada subtipo debe cumplir el contrato de `Turno`:
- Tener horario válido
- Tener paciente y especialista
- Poder cancelarse bajo ciertas condiciones
- Poder cambiar de estado

### Jerarquía de Especialistas
- **Especialista** (base)
  - EspecialistaPresencial
  - EspecialistaTelemedico
  - EspecialistaHibrido

### Jerarquía de Notificadores
- **INotificador** (interfaz)
  - NotificadorEmail
  - NotificadorSMS
  - NotificadorWhatsApp

## 4. Aplicación de LSP al Sistema

### Jerarquía Correcta de Turnos:

```java
// Contrato base que TODOS los turnos deben cumplir
public interface ITurno {
    LocalDateTime getHorario();
    Paciente getPaciente();
    Especialista getEspecialista();
    void cambiarEstado(EstadoTurno nuevoEstado);
    boolean puedeCancelarse();
    void cancelar() throws TurnoNoCancelableException;
}

// Implementación base con lógica común
public abstract class Turno implements ITurno {
    protected Paciente paciente;
    protected Especialista especialista;
    protected LocalDateTime horario;
    protected EstadoTurno estado;
    
    @Override
    public LocalDateTime getHorario() {
        return horario;
    }
    
    @Override
    public Paciente getPaciente() {
        return paciente;
    }
    
    @Override
    public Especialista getEspecialista() {
        return especialista;
    }
    
    @Override
    public void cambiarEstado(EstadoTurno nuevoEstado) {
        this.estado = nuevoEstado;
    }
    
    // Subclases pueden override pero respetando contrato
    @Override
    public abstract boolean puedeCancelarse();
    
    @Override
    public void cancelar() throws TurnoNoCancelableException {
        if (!puedeCancelarse()) {
            throw new TurnoNoCancelableException("Este turno no puede cancelarse");
        }
        cambiarEstado(EstadoTurno.CANCELADO);
    }
}

// TurnoPresencial respeta el contrato
public class TurnoPresencial extends Turno {
    @Override
    public boolean puedeCancelarse() {
        // Un turno presencial puede cancelarse si está más de 24h en el futuro
        LocalDateTime limite = horario.minusHours(24);
        return LocalDateTime.now().isBefore(limite);
    }
}

// TurnoTelemedicina respeta el contrato (pero con otra lógica)
public class TurnoTelemedicina extends Turno {
    @Override
    public boolean puedeCancelarse() {
        // Un turno telemedicina puede cancelarse si está más de 1h en el futuro
        LocalDateTime limite = horario.minusHours(1);
        return LocalDateTime.now().isBefore(limite);
    }
}

// TurnoUrgencia respeta el contrato (pero diferente)
public class TurnoUrgencia extends Turno {
    @Override
    public boolean puedeCancelarse() {
        // Un turno de urgencia NO se puede cancelar una vez creado
        return false;
    }
}
```

### Uso que respeta LSP:

```java
public void procesarCancelacion(Turno turno) {
    try {
        // Funciona con CUALQUIER tipo de turno
        // porque todos respetan el contrato
        turno.cancelar();
        System.out.println("Turno cancelado exitosamente");
    } catch (TurnoNoCancelableException e) {
        System.out.println("No se puede cancelar: " + e.getMessage());
    }
}

// Uso polimórfico correcto:
List<Turno> turnos = new ArrayList<>();
turnos.add(new TurnoPresencial(...));
turnos.add(new TurnoTelemedicina(...));
turnos.add(new TurnoUrgencia(...));

for (Turno turno : turnos) {
    procesarCancelacion(turno);  // ✓ Funciona correctamente para todos
}
```

### Jerarquía de Especialistas:

```java
public interface IEspecialista {
    String getNombre();
    String getEspecialidad();
    List<ITurno> getTurnosAsignados();
    boolean estaDisponible(LocalDateTime horario);
}

// Clase base
public abstract class Especialista implements IEspecialista {
    protected String nombre;
    protected String especialidad;
    protected List<ITurno> turnosAsignados;
    
    @Override
    public String getNombre() { return nombre; }
    
    @Override
    public String getEspecialidad() { return especialidad; }
    
    @Override
    public List<ITurno> getTurnosAsignados() { return turnosAsignados; }
    
    // Subclases deben respetar el contrato de estaDisponible
    @Override
    public abstract boolean estaDisponible(LocalDateTime horario);
}

public class EspecialistaPresencial extends Especialista {
    private List<LocalDateTime> holariosConsultorio;
    
    @Override
    public boolean estaDisponible(LocalDateTime horario) {
        // Disponible si tiene horario en el consultorio y no hay turno
        return holariosConsultorio.contains(horario) &&
               turnosAsignados.stream().noneMatch(t -> t.getHorario().equals(horario));
    }
}

public class EspecialistaTelemedico extends Especialista {
    private boolean conectado;
    
    @Override
    public boolean estaDisponible(LocalDateTime horario) {
        // Disponible si está conectado y no hay turno
        return conectado &&
               turnosAsignados.stream().noneMatch(t -> t.getHorario().equals(horario));
    }
}
```

## 5. Cómo Identificar Violaciones de LSP

Pregúntate:

- ¿Necesito usar `instanceof` para comprobar el tipo real?
- ¿Una subclase lanza excepciones que la clase base no?
- ¿Una subclase restringe más que la clase base (precondiciones más fuertes)?
- ¿Una subclase promete menos que la clase base (postcondiciones más débiles)?
- ¿El comportamiento cambia de forma inesperada al usar subclases?

Si respondes "sí" a alguna, probablemente violes LSP.

## 6. Beneficios de Aplicar LSP

1. **Polimorfismo predecible**: subclases se comportan como se espera
2. **Menos sorpresas**: cambiar tipos de objetos no causa fallos ocultos
3. **Código más robusto**: se puede confiar en el contrato
4. **Mantenimiento más fácil**: subclases extienden sin sorpresas
5. **Mejor reutilización**: componentes funcionan con cualquier subtipo

## 7. Relación con Otros Principios SOLID

- **OCP**: LSP asegura que las extensiones (subclases) respeten el contrato
- **DIP**: LSP facilita la inversión de dependencias mediante interfaces
- **SRP**: cada subtipo tiene una responsabilidad clara
- **ISP**: cada interfaz es específica y respetada completamente

## 8. Resumen

El Principio de Sustitución de Liskov garantiza que las jerarquías de clases en el Sistema de Turnos Médicos sean predecibles y reutilizables. Respetar el contrato en todas las subclases significa que el código cliente puede trabajar polimórficamente sin sorpresas, resultando en un sistema más robusto y mantenible.
