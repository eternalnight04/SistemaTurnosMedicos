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
- herramientas-agile/tarjetas-crc/01-tarjeta-crc-paciente.md

## Ajustes realizados

- Se crearon 5 archivos PUMl separados en la carpeta diagramas/05-diagramas-secuencia/ con nombres descriptivos basados en los escenarios.
- Se utilizaron actores para representar usuarios humanos (Secretaria, Medico, Paciente) y participantes para clases del sistema (Agenda, Turno).
- Se aplicó notación Clase:objeto para instancias de clases del sistema (e.g., Agenda:agenda, Turno:turno). Para actores se utilizó alias en camelCase (e.g., Secretaria as victoria).
- Los mensajes se nombraron en camelCase y se incluyeron argumentos cuando correspondía (e.g., crearTurno(fecha, hora, paciente)).
- Se agregaron activaciones y desactivaciones para claridad en el flujo.
- Se corrigieron algunas flechas y se cambiaron de lugar ciertos actores para una mejor organización.

## Iteraciones

### Iteración 1

```
Corrija los siguientes diagramas teniendo en cuenta que hay que indicar la finalización de los objetos que dejan de existir durante el escenario mediante una X al final de la línea de vida (destroy objeto). Esto es obligatorio para objetos que se crean temporalmente y no persisten.
```

### Respuesta

✓ Completado. He agregado los símbolos de finalización (`destroy`) a todos los 5 diagramas de secuencia:

- **05-secuencia-autorizar-sobreturno-05.puml**: `destroy turno` y `destroy agenda`
- **05-secuencia-cancelar-turno-02.puml**: `destroy turno` y `destroy agenda`
- **05-secuencia-crear-turno-01.puml**: `destroy turno` y `destroy agenda`
- **05-secuencia-registrar-llegada-04.puml**: `destroy turno` y `destroy agenda`
- **05-secuencia-reprogramar-turno-03.puml**: `destroy turno` y `destroy agenda`

Ahora los diagramas mostrarán una **X** al final de la línea de vida de los objetos `Turno` y `Agenda`, indicando correctamente su finalización según la notación UML estándar.

### Iteración 2

```
Corrija los siguientes diagramas teniendo en cuenta que los mensajes de retorno no deben tener formato de método (), ya que son respuestas a la invocación de un método, es decir, al mensaje que se recibió primero.
```

### Respuesta

✓ Corregidos. He eliminado los paréntesis de los siguientes mensajes de retorno:

- **05-secuencia-crear-turno-01.puml**: `disponibilidadConfirmada()` → `disponibilidadConfirmada`
- **05-secuencia-reprogramar-turno-03.puml**: `conflictoDetectado()` → `conflictoDetectado` y `horarioValido()` → `horarioValido`

Ahora los diagramas siguen la notación correcta de UML, donde los mensajes de retorno (`-->`) son respuestas simples sin formato de método.

### Iteración 3

```
Elimina los nombres propios.
```

### Respuesta

✓ Completado. He eliminado todos los nombres propios de los actores en los 5 diagramas de secuencia. Los cambios realizados:

- **victoria** → `secretaria`
- **drMolina** → `medico`
- **patricia, roberto, juan, diego_martinez, maria** → `paciente`

Ahora los diagramas utilizan nombres genéricos en minúsculas que representan los roles sin referencias a nombres específicos, haciendo los diagramas más profesionales y reutilizables.

## Decisiones de diseño

- Participantes: Se seleccionaron al menos 4 por diagrama basados en los actores del escenario y las colaboraciones de CRC. Por ejemplo, en "Autorizar Sobreturno" se incluyeron Secretaria, Medico, Paciente, Agenda y Turno.
- Mensajes: Se derivaron directamente del flujo principal de cada escenario, asegurando al menos 3 mensajes. Se priorizaron las responsabilidades clave de cada clase (e.g., Secretaria gestiona turnos, Turno modifica estados).
- Consistencia: Los diagramas se alinean con las tarjetas CRC, donde Secretaria colabora con Paciente, Medico y Turno; Agenda maneja disponibilidad; Turno registra solicitudes y modifica estados.
- Sintaxis PlantUML: Se usó sintaxis estándar con actores para humanos y participantes para clases, incluyendo activaciones para mostrar duración de interacciones.
- Comentarios: Cada diagrama incluye comentarios con nombre del escenario, archivo fuente y objetivo para trazabilidad.

## Reflexión

El proceso de generación de diagramas de secuencia fue efectivo al integrar los escenarios de casos de uso con las responsabilidades de las tarjetas CRC, asegurando que los diagramas fueran no solo técnicamente correctos sino también coherentes con el diseño del sistema. La referencia explícita a archivos fuente facilitó la validación y mantuvo la consistencia. Se identificó que algunos escenarios requerían más participantes para cubrir todas las colaboraciones, lo que enriqueció los diagramas. En futuras iteraciones, se podría considerar agregar más detalles como tipos de retorno o excepciones para mayor precisión.
