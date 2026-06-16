# Issues detectados al unificar artefactos

1. Clases referenciadas en CRC pero no listadas inicialmente: `UsuarioDelSistema` aparece como superclase en tarjetas CRC (Paciente/Medico/Secretaria). No estaba en la lista original proporcionada.
2. Inconsistencia de responsabilidades/creación de `Turno`: en algunos diagramas la `Secretaria` crea el turno, en otros `Agenda` ejecuta `crearTurno` directamente.
3. Estados de `Turno` incompletos en tarjetas CRC: CRC lista (pendiente, confirmado, cancelado, realizado) pero los diagramas usan `reprogramado` y `presente` también.
4. Nombres de atributos inconsistentes: `horaLlegada` vs `horaReal` vs `horaRealLlegada` (usado en diferentes artefactos).
5. Clase `LlegadaPaciente`: está modelada en tarjetas CRC pero en secuencias la llegada se registra vía `Turno.registrarLlegada` (solapamiento funcional).
6. Multiplicidad/propiedad de `Agenda`: no hay definición clara si hay una `Agenda` por `Medico` (se asume 1:1 en secuencias), falta especificación en CRC.
7. Historial: los diagramas llaman a `registrarEnHistorial` pero no hay entidad/estructura definida para registros; se usa textualmente sin modelo de datos.
8. Métodos con firmas diferentes: `solicitarTurno`, `crearTurno`, `agendarTurno` se usan indistintamente; conviene normalizar nombres y responsabilidades en la API.
9. Flujo de autorización de sobreturno: el diagrama de secuencia indica interacción `solicitarAutorizacion(solicitudId, ...)` pero no hay un objeto Solicitud ni identificador consistente en CRC.

Recomendaciones rápidas:
- Normalizar nombres de métodos públicos (`agendarTurno` o `crearTurno`) y documentar su contrato.
- Definir `UsuarioDelSistema` como superclase (abstracta) claramente en el modelo y en las tarjetas CRC.
- Elegir un único lugar responsable de crear/guardar `Turno` (recomiendo `Agenda` como fuente de verdad, invocada por `Secretaria`).
- Unificar el tipo y nombre para `horaRealLlegada` y representar `LlegadaPaciente` como un objeto de valor o como atributos de `Turno` (preferible última opción para simplicidad).
- Definir estructura para `RegistroHistorial` si se requiere auditoría detallada.
