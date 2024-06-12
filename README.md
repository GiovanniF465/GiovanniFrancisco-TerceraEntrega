# Proyecto de Registro de Empleados

Este proyecto es una aplicación web para gestionar el registro de empleados.

El nombre de la aplicación fue asignado como "main"

## Estructura del Proyecto

### Plantillas

1. **template base (`base.html`)**
   - Estructura principal de la aplicación.
   - Incluye la barra lateral de navegación y el contenido principal.

2. **Creación de empleado (`creacion.html`)**
   - Hereda de `base.html`.
   - Contiene un formulario para crear un nuevo empleado.

3. **Edición de empleado (`editarEmpleado.html`)**
   - Hereda de `base.html`.
   - Similar al template de creación, pero usado para editar empleados existentes.

4. **Listado de empleados (`empleados.html`)**
   - Hereda de `base.html`.
   - Muestra una lista de empleados con opciones para editar o eliminar cada uno.

### Vistas

1. **Inicio (`inicio`)**
   - Renderiza la página principal.
   - URL: `/`

2. **Crear nuevo empleado (`empleadoNuevo`)**
   - Renderiza y procesa el formulario de creación de empleado.
   - URL: `/empleados/nuevoEmpleado/`

3. **Listar empleados (`empleados`)**
   - Renderiza una lista de empleados y permite buscar por nombre.
   - URL: `/empleados/`

4. **Eliminar empleado (`eliminarEmpleado`)**
   - Elimina un empleado específico, indicado por su id dentro de la base de datos.
   - URL: `/empleados/eliminarEmpleado/<int:id>`

5. **Editar empleado (`editarEmpleado`)**
   - Renderiza y procesa el formulario de edición de empleado, y almacenando la edición en el empleado  ya creado.
   - URL: `/empleado/editarEmpleado/<int:id>`


