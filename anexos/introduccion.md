# Introducción

---

## Descripción del Paradigma Orientado a Objetos

El paradigma orientado a objetos (POO) es un modelo de programación basado en la representación de entidades del mundo real mediante objetos. Un objeto combina datos (atributos) y comportamientos (métodos) dentro de una misma estructura.

Este paradigma permite organizar sistemas complejos de forma modular, facilitando la reutilización, el mantenimiento y la escalabilidad del software.

En el sistema de turnos médicos, entidades como Paciente, Médico o Turno pueden representarse como clases con atributos y comportamientos propios.

---

## Los Cuatro Fundamentos de la Programación Orientada a Objetos

### 1. Abstracción

Consiste en representar solo las características esenciales de un objeto, ocultando detalles innecesarios.

Ejemplo: La clase Turno puede contener fecha, hora y estado, sin modelar detalles irrelevantes.

---

### 2. Encapsulamiento

Implica proteger los datos internos de un objeto y permitir el acceso mediante métodos definidos.

Ejemplo: El historial médico de un paciente podría ser un atributo privado accesible mediante métodos controlados.

---

### 3. Herencia

Permite que una clase derive de otra, heredando atributos y comportamientos.

Ejemplo: Una clase Persona podría ser base de Médico y Paciente.

---

### 4. Polimorfismo

Permite que distintos objetos respondan de forma diferente ante el mismo método.

Ejemplo: La forma de calcular el costo de una consulta puede variar según si es un control médico o una primera consulta. El sistema invoca la misma operación "calcular costo", pero el resultado difiere según el tipo de consulta, sin que el resto del sistema necesite conocer esa diferencia.

---

## Requisitos Iniciales del Sistema

🔗 [Cuaderno grupal en NotebookLM](https://notebooklm.google.com/notebook/ae349fb5-874b-428f-9bb0-5822e5c8be15)

El sistema de turnos médicos tiene como objetivo gestionar la asignación, modificación y cancelación de turnos entre pacientes y profesionales de la salud.

### Requisitos Funcionales (RF)

* RF01: Permitir a los pacientes solicitar turnos médicos.
* RF02: Permitir a los pacientes cancelar o reprogramar turnos.
* RF03: Permitir a los médicos visualizar su agenda de turnos.
* RF04: Registrar información básica de pacientes y médicos.
* RF05: Gestionar la disponibilidad horaria de los profesionales.

### Requisitos No Funcionales (RNF)

* RNF01: El sistema debe garantizar la no-superposición de turnos: un profesional no puede tener dos turnos simultáneamente (restricción crítica del negocio).
* RNF02: Toda modificación de turno debe registrarse con trazabilidad completa: quién realizó el cambio, cuándo y qué datos fueron modificados.
* RNF03: El sistema debe implementar control de acceso diferenciado por rol: Secretaria (gestión de turnos) vs Profesional (visualización de agenda personal).
* RNF04: El sistema debe permitir extensibilidad para agregar nuevos profesionales sin requerer rediseño arquitectónico.
* RNF05: El tiempo de respuesta en operaciones críticas (crear turno, consultar agenda) debe ser ≤ 2 segundos en condiciones normales de carga.

---

## Casos de Uso

### CU-01: Crear Turno

**Actor(es):** Secretaria (principal)

**Descripción:** La secretaria registra un nuevo turno para un paciente con el profesional, verificando disponibilidad y evitando superposiciones.

**Precondiciones:**
- La secretaria está autenticada en el sistema.
- El paciente existe o es dado de alta en el momento.
- El profesional tiene disponibilidad configurada.

**Flujo principal:**
1. La secretaria selecciona "Nuevo Turno".
2. Busca o selecciona al paciente por nombre o identificador.
3. Selecciona profesional, fecha, hora y tipo de consulta (control o primera vez).
4. El sistema verifica que el horario esté dentro de la disponibilidad del profesional.
5. El sistema verifica que no haya otro turno en ese horario.
6. El sistema registra el turno como "Confirmado" con duración estimada (15 min control, 30 min primera vez).
7. El sistema guarda el evento en el historial del turno.
8. El sistema notifica al paciente por WhatsApp o mail.

**Flujos alternativos:**
- FA-01A: Si el horario está fuera de disponibilidad, el sistema informa el conflicto y no registra el turno.
- FA-01B: Si ya existe un turno en ese horario, el sistema advierte la superposición y bloquea el registro. La secretaria puede elegir otro horario o solicitar sobreturno (ver CU-04).
- FA-01C: Si el paciente no existe, la secretaria puede darlo de alta antes de continuar.

**Postcondiciones:**
- El turno queda registrado en la agenda del profesional.
- El paciente recibe notificación de confirmación.
- El historial registra la creación con fecha, hora y usuario.

---

### CU-02: Reprogramar Turno

**Actor(es):** Secretaria (principal), Paciente (secundario)

**Descripción:** La secretaria modifica la fecha u hora de un turno existente, valida el nuevo horario y notifica al paciente.

**Precondiciones:**
- La secretaria está autenticada.
- El turno existe y no está cancelado ni atendido.
- El nuevo horario es una fecha futura.

**Flujo principal:**
1. La secretaria busca y selecciona el turno a reprogramar.
2. Selecciona la nueva fecha y/u hora.
3. El sistema verifica que el nuevo horario esté dentro de la disponibilidad del profesional.
4. El sistema verifica que no haya superposición con otro turno.
5. El sistema actualiza el turno con el nuevo horario, manteniendo el tipo de consulta original.
6. El sistema registra en el historial el horario anterior, el nuevo horario, fecha del cambio y usuario.
7. El sistema notifica al paciente el nuevo horario.

**Flujos alternativos:**
- FA-02A: Si el nuevo horario está ocupado, el sistema informa el conflicto y no realiza el cambio.
- FA-02B: Si el turno está cancelado o atendido, el sistema informa que no es posible reprogramarlo.
- FA-02C: Si falla la notificación, el turno se reprograma igual y queda registrado para notificación manual.

**Postcondiciones:**
- El turno queda con el nuevo horario en la agenda.
- El historial refleja la reprogramación con trazabilidad completa.
- El paciente es notificado.

---

### CU-03: Cancelar Turno

**Actor(es):** Secretaria (principal), Paciente (secundario)

**Descripción:** La secretaria cancela un turno existente. El sistema libera el horario, actualiza el historial y notifica al paciente.

**Precondiciones:**
- La secretaria está autenticada.
- El turno existe y no está cancelado ni atendido.

**Flujo principal:**
1. La secretaria busca y selecciona el turno a cancelar.
2. Indica el motivo de cancelación (opcional).
3. El sistema solicita confirmación antes de proceder.
4. La secretaria confirma la cancelación.
5. El sistema cambia el estado a "Cancelado" y libera el horario.
6. El sistema registra en el historial la cancelación con fecha, hora y responsable.
7. El sistema notifica al paciente.

**Flujos alternativos:**
- FA-03A: Si el turno ya está cancelado o atendido, el sistema informa que la operación no es válida.
- FA-03B: Si la secretaria no confirma, el sistema descarta la operación y el turno no cambia.
- FA-03C: Si la cancelación es iniciada por el paciente, la secretaria la carga igual registrando "a pedido del paciente".

**Postcondiciones:**
- El turno queda con estado "Cancelado" (no se elimina).
- El horario queda disponible para nuevas reservas.
- El paciente es notificado.

---

### CU-04: Autorizar Sobreturno

**Actor(es):** Profesional / Dr. Molina (principal), Secretaria (secundario)

**Descripción:** El profesional autoriza manualmente agregar un paciente fuera del horario normal o en un horario ocupado. La secretaria solo puede registrarlo con autorización explícita del médico.

**Precondiciones:**
- La secretaria está autenticada.
- El profesional dio su autorización explícita.
- Existe un paciente identificado para el sobreturno.

**Flujo principal:**
1. La secretaria intenta registrar un turno en horario ocupado o fuera de disponibilidad.
2. El sistema detecta el conflicto y advierte sobre la superposición.
3. La secretaria indica que el médico autorizó el sobreturno.
4. El sistema solicita confirmación explícita del sobreturno.
5. La secretaria confirma.
6. El sistema registra el turno con indicador "Sobreturno = verdadero".
7. El sistema guarda en el historial que fue un sobreturno autorizado manualmente.

**Flujos alternativos:**
- FA-04A: Si no hay autorización del médico, la secretaria debe cancelar la operación. El sistema no genera sobreturnos automáticamente.
- FA-04B: Si el médico no está presente y no es urgencia real, el sobreturno no debe registrarse (regla explícita del Dr. Molina: "si no estoy → no debería agregarse").
- FA-04C: Si hay múltiples sobreturnos simultáneos, el sistema muestra advertencia informativa pero no bloquea.

**Postcondiciones:**
- El sobreturno queda registrado con su indicador.
- El historial deja trazabilidad de la decisión manual.
- No se generan sobreturnos automáticos.

---

### CU-05: Registrar Llegada del Paciente

**Actor(es):** Secretaria (principal)

**Descripción:** Cuando el paciente llega físicamente al consultorio, la secretaria registra su presencia. Esto diferencia la planificación del turno de la presencia física real.

**Precondiciones:**
- La secretaria está autenticada.
- Existe un turno activo para el paciente en la fecha actual.
- El paciente se presentó físicamente.

**Flujo principal:**
1. La secretaria accede a la agenda del día.
2. Localiza el turno del paciente que llegó.
3. Selecciona "Registrar llegada".
4. El sistema registra la hora real de llegada.
5. El sistema cambia el estado a "Presente".
6. El sistema registra en el historial la llegada con hora exacta.

**Flujos alternativos:**
- FA-05A: Si el turno no existe o está cancelado, el sistema informa que no puede registrar la llegada.
- FA-05B: Si el paciente llega fuera del horario del turno, el sistema registra igual pero advierte la diferencia horaria.

**Postcondiciones:**
- El turno queda con estado "Presente".
- El historial registra la llegada con timestamp exacto.
- El profesional puede iniciar la atención.

---

## Diagrama de Clases del Sistema

El diagrama de clases del Sistema de Turnos Médicos modela las entidades principales y sus relaciones para garantizar una gestión correcta de turnos con trazabilidad, validación de disponibilidad y notificaciones.

### Entidades Centrales

**Turno** es la entidad nuclear del sistema, que vincula pacientes con profesionales en un horario específico. Contiene:
- Identificación única y rango horario (fecha-hora inicio/fin)
- Estado del turno (Programado, Presente, Cancelado, Atendido)
- Tipo de consulta (Control o Primera consulta) con duración determinada
- Flag de sobreturno para autorización manual
- Método de cancelación con registro de motivo
- Métodos de reprogramación, registro de llegada y auditoria

**Agenda** gestiona los turnos de un profesional específico y controla la disponibilidad:
- Colección de turnos del profesional
- Colección de bloqueos horarios (vacaciones, feriados, reuniones, capacitaciones)
- Métodos para validar disponibilidad, crear/reprogramar/cancelar turnos
- Generación de sobreturnos con autorización explícita

**Profesional** define los datos del médico o especialista:
- Identificación, nombre, apellido, especialidad
- Métodos para definir disponibilidad, bloquear horarios y obtener agenda

**Paciente** contiene información de contacto:
- Identificación, datos personales (nombre, apellido, documento)
- Teléfono y email para notificaciones
- Método para actualizar datos

**Secretaria** representa el usuario administrativo:
- Autenticación (usuario, contraseña)
- Rol para control de acceso
- Métodos de gestión de turnos y visualización de agenda

### Entidades de Soporte

**TipoConsulta** define tipos de consulta con duración específica (control: 15 min, primera vez: 30 min).

**TurnoEstado** es una enumeración de estados posibles: Programado, Presente, Cancelado, Atendido.

**BloqueoHorario** registra períodos no disponibles con motivo y tipo específico.

**BloqueoTipo** enumera: Vacaciones, Feriado, Reunion, Capacitación.

**Notificación** gestiona comunicaciones al paciente:
- Referencia a turno y destinatario
- Medio de envío (Email, WhatsApp)
- Mensaje y estado de envío (enviada/no enviada)

**NotificacionMedio** enumera canales: Email y WhatsApp.

**Auditoria** garantiza trazabilidad completa:
- Referencia a turno, usuario, acción realizada
- Timestamp y detalles de cambios

### Relaciones Clave

- **Paciente ↔ Turno**: Un paciente puede tener múltiples turnos (1 a N)
- **Profesional ↔ Agenda**: Un profesional tiene exactamente una agenda (1 a 1)
- **Agenda ↔ Turno**: Una agenda contiene múltiples turnos (1 a N)
- **Agenda ↔ BloqueoHorario**: Una agenda puede tener múltiples bloqueos (1 a N)
- **Turno ↔ TipoConsulta**: Cada turno está asociado a un tipo específico (N a 1)
- **BloqueoHorario ↔ BloqueoTipo**: Cada bloqueo tiene un tipo específico (N a 1)
- **Turno ↔ Notificación**: Un turno genera una o más notificaciones (1 a N)
- **Notificación ↔ NotificacionMedio**: Cada notificación usa un medio específico (N a 1)
- **Turno ↔ Auditoria**: Un turno registra múltiples cambios en auditoria (1 a N)
- **Turno ↔ TurnoEstado**: Cada turno tiene un estado en cada momento (N a 1)

### Principios de Diseño Garantizados

- **No-superposición de turnos**: Validación de disponibilidad antes de crear turno (RNF01)
- **Trazabilidad completa**: Registro de todas las acciones en Auditoria (RNF02)
- **Control de acceso**: Roles diferenciados (Secretaria vs Profesional vs Profesional) (RNF03)
- **Extensibilidad**: Fácil agregar nuevos profesionales sin rediseño (RNF04)
- **Notificaciones**: Comunicación automática por múltiples canales
- **Sobreturnos**: Generación manual solo con autorización explícita del profesional
