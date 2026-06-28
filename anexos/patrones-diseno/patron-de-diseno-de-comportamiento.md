# Patrones de Diseño de Comportamiento y su Relación con los Principios SOLID
En la Programación Orientada a Objetos (POO), los patrones de comportamiento constituyen un conjunto de soluciones probadas para problemas recurrentes relacionados con la interacción y comunicación entre objetos. Su propósito es definir cómo los objetos colaboran y se reparten responsabilidades, garantizando que el sistema sea flexible, extensible y fácil de mantener.

### ¿Qué son los Patrones de Comportamiento?
Patrones de comportamiento: Se centran en algoritmos y en la asignación de responsabilidades entre objetos.

**Ejemplos clásicos:** Observer, Strategy, Command, Mediator.

**Beneficio principal:** Reducen el acoplamiento y promueven la reutilización del código.

### Relación con los Principios SOLID
Los principios SOLID son lineamientos que buscan mejorar la calidad del diseño en POO. Los patrones de comportamiento se alinean directamente con ellos:

**Single Responsibility Principle:** Cada clase debe tener una única responsabilidad. Patrones como *Command* ayudan a encapsular acciones en objetos separados, evitando sobrecarga de responsabilidades.

**Open/Closed Principle:** Los sistemas deben estar abiertos a la extensión pero cerrados a la modificación. *Strategy* permite cambiar algoritmos sin alterar el código existente.

**Liskov Substitution Principle:** Los objetos derivados deben poder sustituir a sus padres sin alterar el comportamiento esperado. Patrones como *Observer* garantizan que las clases puedan ser reemplazadas sin romper la comunicación.

**Interface Segregation Principle:** Los clientes no deben depender de interfaces que no usan. Patrones como *Mediator* organizan la comunicación evitando interfaces demasiado grandes.

**Dependency Inversion Principle:** Los módulos de alto nivel no deben depender de los de bajo nivel, sino de abstracciones. Patrones como *Strategy* y *Observer* fomentan este principio al depender de interfaces y no de implementaciones concretas.

Los patrones de comportamiento no solo ofrecen soluciones prácticas a problemas comunes, sino que también refuerzan los principios SOLID, logrando sistemas más robustos, escalables y fáciles de mantener. En esencia, los patrones son la aplicación concreta de los principios de diseño, y juntos forman la base de un programa de calidad.

## Propósito y Tipo del Patrón

**Propósito:** El sistema de turnos médicos actual estaba lidiando con un programa para notificar cambios de turno al paciente y médico asociados.

Agenda, la cual ya estaba lidiando con varios métodos que podrían ralentizar el proceso del programa, tenía asignado este comportamiento.

El hecho de que este método esté en Agenda puede provocar problemas a la hora de decidir expandir o modificar el código, debido a que no cumple con el Principio de Responsabilidad Única y el Principio de Abierto/Cerrado.

**Tipo:** El patrón de diseño de comportamiento seleccionado para este problema es *Observer*. Este mismo establece una relación de dependencia de uno a muchos entre objetos, permitiendo que cuando un objeto cambie su estado, todos los objetos interesados sean notificados y actualizados automáticamente. 

Sirve para desacoplar emisores de eventos de sus receptores, facilitando la extensibilidad y la comunicación dinámica en sistemas orientados a objetos.

Por esta misma razón, la aplicación de este patrón sería beneficiosa no solo para Agenda, sino para la organización del programa en sí.

## Motivación

El sistema originalmente manejaba el sistema de notificaciones mediante un método en Agenda llamado 'enviarNotificacion()'. Aunque puede parecer algo sencillo, de hecho resulta ser algo impráctico después. No solo añade muchas más responsabilidades innecesarias a Agenda, haciendo conflicto con el Principio de Responsabilidad Única y el Principio de Abierto/Cerrado, sino que también puede ralentizar el proceso de registrar un turno por algo de lo que podrían encargarse otras clases de forma más eficientes.

El patrón introduce a las nuevas clases:

- *Sujeto:* Contiene los métodos necesarios para notificar los nuevos cambios a las demás clases suscriptas.

- *NotificacionMedio:* Adapta la información con respecto a los nuevos cambios en un mensaje.

- *NotificacionEmail:* Envía el mensaje transformado por *NotificacionMedio* al paciente y médico asociados al turno por Email.

- *NotificacionWhatsapp:* Envía el mensaje transformado por *NotificacionMedio* al paciente y médico asociados al turno por Whatsapp.

De esta forma, se agregan más clases para manejar el nuevo sistema de notificaciones. Cumpliendo con el Principio de Responsabilidad Única y el Principio de Abierto/Cerrado, con este último se hace mucho más sencillo modificar alguna parte de este procedimiento sin tener que alterar las demás clases y comportamientos.


## Estructura de Clases

[Diagrama de Clases con Observer](../../diagramas/01-diagrama-clases/01-patron-comportamiento-observer.png)

## Justificación Técnica de la Estructura de Clases

### Explicación Detallada de Cada Clase Utilizada

- **Turno:** Su responsabilidad es vincular turnos con fecha y hora con su paciente y médico respectivos. Gestiona los métodos para registrar, asignar, modificar y reprogramar turnos. Interactúa con otras clases mediante el Notificador, que es el que observa el comportamiento de Turno y envía un mensaje recordatorio al Paciente y Medico asignados en el turno por medio de NotificadorMedio, al mismo tiempo que activa Auditoria para guardar los detalles del evento; esto ocurre cada vez que haya un cambio en el estado de Turno. Es indispensable para la implementación del patrón debido a que, en los requisitos funcionales, es el objeto observable.

- **Auditoria:** Su responsabilidad es garantizar la trazabilidad completa con referencia al turno, usuario, acción realizada, timestamp y detalles de cambios. Gestiona los comportamientos para guardar los eventos con todos los detalles. Interactúa con Notificacion para avisarle que el estado de Turno cambió y obtiene los detalles desde el Turno. Es indispensable debido a que uno de los requisitos funcionales del sistema es que se tenga un registro de todos los cambios realizados con el usuario y acción realizada.

- **Sujeto:** Clase abstracta que encapsula los métodos para suscribirse, desuscribirse y notificar acerca de cualquier cambio de estado del Turno. Sirve para que Turno herede sus comportamientos y pueda notificar los cambios a Notificacion.

- **NotificacionMedio:** Se encarga de enviar un mensaje recordatorio para los usuarios suscriptos a Sujeto.

- **NotificacionEmail:** Envía el mensaje mediante Email para el Paciente o Médico asociados con el turno.

- **NotificacionWhatsapp:** Envía el mensaje mediante Whatsapp para el Paciente o Médico asociados con el turno.

- **iNotificacion:** Interfaz que sirve como el medio general por el cuál los objetos suscriptos a Sujeto se notifican con respecto a los cambios realizados en Turno.

### Descripcion del Flujo de Comportamiento

Cada vez que se crea un nuevo turno que se asocia a un usuario y a un médico, el Turno automáticamente realiza la suscripción (ya que hereda estos comportamientos de Sujeto) de estos a la misma clase.

Cuando Turno cambia de estado, la interfaz iNotificacion recibe estos datos y llama a las demás clases suscriptas, NotificacionMedio y Auditoria, para que accedan directamente al Turno.

En el caso de NotificacionMedio, transforma la información en un mensaje y lo pasa a NotificacionEmail y NotificacionWhatsapp para que lo manden en sus respectivos medios al paciente y médico asociados al Turno registrado.

