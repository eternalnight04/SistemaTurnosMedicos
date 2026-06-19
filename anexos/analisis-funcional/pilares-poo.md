# Pilares de la Programación Orientada a Objetos (POO) aplicados a SistemaTurnosMedicos

## Encapsulamiento
- Definición: Ocultar el estado interno de los objetos y exponer operaciones controladas (métodos) para interactuar.
- Ejemplo 1: `Turno` mantiene `horaRealLlegada` privado y expone `registrarLlegada(horaReal)` para validar y actualizar el estado.
  
	![](../../diagramas/01-diagrama-clases/capturas-pilares/poo-encapsulamiento-ejemplo-1.png)
- Ejemplo 2: `UsuarioDelSistema` tiene `contrasena` privada y método `autenticar(password)` para comprobar credenciales.

	![](../../diagramas/01-diagrama-clases/capturas-pilares/poo-encapsulamiento-ejemplo-2.png)

## Herencia
- Definición: Reutilizar comportamiento creando jerarquías de clases (superclase/subclase).
- Ejemplo 1: `Paciente`, `Medico` y `Secretaria` extienden `UsuarioDelSistema` y comparten `autenticar()` y atributos comunes.

	![](../../diagramas/01-diagrama-clases/capturas-pilares/poo-herencia-ejemplo-1.png)
- Ejemplo 2: Si más adelante hay `Administrador`, puede extender `UsuarioDelSistema` para añadir permisos administrativos.

	![](../../diagramas/01-diagrama-clases/capturas-pilares/poo-herencia-ejemplo-2.png)

## Polimorfismo
- Definición: Tratar objetos de distintas clases derivadas como instancias de la superclase y ejecutar métodos sobre ellas.
- Ejemplo 1: Un método `notificarUsuario(u: UsuarioDelSistema, mensaje)` puede enviar notificaciones a `Paciente` o `Medico`.

	![](../../diagramas/01-diagrama-clases/capturas-pilares/poo-polimorfismo-ejemplo-1.png)
- Ejemplo 2: `consultarAgenda(secretaria: UsuarioDelSistema)` puede aceptar distintos tipos de usuario que implementen la interfaz/contrato necesario.

	![](../../diagramas/01-diagrama-clases/capturas-pilares/poo-polimorfismo-ejemplo-2.png)

## Abstracción
- Definición: Modelar entidades centradas en lo esencial, ocultando detalles irrelevantes para el nivel de diseño.
- Ejemplo 1: `Agenda` ofrece `verificarDisponibilidad(...)` sin exponer la estructura interna de horarios.

	![](../../diagramas/01-diagrama-clases/capturas-pilares/poo-abstraccion-ejemplo-1.png)
- Ejemplo 2: `Turno` presenta `cambiarEstado(...)` en vez de forzar cambios directos en atributos internos.

	![](../../diagramas/01-diagrama-clases/capturas-pilares/poo-abstraccion-ejemplo-2.png)

Cada pilar se ejemplifica con clases y métodos ya presentes en el repositorio y está alineado con las tarjetas CRC y diagramas de secuencia.
