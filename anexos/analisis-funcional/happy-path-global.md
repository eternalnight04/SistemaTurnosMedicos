# Happy Path Global - Sistema de Turnos Médicos

## 1. Descripción del Escenario

Este documento describe el flujo principal del Sistema de Turnos Médicos desde la autenticación de una secretaria hasta la finalización de una consulta médica. El escenario atraviesa la mayor cantidad de clases del sistema y demuestra la colaboración entre los objetos del dominio.

**Actores involucrados:** Secretaria, Paciente, Médico

**Casos de Uso cubiertos:**
- CU01 - Crear Turno
- CU02 - Reprogramar Turno  
- CU04 - Autorizar Sobreturno
- CU05 - Registrar Llegada

**Clases del dominio involucradas:** UsuarioDelSistema, Secretaria, Paciente, Medico, Agenda, Turno

---

## 2. Pseudocódigo del Happy Path

```text
// ========================================
// ESCENARIO: Atención completa de un paciente
// desde el alta del turno hasta la consulta
// ========================================

// PASO 1: Autenticación de la Secretaria
// La secretaria inicia sesión en el sistema
// para poder gestionar turnos
secre = new Secretaria(id: "SEC-001", nombre: "Laura", dni: "12345678")
accesoConcedido = secre.autenticar(password: "miPasswordSegura")

SI accesoConcedido ENTONCES
    // La secretaria ahora puede operar en el sistema
    
    // PASO 2: Alta de un nuevo paciente
    // La secretaria registra a Juan García en el sistema
    datosPaciente = { nombre: "Juan García", dni: "30123456", email: "juan@mail.com" }
    nuevoPaciente = secre.darAltaPaciente(datos: datosPaciente)
    
    // PASO 3: Verificar disponibilidad del médico
    // Antes de crear el turno, se verifica que el Dr. Molina
    // tenga disponibilidad el 30/06 a las 10:00
    medico = new Medico(matricula: "MP12345", especialidad: "Cardiología")
    agenda = new Agenda(id: "AG-001", medico: medico)
    
    hayDisponibilidad = agenda.verificarDisponibilidad(
        medicoId: medico.matricula, 
        fecha: "2026-06-30", 
        hora: "10:00"
    )
    
    SI hayDisponibilidad ENTONCES
        // PASO 4: Crear el turno
        // La Agenda es responsable de instanciar el objeto Turno
        nuevoTurno = agenda.crearTurno(
            fechaHora: "2026-06-30 10:00",
            paciente: nuevoPaciente,
            medico: medico,
            sobreturno: FALSO
        )
        
        // El turno inicia en estado PENDIENTE
        nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.PENDIENTE)
        
        // PASO 5: Notificar al paciente
        // El paciente recibe la notificación del turno asignado
        nuevoPaciente.recibirNotificacion(
            mensaje: "Su turno ha sido asignado para el 30/06 a las 10:00"
        )
        
        // PASO 6: Confirmación del turno por el paciente
        // El paciente confirma su asistencia
        confirmado = nuevoPaciente.confirmarTurno(turnoId: nuevoTurno.id)
        
        SI confirmado ENTONCES
            nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.CONFIRMADO)
            agenda.registrarEnHistorial(
                turnoId: nuevoTurno.id,
                descripcion: "Turno confirmado por el paciente"
            )
        FIN SI
        
        // PASO 7: Reprogramación del turno (CU02)
        // El paciente solicita cambiar el horario a las 14:00
        // Primero se verifica disponibilidad en el nuevo horario
        disponibleNuevoHorario = agenda.verificarDisponibilidad(
            medicoId: medico.matricula,
            fecha: "2026-06-30", 
            hora: "14:00"
        )
        
        SI NO disponibleNuevoHorario ENTONCES
            // Si no hay disponibilidad, sugerir horarios alternativos
            alternativas = agenda.sugerirHorariosAlternativos(
                medicoId: medico.matricula,
                fecha: "2026-06-30"
            )
            nuevaFechaHora = alternativas[0]
        SINO
            nuevaFechaHora = "2026-06-30 14:00"
        FIN SI
        
        // Se reprograma el turno
        nuevoTurno.reprogramar(nuevaFechaHora: nuevaFechaHora)
        nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.REPROGRAMADO)
        
        agenda.registrarEnHistorial(
            turnoId: nuevoTurno.id,
            descripcion: "Turno reprogramado al " + nuevaFechaHora
        )
        
        nuevoPaciente.recibirNotificacion(
            mensaje: "Su turno fue reprogramado para las " + nuevaFechaHora
        )
        
        // PASO 8: Registro de llegada del paciente (CU05)
        // El día de la consulta, el paciente llega al consultorio
        nuevoTurno.registrarLlegada(horaReal: "2026-06-30 13:50")
        
        // El sistema calcula automáticamente si llegó a tiempo
        SI nuevoTurno.presente ENTONCES
            nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.PRESENTE)
        FIN SI
        
        // PASO 9: Atención médica
        // El Dr. Molina consulta su agenda del día
        agendaDiaria = medico.consultarAgenda(fecha: "2026-06-30")
        
        // El médico atiende al paciente y registra observaciones
        medico.registrarObservacion(
            turnoId: nuevoTurno.id,
            observacion: "Paciente presenta presión arterial normal"
        )
        
        // PASO 10: Finalización del turno
        nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.REALIZADO)
        
        agenda.registrarEnHistorial(
            turnoId: nuevoTurno.id,
            descripcion: "Atención médica completada"
        )
        
    SINO
        // No hay disponibilidad para el médico seleccionado
    FIN SI
    
SINO
    // Error de autenticación
FIN SI

// PASO 11: Autorización de sobreturno (CU04)
// Escenario alternativo: llega un paciente con urgencia
pacienteUrgencia = new Paciente(dni: "31987654", nombre: "María López")

// El médico debe autorizar el sobreturno
autorizado = medico.autorizarSobreturno(solicitudId: "SOL-001")

SI autorizado ENTONCES
    sobreturno = agenda.crearTurno(
        fechaHora: "2026-06-30 15:00",
        paciente: pacienteUrgencia,
        medico: medico,
        sobreturno: VERDADERO
    )
    sobreturno.cambiarEstado(nuevoEstado: TurnoEstado.CONFIRMADO)
FIN SI
```

---

## 3. Tabla de Trazabilidad

La siguiente tabla vincula cada paso del pseudocódigo con los artefactos previos (tarjetas CRC y casos de uso) de los cuales surge.

| Paso | Clase | Método | Origen (CRC/Diagrama/CU) |
|------|-------|--------|--------------------------|
| 1. Autenticación | `Secretaria` (hereda de `UsuarioDelSistema`) | `autenticar(password)` | CRC UsuarioDelSistema |
| 2. Alta de paciente | `Secretaria` | `darAltaPaciente(datos)` | CRC Secretaria / CU01 |
| 3. Verificar disponibilidad | `Agenda` | `verificarDisponibilidad(medicoId, fecha, hora)` | CRC Agenda / CU01 |
| 4. Crear turno | `Agenda` | `crearTurno(fechaHora, paciente, medico, sobreturno)` | CRC Agenda / CU01 |
| 4. Cambiar estado | `Turno` | `cambiarEstado(nuevoEstado)` | CRC Turno / CU01 |
| 5. Notificar | `Paciente` | `recibirNotificacion(mensaje)` | CRC Paciente / CU01 |
| 6. Confirmar turno | `Paciente` | `confirmarTurno(turnoId)` | CRC Paciente / CU01 |
| 7. Reprogramar | `Turno` | `reprogramar(nuevaFechaHora)` | CRC Turno / CU02 |
| 7. Sugerir alternativas | `Agenda` | `sugerirHorariosAlternativos(medicoId, fecha)` | CRC Agenda / CU02 |
| 8. Registrar llegada | `Turno` | `registrarLlegada(horaReal)` | CRC Turno / CU05 |
| 9. Consultar agenda | `Medico` | `consultarAgenda(fecha)` | CRC Medico |
| 9. Registrar observación | `Medico` | `registrarObservacion(turnoId, observacion)` | CRC Medico |
| 10. Finalizar turno | `Turno` | `cambiarEstado(TurnoEstado.REALIZADO)` | Enum TurnoEstado |
| 11. Autorizar sobreturno | `Medico` | `autorizarSobreturno(solicitudId)` | CRC Medico / CU04 |
