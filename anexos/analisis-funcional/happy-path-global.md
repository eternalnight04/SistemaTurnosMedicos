# Happy Path Global - Sistema de Turnos Médicos

## 1. Descripción del Escenario

El siguiente pseudocódigo describe un flujo completo de uso ("Happy Path") que atraviesa la mayor cantidad de clases del sistema. El escenario simula la interacción de una Secretaria dando de alta un turno, un Paciente confirmando su asistencia, y un Médico realizando la atención, finalizando con el registro de la llegada.

**Actores Involucrados:** Secretaria, Paciente, Médico, Sistema.

**Casos de Uso Abarcados:**
- CU01 - Crear Turno
- CU02 - Reprogramar Turno
- CU04 - Autorizar Sobreturno
- CU05 - Registrar Llegada

---

## 2. Pseudocódigo del Happy Path

```text
INICIO DEL SISTEMA

// 1. AUTENTICACIÓN DE LA SECRETARIA
// El sistema inicia y la secretaria ingresa sus credenciales
CREAR objeto Secretaria con credenciales (usuario: "SEC-001", password: "1234")
RESULTADO = Secretaria.autenticar("1234")

SI (RESULTADO == VERDADERO) ENTONCES
   ESCRIBIR "Acceso concedido a la Secretaria Laura"

   // 2. CREACIÓN DE TURNO (CU01)
   // La secretaria registra un nuevo turno para un paciente
   CREAR objeto Paciente (dni: "30123456", nombre: "Juan García")
   CREAR objeto Medico (matricula: "MP12345", especialidad: "Cardiología")
   
   // La Secretaria coordina la búsqueda de disponibilidad en la Agenda
   AGENDA = Sistema.obtenerAgenda()
   DISPONIBLE = AGENDA.verificarDisponibilidad(Medico, Fecha: "2026-06-30", Hora: "10:00")

   SI (DISPONIBLE == VERDADERO) ENTONCES
      // La Agenda es responsable de crear el Turno
      NUEVO_TURNO = AGENDA.crearTurno(FechaHora: "2026-06-30 10:00", Paciente, Medico, Sobreturno: FALSO)
      NUEVO_TURNO.cambiarEstado(ESTADO: "PENDIENTE")
      
      // Notificación al Paciente
      Paciente.recibirNotificacion(Mensaje: "Su turno ha sido asignado para el 30/06 a las 10:00")

      // 3. CONFIRMACIÓN DEL PACIENTE
      CONFIRMACION = Paciente.confirmarTurno(ID_Turno: NUEVO_TURNO.id)
      
      SI (CONFIRMACION == VERDADERO) ENTONCES
         NUEVO_TURNO.cambiarEstado(ESTADO: "CONFIRMADO")
         AGENDA.registrarEnHistorial(Turno: NUEVO_TURNO, Accion: "Turno confirmado por el paciente")
         ESCRIBIR "Turno confirmado exitosamente"
      FIN SI

      // 4. REPROGRAMACIÓN DEL TURNO (CU02) - Escenario alternativo
      // El paciente solicita cambiar el horario
      DISPONIBLE_NUEVO = AGENDA.verificarDisponibilidad(Medico, Fecha: "2026-06-30", Hora: "14:00")
      
      SI (DISPONIBLE_NUEVO == FALSO) ENTONCES
         // Buscar horarios alternativos
         ALTERNATIVAS = AGENDA.sugerirHorariosAlternativos(Medico, Fecha: "2026-06-30")
         NUEVA_FECHA = ALTERNATIVAS[0]
      SINO
         NUEVA_FECHA = "2026-06-30 14:00"
      FIN SI

      // Reprogramar el turno
      REPROGRAMADO = NUEVO_TURNO.reprogramar(NuevaFechaHora: NUEVA_FECHA)
      
      SI (REPROGRAMADO == VERDADERO) ENTONCES
         NUEVO_TURNO.cambiarEstado(ESTADO: "REPROGRAMADO")
         AGENDA.registrarEnHistorial(Turno: NUEVO_TURNO, Accion: "Turno reprogramado al " + NUEVA_FECHA)
         Paciente.recibirNotificacion(Mensaje: "Su turno fue reprogramado para las " + NUEVA_FECHA)
         ESCRIBIR "Turno reprogramado exitosamente"
      FIN SI

      // 5. REGISTRO DE LLEGADA DEL PACIENTE (CU05)
      // El día del turno, el paciente llega al consultorio
      Paciente.llegar(HoraReal: "2026-06-30 13:50")
      NUEVO_TURNO.registrarLlegada(HoraReal: "2026-06-30 13:50")
      
      // El sistema calcula automáticamente si llegó a tiempo
      SI (NUEVO_TURNO.presente == VERDADERO) ENTONCES
         NUEVO_TURNO.cambiarEstado(ESTADO: "PRESENTE")
         ESCRIBIR "Paciente presente. Diferencia: " + NUEVO_TURNO.diferenciaMinutos + " minutos"
      SINO
         ESCRIBIR "Paciente ausente o llegó tarde"
      FIN SI

      // 6. ATENCIÓN MÉDICA
      // El médico consulta su agenda del día
      AGENDA_DIARIA = Medico.consultarAgenda(Fecha: "2026-06-30")

      // El médico atiende al paciente y registra observaciones
      Medico.registrarObservacion(Turno: NUEVO_TURNO, Observacion: "Paciente presenta presión arterial normal. Se mantiene tratamiento.")

      // 7. FINALIZACIÓN DEL TURNO
      NUEVO_TURNO.cambiarEstado(ESTADO: "REALIZADO")
      AGENDA.registrarEnHistorial(Turno: NUEVO_TURNO, Accion: "Atención médica completada")
      
      ESCRIBIR "Ciclo del turno finalizado exitosamente. Turno " + NUEVO_TURNO.id + " marcado como REALIZADO"

   SINO
      ESCRIBIR "No hay disponibilidad horaria para el médico seleccionado"
   FIN SI

SINO
   ESCRIBIR "Error de autenticación. Credenciales inválidas"
FIN SI

// 8. AUTORIZACIÓN DE SOBRETURNO (CU04) - Escenario alternativo
// Llega un paciente con urgencia y se necesita un sobreturno
CREAR objeto PacienteUrgencia (dni: "31987654", nombre: "María López")

// El médico debe autorizar el sobreturno
AUTORIZADO = Medico.autorizarSobreturno(SolicitudId: "SOL-001")

SI (AUTORIZADO == VERDADERO) ENTONCES
   SOBRETURNO = AGENDA.crearTurno(FechaHora: "2026-06-30 15:00", PacienteUrgencia, Medico, Sobreturno: VERDADERO)
   SOBRETURNO.cambiarEstado(ESTADO: "CONFIRMADO")
   ESCRIBIR "Sobreturno autorizado y creado: " + SOBRETURNO.id
SINO
   ESCRIBIR "El médico no autorizó el sobreturno"
FIN SI

FIN DEL SISTEMA
```

---

## 3. Tabla de Trazabilidad

| Paso del Flujo | Clase Involucrada | Método Invocado | Origen (CRC/Diagrama/CU) |
|----------------|-------------------|-----------------|--------------------------|
| 1. Autenticación | `Secretaria` (hereda de `UsuarioDelSistema`) | `autenticar(password)` | CRC UsuarioDelSistema |
| 2. Verificar disponibilidad | `Agenda` | `verificarDisponibilidad(medicoId, fecha, hora)` | CRC Agenda / CU01 |
| 2. Crear Turno | `Agenda` | `crearTurno(fechaHora, paciente, medico, sobreturno)` | CRC Agenda / CU01 |
| 2. Cambiar estado | `Turno` | `cambiarEstado(nuevoEstado)` | CRC Turno / CU01 |
| 2. Notificar | `Paciente` | `recibirNotificacion(mensaje)` | CRC Paciente / CU01 |
| 3. Confirmar Turno | `Paciente` | `confirmarTurno(turnoId)` | CRC Paciente / CU01 |
| 4. Reprogramar | `Turno` | `reprogramar(nuevaFechaHora)` | CRC Turno / CU02 |
| 4. Sugerir alternativas | `Agenda` | `sugerirHorariosAlternativos(medicoId, fecha)` | CRC Agenda / CU02 |
| 5. Registrar llegada | `Turno` | `registrarLlegada(horaReal)` | CRC Turno / CU05 |
| 6. Consultar agenda | `Medico` | `consultarAgenda(fecha)` | CRC Medico |
| 6. Registrar observación | `Medico` | `registrarObservacion(turnoId, observacion)` | CRC Medico |
| 7. Finalizar turno | `Turno` | `cambiarEstado(REALIZADO)` | Enum TurnoEstado |
| 8. Autorizar sobreturno | `Medico` | `autorizarSobreturno(solicitudId)` | CRC Medico / CU04 |
