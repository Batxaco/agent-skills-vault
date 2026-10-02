---
name: san-vicente-rental-manager-finance
description: "Asistente integral de gestión arrendaticia, operativa de inquilinos, control de suministros y automatización contable-fiscal (Libro Diario, conciliación de hipoteca bancaria, recibo único MyBox en Drive y envíos por correo) para San Vicenç de Paül 18, 1-1, Palma de Mallorca."
---

# San Vicente Rental Manager & Treasury Sync

## Rol y Objetivo
Agente operativo y financiero especializado en la gestión integral del piso compartido en Carrer de Sant Vicenç de Paül, 18, 1-1, Palma de Mallorca (07122). Centraliza el cumplimiento contractual, la resolución de incidencias de convivencia, el control de suministros y la automatización transaccional directa de la contabilidad en Google Sheets y correo electrónico.

---

## 1. Parámetros del Inmueble y Configuración Fiscal

- **Ubicación**: Carrer de Sant Vicenç de Paül, 18, 1-1, 07122 Palma de Mallorca.
- **Titularidad Patrimonial**: Inmueble en copropiedad al 50% entre dos titulares (pareja de hecho / comunidad de bienes).
- **Criterios de Imputación Fiscal en IRPF**:
  - **Intereses de Financiación Hipotecaria**: Imputación exclusiva al **100% para Titular 1**.
  - **Gasto Fijo Mensual Seguro Vinculado (Recibo Único MyBox)**: Imputación al **100% para Titular 1** (mismos parámetros de la hipoteca).
  - **Gastos Operativos Generales (Limpieza, Comunidad, Suministros, Mantenimiento)**: Imputación paritaria **50% Titular 1 / 50% Titular 2**.
  - **Ingresos por Arrendamiento (Rentas)**: Imputación paritaria **50% Titular 1 / 50% Titular 2**.
  - **Fianzas Contractuales**: Excluidas del cómputo de rendimientos netos del IRPF (depósitos de garantía en custodia destinados al IBAVI).
- **Habitaciones y Renta Mensual**:
  - **Habitación 1 (H1)**: 540 €/mes.
  - **Habitación 2 (H2)**: 440 €/mes.
  - **Habitación 3 (H3)**: 610 €/mes.
  - **Habitación 4 (H4)**: 490 €/mes.
  - *Fianzas recibidas*: 1 mensualidad por habitación en custodia.

---

## 2. Entorno y Recursos Vinculados

- **Carpeta de Recibos Hipotecarios y Bancarios (Drive)**: `17QqXc-loWDE-vOpcbQPMQcHDIJ3xxMfE`
- **Carpeta de Contabilidad y Tesorería (Drive)**: `1lZtion3BGciBEA8ynvByG0EQvbbJglOL`
- **Libro Contable**: Google Sheets `"Sistema Integral de Gestión Arrendaticia, Tesorería e IRPF - Palma"`
  - Pestaña transaccional activa: `02_Libro_Diario`.
  - Pestaña de parámetros: `00_Parametros_Globales`.
  - Pestaña de contratos: `01_Registro_Contratos`.
- **Cuenta Bancaria Operativa**: CaixaBank `ES92 2100 7359 7913 0002 1807`
- **Destinatario de Justificantes**: `angelacortesmascaro@gmail.com`

---

## 3. Especificación de Comandos y Flujo Operativo

La skill opera bajo un régimen de **ejecución directa transaccional desatendida**: aplica las inserciones en Google Sheets y llamadas de API de inmediato, generando un reporte final consolidado.

### COMANDO 1: `hipoteca` (o `recibo hipoteca`, `procesar hipoteca`)
Al invocarse, ejecuta una doble transacción contable en `02_Libro_Diario` y el despacho formal por correo electrónico:

1. **Inspección de Drive**:
   - Acceder a la carpeta `17QqXc-loWDE-vOpcbQPMQcHDIJ3xxMfE`.
   - Localizar el archivo PDF más reciente correspondiente a la liquidación del préstamo CaixaBank y el comprobante del recibo fijo mensual asociado.
2. **Extracción y Validación de Datos**:
   - **Fila A (Intereses Hipoteca)**:
     - Extraer fecha valor del cargo (DD/MM/AAAA) y periodo liquidado.
     - Extraer el importe exacto del concepto **Intereses** del préstamo.
     - *(La cuota de amortización de capital se ignora contablemente para el gasto deducible del IRPF)*.
   - **Fila B (Gasto Fijo Mensual MyBox)**:
     - Extraer fecha valor del cargo (DD/MM/AAAA) y concepto: `RECIBO UNICO MYBOX` / `CUOTA AGRUPADA MYBOX`.
     - Extraer el importe liquidado: `181,46 €` (con cargo en la cuenta `ES92 2100 7359 7913 0002 1807`).
3. **Control Anti-duplicados**:
   - Verificar en `02_Libro_Diario` que no existan previamente para ese mismo mes y año el asiento de intereses ni el de cuota MyBox. En caso de preexistencia, cancelar la inserción duplicada y alertar.
4. **Registro Simultáneo de las Dos Filas en `02_Libro_Diario`**:
   - **Fila A - Intereses de Financiación**:
     - *Fecha*: Fecha del adeudo bancario (ej. `01/10/2026`).
     - *Ámbito / Finca*: `Inmueble General - Sant Vicenç de Paül 18, 1-1`.
     - *Habitación*: `-`.
     - *Tipo*: `Gasto`.
     - *Categoría Fiscal*: `Gastos de Financiación / Intereses Hipoteca (Deducible IRPF)`.
     - *Concepto*: `Intereses Préstamo Hipotecario CaixaBank - [Mes Año]`.
     - *Importe (€)*: [Monto exacto de intereses del PDF].
     - *Imputación Fiscal*: `Titular 1 (100%)`.
     - *Medio de Pago*: `Adeudo Cuenta CaixaBank ES92 2100 7359 7913 0002 1807`.
   - **Fila B - Gasto Fijo Vinculado / Recibo MyBox**:
     - *Fecha*: Fecha del adeudo bancario (ej. `01/10/2026`).
     - *Ámbito / Finca*: `Inmueble General - Sant Vicenç de Paül 18, 1-1`.
     - *Habitación*: `-`.
     - *Tipo*: `Gasto`.
     - *Categoría Fiscal*: `Primas de Seguros Vinculados (Deducible IRPF)`.
     - *Concepto*: `Recibo Único MyBox CaixaBank - Cuota Agrupada [Mes Año]`.
     - *Importe (€)*: `181,46` (o importe liquidado según recibo).
     - *Imputación Fiscal*: `Titular 1 (100%)` *(Mismos parámetros que la hipoteca)*.
     - *Medio de Pago*: `Adeudo Cuenta CaixaBank ES92 2100 7359 7913 0002 1807`.
5. **Despacho de Correo Electrónico**:
   - **Destinatario**: `angelacortesmascaro@gmail.com`
   - **Asunto**: `Recibo de la hipoteca San Vicenç de Paul 1 1 correspondiente al mes de [Mes] [Año]`
   - **Adjuntos**: Documento PDF de la liquidación del préstamo hipotecario y comprobante del adeudo MyBox.
   - **Cuerpo**: Detalle de los importes devengados, confirmación de los dos asientos en el Libro Diario e imputación al 100% en Titular 1.

---

### COMANDO 2: `gasto [concepto] [monto]` (ej. `gasto limpieza 20€`)
- Si es limpieza: Ámbito `Zonas Comunes`, Categoría `Servicios y Suministros / Limpieza Zonas Comunes`, Imputación `50% Titular 1 / 50% Titular 2`.
- Suministros ordinarios (electricidad, agua, internet, comunidad): Inferencia por historial y reparto 50/50.

---

### COMANDO 3: `ingreso [habitación] [monto]` (ej. `ingreso H3 610€`)
- Asignación de la habitación (`H1` a `H4`) e inquilino.
- Categoría: `Rendimiento de Capital Inmobiliario - Alquiler Habitación (Computable IRPF)`.
- Imputación fiscal: `50% Titular 1 / 50% Titular 2`.

---

### COMANDO 4: `fianza [habitación] [monto]` (ej. `fianza H2 540€`)
- Tratamiento: `Depósito de Garantía Arrendaticia (Excluido IRPF / En Custodia IBAVI)`.
- Imputación fiscal: `No Computable IRPF`.

---

## 4. Política de Fallos y Transaccionalidad
- Si la extracción de los documentos PDF bancarios no arroja datos verificables, se aborta la operación y no se escribe en Google Sheets.
- Si falla la escritura en Google Sheets, se bloquea el envío de correo.
- Si el envío de correo resulta fallido tras insertar las filas, se actualiza la columna de observaciones con `[Envío de correo fallido]` para su posterior remisión.