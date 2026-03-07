import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.geometry('600x800')
root.title("Telecomsys - Conexión Total S.A.")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Clientes")
notebook.add(tab2, text="Planes")
notebook.add(tab3, text="Contratos")
notebook.add(tab4, text="Facturación")

# Empaquetar el Notebook
notebook.pack(expand=True, fill="both")

# ---------------- PESTAÑA 1: CLIENTES ----------------
titulo1 = tk.Label(tab1, text="GESTIÓN DE CLIENTES", font=("Arial", 16, "bold"), fg="black")
titulo1.pack(pady=20)

form1 = tk.Frame(tab1)
form1.pack(pady=20, anchor="w", padx=100)

tk.Label(form1, text="ClienteID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ClienteID = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
ClienteID.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form1, text="Tipo Cliente:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
TipoCliente = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
TipoCliente.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form1, text="Nombre/Razón Social:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
NombreCliente = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
NombreCliente.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form1, text="Documento/RUC:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Documento = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
Documento.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form1, text="Fecha Nacimiento/Constitución:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
FechaNacimiento = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaNacimiento.grid(row=5, column=1, sticky="w", pady=10)

tk.Label(form1, text="Dirección:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Direccion = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
Direccion.grid(row=6, column=1, sticky="w", pady=10)

tk.Label(form1, text="Coordenadas Geográficas:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Coordenadas = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
Coordenadas.grid(row=7, column=1, sticky="w", pady=10)

tk.Label(form1, text="Teléfono:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Telefono = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
Telefono.grid(row=8, column=1, sticky="w", pady=10)

tk.Label(form1, text="Correo:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
Correo = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
Correo.grid(row=9, column=1, sticky="w", pady=10)

tk.Label(form1, text="Fecha de Registro:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
FechaRegistro = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaRegistro.grid(row=10, column=1, sticky="w", pady=10)

tk.Label(form1, text="Clasificación Crediticia:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
Clasificacion = tk.Entry(form1, width=25, font=("Arial", 12), relief="solid", bd=1)
Clasificacion.grid(row=11, column=1, sticky="w", pady=10)

btn_frame1 = tk.Frame(tab1)
btn_frame1.pack(pady=20)
btn_save1 = tk.Button(btn_frame1, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save1.pack(side=tk.LEFT, padx=5)
btn_update1 = tk.Button(btn_frame1, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update1.pack(side=tk.LEFT, padx=5)
btn_delete1 = tk.Button(btn_frame1, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete1.pack(side=tk.LEFT, padx=5)
btn_clear1 = tk.Button(btn_frame1, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear1.pack(side=tk.LEFT, padx=5)

# ---------------- PESTAÑA 2: PLANES ----------------
titulo2 = tk.Label(tab2, text="GESTIÓN DE PLANES", font=("Arial", 16, "bold"), fg="black")
titulo2.pack(pady=20)

form2 = tk.Frame(tab2)
form2.pack(pady=20, anchor="w", padx=100)

tk.Label(form2, text="Código Plan:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CodigoPlan = tk.Entry(form2, width=25, font=("Arial", 12), relief="solid", bd=1)
CodigoPlan.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form2, text="Nombre Comercial:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
NombrePlan = tk.Entry(form2, width=25, font=("Arial", 12), relief="solid", bd=1)
NombrePlan.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form2, text="Tipo Servicio:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
TipoServicio = tk.Entry(form2, width=25, font=("Arial", 12), relief="solid", bd=1)
TipoServicio.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form2, text="Características:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Caracteristicas = tk.Entry(form2, width=25, font=("Arial", 12), relief="solid", bd=1)
Caracteristicas.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form2, text="Tarifa Mensual:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
TarifaMensual = tk.Entry(form2, width=25, font=("Arial", 12), relief="solid", bd=1)
TarifaMensual.grid(row=5, column=1, sticky="w", pady=10)

tk.Label(form2, text="Permanencia Mínima:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
PermanenciaMinima = tk.Entry(form2, width=25, font=("Arial", 12), relief="solid", bd=1)
PermanenciaMinima.grid(row=6, column=1, sticky="w", pady=10)

tk.Label(form2, text="Promociones:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Promociones = tk.Entry(form2, width=25, font=("Arial", 12), relief="solid", bd=1)
Promociones.grid(row=7, column=1, sticky="w", pady=10)

tk.Label(form2, text="Estado:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
EstadoPlan = tk.Entry(form2, width=25, font=("Arial", 12), relief="solid", bd=1)
EstadoPlan.grid(row=8, column=1, sticky="w", pady=10)

btn_frame2 = tk.Frame(tab2)
btn_frame2.pack(pady=20)
btn_save2 = tk.Button(btn_frame2, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save2.pack(side=tk.LEFT, padx=5)
btn_update2 = tk.Button(btn_frame2, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update2.pack(side=tk.LEFT, padx=5)
btn_delete2 = tk.Button(btn_frame2, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete2.pack(side=tk.LEFT, padx=5)
btn_clear2 = tk.Button(btn_frame2, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear2.pack(side=tk.LEFT, padx=5)

# ---------------- PESTAÑA 3: CONTRATOS ----------------
titulo3 = tk.Label(tab3, text="GESTIÓN DE CONTRATOS", font=("Arial", 16, "bold"), fg="black")
titulo3.pack(pady=20)

form3 = tk.Frame(tab3)
form3.pack(pady=20, anchor="w", padx=100)

tk.Label(form3, text="Número Contrato:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
NumeroContrato = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
NumeroContrato.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form3, text="Fecha Firma:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
FechaFirma = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaFirma.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form3, text="Cliente:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ClienteContrato = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
ClienteContrato.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form3, text="Tipo Servicio:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
TipoServicioContrato = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
TipoServicioContrato.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form3, text="Plan Seleccionado:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
PlanSeleccionado = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
PlanSeleccionado.grid(row=5, column=1, sticky="w", pady=10)

tk.Label(form3, text="Dirección Instalación:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
DireccionInstalacion = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
DireccionInstalacion.grid(row=6, column=1, sticky="w", pady=10)

tk.Label(form3, text="Equipos Incluidos:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
EquiposIncluidos = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
EquiposIncluidos.grid(row=7, column=1, sticky="w", pady=10)

tk.Label(form3, text="Condiciones Especiales:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
CondicionesEspeciales = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
CondicionesEspeciales.grid(row=8, column=1, sticky="w", pady=10)

tk.Label(form3, text="Fecha Inicio:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
FechaInicio = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaInicio.grid(row=9, column=1, sticky="w", pady=10)

tk.Label(form3, text="Duración:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
Duracion = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
Duracion.grid(row=10, column=1, sticky="w", pady=10)

tk.Label(form3, text="Monto Mensual:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
MontoMensual = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
MontoMensual.grid(row=11, column=1, sticky="w", pady=10)

tk.Label(form3, text="Estado:", font=("Arial", 12)).grid(row=12, column=0, sticky="w", padx=(0, 10), pady=10)
EstadoContrato = tk.Entry(form3, width=25, font=("Arial", 12), relief="solid", bd=1)
EstadoContrato.grid(row=12, column=1, sticky="w", pady=10)

btn_frame3 = tk.Frame(tab3)
btn_frame3.pack(pady=20)
btn_save3 = tk.Button(btn_frame3, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save3.pack(side=tk.LEFT, padx=5)
btn_update3 = tk.Button(btn_frame3, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update3.pack(side=tk.LEFT, padx=5)
btn_delete3 = tk.Button(btn_frame3, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete3.pack(side=tk.LEFT, padx=5)
btn_clear3 = tk.Button(btn_frame3, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear3.pack(side=tk.LEFT, padx=5)

# ---------------- PESTAÑA 4: FACTURACIÓN ----------------
titulo4 = tk.Label(tab4, text="GESTIÓN DE FACTURACIÓN", font=("Arial", 16, "bold"), fg="black")
titulo4.pack(pady=20)

form4 = tk.Frame(tab4)
form4.pack(pady=20, anchor="w", padx=100)

tk.Label(form4, text="Número Factura:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
NumeroFactura = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
NumeroFactura.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form4, text="Periodo Facturado:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
PeriodoFacturado = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
PeriodoFacturado.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form4, text="Fecha Emisión:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
FechaEmision = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaEmision.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form4, text="Fecha Vencimiento:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
FechaVencimiento = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaVencimiento.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form4, text="Cliente:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
ClienteFactura = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
ClienteFactura.grid(row=5, column=1, sticky="w", pady=10)

tk.Label(form4, text="Servicios Incluidos:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
ServiciosIncluidos = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
ServiciosIncluidos.grid(row=6, column=1, sticky="w", pady=10)

tk.Label(form4, text="Cargos Fijos:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
CargosFijos = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
CargosFijos.grid(row=7, column=1, sticky="w", pady=10)

tk.Label(form4, text="Cargos Variables:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
CargosVariables = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
CargosVariables.grid(row=8, column=1, sticky="w", pady=10)

tk.Label(form4, text="Descuentos:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
Descuentos = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
Descuentos.grid(row=9, column=1, sticky="w", pady=10)

tk.Label(form4, text="Impuestos:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
Impuestos = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
Impuestos.grid(row=10, column=1, sticky="w", pady=10)

tk.Label(form4, text="Total a Pagar:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
TotalPagar = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
TotalPagar.grid(row=11, column=1, sticky="w", pady=10)

tk.Label(form4, text="Estado Pago:", font=("Arial", 12)).grid(row=12, column=0, sticky="w", padx=(0, 10), pady=10)
EstadoPago = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
EstadoPago.grid(row=12, column=1, sticky="w", pady=10)

tk.Label(form4, text="Forma de Pago:", font=("Arial", 12)).grid(row=13, column=0, sticky="w", padx=(0, 10), pady=10)
FormaPago = tk.Entry(form4, width=25, font=("Arial", 12), relief="solid", bd=1)
FormaPago.grid(row=13, column=1, sticky="w", pady=10)

btn_frame4 = tk.Frame(tab4)
btn_frame4.pack(pady=20)
btn_save4 = tk.Button(btn_frame4, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save4.pack(side=tk.LEFT, padx=5)
btn_update4 = tk.Button(btn_frame4, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update4.pack(side=tk.LEFT, padx=5)
btn_delete4 = tk.Button(btn_frame4, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete4.pack(side=tk.LEFT, padx=5)
btn_clear4 = tk.Button(btn_frame4, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear4.pack(side=tk.LEFT, padx=5)

root.mainloop()