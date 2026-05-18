# Especialista en Diagramas de Secuencias - Documentación Copilot

## Prompt utilizado

```
Genera 5 diagramas de secuencia en PlantUML, cada uno correspondiente a los escenarios de casos de uso definidos en la carpeta:
diagramas/03-escenarios-casos-de-uso/

Requisitos obligatorios:
Cada diagrama debe representar un escenario distinto.
Utilizar PlantUML con sintaxis correcta y profesional.
Cada diagrama debe incluir:
Al menos 4 participantes.
Mínimo 3 mensajes entre participantes.
Aplicar correctamente la notación UML:
Clase
:objeto
Clase:objeto
Usar naming en camelCase para métodos y mensajes.
Indicar en cada mensaje si el método recibe argumentos (si corresponde).
Representar correctamente la creación y destrucción de objetos:
Marcar la destrucción con una X al final de la línea de vida (destroy en PlantUML).
Contexto obligatorio (MUY IMPORTANTE):
Para cada diagrama, debés:
Referenciar explícitamente el escenario correspondiente ubicado en:
diagramas/03-escenarios-casos-de-uso/
Referenciar las tarjetas CRC de las clases involucradas en:
herramientas-agile/tarjetas-crc/
Usar esos archivos como fuente de verdad para identificar:
Responsabilidades de cada clase
Colaboraciones entre objetos
Formato de salida:

Generar los 5 diagramas separados, cada uno con su bloque:

@startuml
...
@enduml
Agregar un comentario al inicio de cada diagrama indicando:
Nombre del escenario
Archivo de donde se obtuvo
Objetivo:

Obtener diagramas consistentes con los escenarios y alineados con las responsabilidades definidas en las tarjetas CRC, respetando buenas prácticas de UML.

```

## Archivos de contexto

- diagramas/03-escenarios-casos-de-uso/03-autorizar-sobreturno-flujo-principal.md
- diagramas/03-escenarios-casos-de-uso/03-cancelar-turno-flujo-principal.md
- diagramas/03-escenarios-casos-de-uso/03-crear-turno-flujo-principal.md
- diagramas/03-escenarios-casos-de-uso/03-registrar-llegada-flujo-principal.md
- diagramas/03-escenarios-casos-de-uso/03-reprogramar-turno-flujo-alterno.md
- herramientas-agile/tarjetas-crc/02-tarjeta-crc-medico.md
- herramientas-agile/tarjetas-crc/03-tarjeta-crc-turno.md
- herramientas-agile/tarjetas-crc/04-tarjeta-crc-agenda.md
- herramientas-agile/tarjetas-crc/05-tarjeta-crc-secretaria.md
- ia/ herramientas-agile/tarjetas-crc/01-tarjeta-crc-paciente.md

## Ajustes realizados

- Se crearon 5 archivos PUMl separados en la carpeta diagramas/05-diagramas-secuencia/ con nombres descriptivos basados en los escenarios.
- Se utilizaron actores para representar usuarios humanos (Secretaria, Medico, Paciente) y participantes para clases del sistema (Agenda, Turno).
- Se aplicó notación Clase:objeto para instancias de clases del sistema (e.g., Agenda:agenda, Turno:turno). Para actores se utilizó alias en camelCase (e.g., Secretaria as victoria).
- Los mensajes se nombraron en camelCase y se incluyeron argumentos cuando correspondía (e.g., crearTurno(fecha, hora, paciente)).
- No se incluyó destrucción de objetos (X) ya que en los escenarios modelados los objetos (e.g., Turno, Agenda) persisten en el sistema y no finalizan su ciclo de vida durante la interacción.
- Se agregaron activaciones y desactivaciones para claridad en el flujo.

## Decisiones de diseño

- Participantes: Se seleccionaron al menos 4 por diagrama basados en los actores del escenario y las colaboraciones de CRC. Por ejemplo, en "Autorizar Sobreturno" se incluyeron Secretaria, Medico, Paciente, Agenda y Turno.
- Mensajes: Se derivaron directamente del flujo principal de cada escenario, asegurando al menos 3 mensajes. Se priorizaron las responsabilidades clave de cada clase (e.g., Secretaria gestiona turnos, Turno modifica estados).
- Consistencia: Los diagramas se alinean con las tarjetas CRC, donde Secretaria colabora con Paciente, Medico y Turno; Agenda maneja disponibilidad; Turno registra solicitudes y modifica estados.
- Sintaxis PlantUML: Se usó sintaxis estándar con actores para humanos y participantes para clases, incluyendo activaciones para mostrar duración de interacciones.
- Comentarios: Cada diagrama incluye comentarios con nombre del escenario, archivo fuente y objetivo para trazabilidad.

## Reflexión

El proceso de generación de diagramas de secuencia fue efectivo al integrar los escenarios de casos de uso con las responsabilidades de las tarjetas CRC, asegurando que los diagramas fueran no solo técnicamente correctos sino también coherentes con el diseño del sistema. La referencia explícita a archivos fuente facilitó la validación y mantuvo la consistencia. Se identificó que algunos escenarios requerían más participantes para cubrir todas las colaboraciones, lo que enriqueció los diagramas. En futuras iteraciones, se podría considerar agregar más detalles como tipos de retorno o excepciones para mayor precisión.
