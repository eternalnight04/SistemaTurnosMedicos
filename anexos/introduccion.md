# Introducción

---

## Descripción del Paradigma Orientado a Objetos

El paradigma orientado a objetos (POO) es un modelo de programación basado en la representación de entidades del mundo real mediante objetos. Un objeto combina datos (atributos) y comportamientos (métodos) dentro de una misma estructura.

Este paradigma permite organizar sistemas complejos de forma modular, facilitando la reutilización, el mantenimiento y la escalabilidad del software.

En el sistema de turnos médicos, entidades como Paciente, Médico o Turno pueden representarse como clases con atributos y comportamientos propios.

---

## Los Cuatro Fundamentos de la Programación Orientada a Objetos

### 1. Abstracción

Consiste en representar solo las características esenciales de un objeto, ocultando detalles innecesarios.

Ejemplo: La clase Turno puede contener fecha, hora y estado, sin modelar detalles irrelevantes.

---

### 2. Encapsulamiento

Implica proteger los datos internos de un objeto y permitir el acceso mediante métodos definidos.

Ejemplo: El historial médico de un paciente podría ser un atributo privado accesible mediante métodos controlados.

---

### 3. Herencia

Permite que una clase derive de otra, heredando atributos y comportamientos.

Ejemplo: Una clase Persona podría ser base de Médico y Paciente.

---

### 4. Polimorfismo

Permite que distintos objetos respondan de forma diferente ante el mismo método.

Ejemplo: Un método calcularCosto() podría comportarse distinto según el tipo de consulta.

---

## Requisitos Iniciales del Sistema

El sistema de turnos médicos tiene como objetivo gestionar la asignación, modificación y cancelación de turnos entre pacientes y profesionales de la salud.

### Requisitos Funcionales (RF)

* RF01: Permitir a los pacientes solicitar turnos médicos.
* RF02: Permitir a los pacientes cancelar o reprogramar turnos.
* RF03: Permitir a los médicos visualizar su agenda de turnos.
* RF04: Registrar información básica de pacientes y médicos.
* RF05: Gestionar la disponibilidad horaria de los profesionales.

### Requisitos No Funcionales (RNF)

* RNF01: El sistema debe ser accesible y fácil de usar.
* RNF02: Debe garantizar la seguridad y privacidad de los datos.
* RNF03: Debe permitir escalabilidad ante aumento de usuarios.
* RNF04: El tiempo de respuesta debe ser menor a 2 segundos en operaciones comunes.

---

## Casos de Uso

A partir del análisis de los requisitos, se definieron los siguientes casos de uso principales:

* UC-01: Registrar paciente
* UC-02: Solicitar turno
* UC-03: Cancelar turno
* UC-04: Reprogramar turno
* UC-05: Visualizar agenda médica

Cada caso de uso describe la interacción entre los actores (Paciente y Médico) y el sistema, permitiendo modelar el comportamiento esperado del mismo.

---

## Boceto Inicial del Diseño de Clases

El diseño inicial del sistema se representa mediante un diagrama de clases que modela las entidades principales y sus relaciones.

Entre las clases identificadas se encuentran:

* Paciente
* Médico
* Turno
* Agenda

Estas clases incluyen atributos y métodos que reflejan el comportamiento del sistema, así como relaciones de asociación entre ellas.

El diagrama fue desarrollado en formato `.excalidraw`, `.png` y `.puml`, permitiendo su visualización y documentación dentro del repositorio.

---
