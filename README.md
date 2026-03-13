instalacion
Python 3.8 o superior instalado en tu sistema.
Librerías estándar de Python

descargar en maquina local por git 
git clone https://github.com/restreporg/telecomsys


Uso de la aplicación:
Al iniciar, se abrirá una ventana principal con el título "Telecomsys - Conexión Total S.A.".

La interfaz está organizada en cuatro pestañas principales:

Clientes
Permite registrar y gestionar información de clientes:
ID, tipo, nombre, documento, dirección, teléfono, correo, clasificación crediticia, etc.
Botones disponibles: Guardar, Actualizar, Eliminar, Limpiar.

Planes
Gestión de planes comerciales: 
código, nombre, tipo de servicio, características, tarifa mensual, promociones y estado. 
Botones disponibles: Guardar, Actualizar, Eliminar, Limpiar.

Contratos 
Administración de contratos: 
número, fechas, cliente asociado, plan seleccionado, dirección de instalación, equipos incluidos, condiciones especiales, monto mensual y estado.
Botones disponibles: Guardar, Actualizar, Eliminar, Limpiar. 

Facturación 
Control de facturas:
número, periodo facturado,fechas de emisión y vencimiento, cliente, servicios incluidos, cargos, descuentos, impuestos, total a pagar y forma de pago. 
Botones disponibles: Guardar, Actualizar, Eliminar, Limpiar.

La aplicación está diseñada como un monolito, por lo que todo el código se encuentra en un único archivo. Se recomienda modularizarlo en el futuro para mejorar mantenibilidad.
Este proyecto es un prototipo funcional de interfaz gráfica.
