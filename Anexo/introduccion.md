## Casos de uso

### 1. Crear Turno
**Actor(es) involucrado(s):** Secretaria  
**Descripción breve:** La secretaria agenda un nuevo turno para un paciente con un profesional en un horario disponible.

**Flujo principal de eventos:**
1. La secretaria selecciona el profesional y consulta su agenda.
2. El sistema muestra los horarios disponibles.
3. La secretaria ingresa los datos del paciente y el tipo de consulta.
4. El sistema valida que no haya conflicto y calcula la duración.
5. La secretaria confirma y el sistema crea el turno y programa notificación.

**Precondiciones:** Secretaria autenticada y profesional con agenda definida.  
**Postcondiciones:** Turno creado en estado "Programado" y notificación enviada.

### 2. Reprogramar Turno
**Actor(es) involucrado(s):** Secretaria  
**Descripción breve:** La secretaria mueve un turno existente a otro horario disponible.

**Flujo principal de eventos:**
1. La secretaria busca el turno por paciente o fecha.
2. El sistema muestra el turno actual.
3. La secretaria selecciona nuevo horario disponible.
4. El sistema valida y libera el horario anterior.
5. La secretaria confirma y el sistema actualiza el turno con notificación.

**Precondiciones:** Turno existe y no está atendido.  
**Postcondiciones:** Turno actualizado y notificación enviada.

### 3. Cancelar Turno
**Actor(es) involucrado(s):** Secretaria  
**Descripción breve:** La secretaria cancela un turno y libera el horario.

**Flujo principal de eventos:**
1. La secretaria busca el turno.
2. El sistema muestra detalles.
3. La secretaria selecciona motivo y confirma.
4. El sistema marca el turno como "Cancelado" y libera el horario.
5. El sistema registra el cambio y envía notificación.

**Precondiciones:** Turno no está atendido.  
**Postcondiciones:** Horario liberado y notificación enviada.

### 4. Visualizar Agenda
**Actor(es) involucrado(s):** Secretaria  
**Descripción breve:** La secretaria ve la agenda de un profesional por día o semana.

**Flujo principal de eventos:**
1. La secretaria selecciona profesional y rango (día/semana).
2. El sistema muestra todos los turnos y horarios bloqueados.
3. La secretaria filtra por estado.
4. El sistema resalta sobreturnos o conflictos.
5. La secretaria puede ver detalle de cualquier turno.

**Precondiciones:** Secretaria autenticada.  
**Postcondiciones:** Agenda visualizada correctamente.

### 5. Registrar Llegada de Paciente (Check-in)
**Actor(es) involucrado(s):** Secretaria  
**Descripción breve:** La secretaria marca que el paciente llegó al consultorio.

**Flujo principal de eventos:**
1. La secretaria busca el turno del paciente.
2. El sistema muestra el turno programado.
3. La secretaria registra la hora real de llegada.
4. El sistema cambia el estado a "Presente / En sala de espera".
5. El sistema actualiza la agenda y registra el evento.

**Precondiciones:** Turno existe y está programado.  
**Postcondiciones:** Turno en estado "Presente" y historial actualizado.