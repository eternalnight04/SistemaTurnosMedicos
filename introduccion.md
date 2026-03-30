## Requisitos iniciales del sistema

**Evidencia de IA:** https://notebooklm.google.com/notebook/58bfbaaf-a9ca-48a9-b641-21619e4ec0d2

### Especificación de Requisitos Funcionales (RF)
1. **RF1 - Gestión integral de turnos y agenda:** El sistema debe permitir las operaciones de creación, reprogramación y cancelación de turnos vinculados a un profesional específico. Asimismo, debe proporcionar una visualización organizada de la agenda en intervalos diarios y semanales para facilitar la gestión administrativa.
2. **RF2 - Prevención de conflictos de programación:** El sistema debe validar la disponibilidad del profesional de manera que se impida automáticamente la superposición de dos o más turnos en un mismo bloque horario. Esta restricción es considerada la funcionalidad crítica primordial del modelo.
3. **RF3 - Gestión de disponibilidad y bloqueos horarios:** El sistema debe permitir la configuración de la disponibilidad del profesional, incluyendo el bloqueo de horarios por vacaciones, feriados, reuniones o compromisos académicos fijos, como las clases dictadas los jueves por la tarde.
4. **RF4 - Administración de sobreturnos autorizados:** El sistema debe permitir la incorporación manual de hasta dos sobreturnos diarios, condicionados exclusivamente a la decisión y autorización del profesional médico. El sistema no debe automatizar esta función para evitar el colapso de la atención.
5. **RF5 - Registro de presencia física (Check-in):** El sistema debe permitir registrar la llegada de los pacientes al consultorio, cambiando su estado a "presente" o "en sala de espera" y capturando la hora real de arribo. Esta entidad debe ser liviana y estar vinculada al turno correspondiente.

---

### Especificación de Requisitos No Funcionales (RNF)
*Los requisitos no funcionales establecen las restricciones y criterios de calidad bajo los cuales el sistema debe operar.*

1. **RNF1 - Usabilidad y simplicidad de interfaz:** El sistema debe poseer una interfaz de usuario intuitiva y de baja complejidad técnica, diseñada para que el profesional y la secretaría puedan operarlo sin necesidad de capacitaciones extensas o procesos disruptivos.
2. **RNF2 - Escalabilidad y extensibilidad del modelo:** El diseño de la arquitectura y el modelo de dominio deben permitir la futura incorporación de nuevos profesionales y salas de consulta sin requerir una reestructuración del núcleo del sistema.
3. **RNF3 - Plazo de entrega de Producto Mínimo Viable (MVP):** El sistema debe estar desarrollado, validado y funcional para su implementación operativa a principios de julio de 2026.
4. **RNF4 - Restricción de infraestructura física:** El modelo de dominio debe considerar, en su etapa inicial, la limitación de una única sala física de consulta disponible para la atención, lo cual simplifica la gestión de conflictos de espacio en el MVP.
5. **RNF5 - Integridad y encapsulamiento del dominio:** El sistema debe garantizar que la lógica de validación de disponibilidad resida exclusivamente en la clase agenda, impidiendo que otros módulos manipulen directamente la colección de turnos sin pasar por las reglas de negocio establecidas.