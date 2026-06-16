# Pilares de la Programación Orientada a Objetos (POO) aplicados a SistemaTurnosMedicos

## Encapsulamiento
- Definición: Ocultar el estado interno de los objetos y exponer operaciones controladas (métodos) para interactuar.
- Ejemplo 1: `Turno` mantiene `horaRealLlegada` privado y expone `registrarLlegada(horaReal)` para validar y actualizar el estado.
- Ejemplo 2: `UsuarioDelSistema` tiene `contrasena` privada y método `autenticar(password)` para comprobar credenciales.

## Herencia
- Definición: Reutilizar comportamiento creando jerarquías de clases (superclase/subclase).
- Ejemplo 1: `Paciente`, `Medico` y `Secretaria` extienden `UsuarioDelSistema` y comparten `autenticar()` y atributos comunes.
- Ejemplo 2: Si más adelante hay `Administrador`, puede extender `UsuarioDelSistema` para añadir permisos administrativos.

## Polimorfismo
- Definición: Tratar objetos de distintas clases derivadas como instancias de la superclase y ejecutar métodos sobre ellas.
- Ejemplo 1: Un método `notificarUsuario(u: UsuarioDelSistema, mensaje)` puede enviar notificaciones a `Paciente` o `Medico`.
- Ejemplo 2: `consultarAgenda(secretaria: UsuarioDelSistema)` puede aceptar distintos tipos de usuario que implementen la interfaz/contrato necesario.

## Abstracción
- Definición: Modelar entidades centradas en lo esencial, ocultando detalles irrelevantes para el nivel de diseño.
- Ejemplo 1: `Agenda` ofrece `verificarDisponibilidad(...)` sin exponer la estructura interna de horarios.
- Ejemplo 2: `Turno` presenta `cambiarEstado(...)` en vez de forzar cambios directos en atributos internos.

Cada pilar se ejemplifica con clases y métodos ya presentes en el repositorio y está alineado con las tarjetas CRC y diagramas de secuencia.