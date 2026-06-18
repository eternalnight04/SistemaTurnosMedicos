# Caso de Uso 05 - Reprogramar Turno


## Descripción

Este caso de uso permite modificar la fecha y horario de un turno existente.
El paciente solicita el cambio y la secretaria verifica disponibilidad antes
de confirmar la nueva programación.


## Trazabilidad con Requisitos Funcionales A1

| Identificador | Requisito |
|---|---|
| RF-07 | El sistema debe permitir solicitar una reprogramación. |
| RF-08 | El sistema debe verificar disponibilidad del médico. |
| RF-09 | El sistema debe actualizar el turno seleccionado. |
| RF-10 | El sistema debe registrar el historial de cambios. |


# Diagrama de Casos de Uso

![Caso de uso Reprogramar Turno](../../diagramas/02-casos-de-uso/02-caso-uso-reprogramar-turno.png)


El diagrama muestra la interacción entre paciente, secretaria y sistema.


# Diagrama de Actividades

![Actividad Reprogramar Turno](../../diagramas/04-diagramas-actividades/05-actividad-reprogramar-turno.png)


Representa la validación del turno y la búsqueda de un nuevo horario disponible.


# Diagrama de Secuencia

![Secuencia Reprogramar Turno](../../diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-02.png)


Representa las llamadas entre Paciente, Secretaria, Agenda, Turno y Médico.


# Diagrama de Clases

![Clases Reprogramar Turno](../../diagramas/01-diagrama-clases/05-clases-reprogramar-turno.png)


Las clases utilizadas permiten gestionar la búsqueda, validación y actualización
del turno.
