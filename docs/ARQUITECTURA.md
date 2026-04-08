# 🏗️ Arquitectura de la Solución - Flipping Management Tool Pro

## 🎯 Visión General

### Propósito
Plataforma integral para la gestión de proyectos de flipping inmobiliario, permitiendo el seguimiento completo del ciclo de vida desde la adquisición hasta la venta final, con un fuerte enfoque en el control de costos mediante automatización OCR.

### Usuarios Principales
- **Socio Gestor**: Control operativo total, gestión de obras y carga de comprobantes vía OCR.
- **Socio Inversor**: Visualización de ROI, reportes de desvíos y salud financiera en USD.

---

## 🛠️ Stack Tecnológico

### Frontend & Backend
- **Framework:** Next.js 14+ (App Router)
- **Lenguaje:** TypeScript
- **UI Library:** Tailwind CSS + shadcn/ui
- **Base de Datos:** PostgreSQL (con soporte para tipos de datos Decimal y JSONB para OCR)

### Integraciones de IA
- **OCR Engine:** Google Cloud Vision API / AWS Textract (para extracción de datos contables).
- **Lógica de Negocio:** Python microservice (opcional) para procesamiento pesado de datos financieros.

---

## 💾 Especificación de Entidades y Atributos (Data Dictionary)

Esta sección define la lógica de negocio para los campos críticos del sistema:

### 1. Entidad: Proyectos (Flipping Projects)
- **id (UUID):** Identificador único universal. Evita colisiones de datos si escalamos a múltiples bases de datos.
- **name (String):** Nombre comercial o dirección de la propiedad.
- **purchase_price (Decimal):** Costo total de adquisición. Incluye el valor de compra más gastos legales (escritura, sellos e impuestos).
- **renovation_budget (Decimal):** Techo financiero aprobado por el Inversor para la reforma. Es el valor contra el cual se compararán los desvíos.
- **status (Enum):** Ciclo de vida del proyecto: PLANNING (Estudio), IN_PROGRESS (Obra activa), SOLD (Finalizado y liquidado).

### 2. Entidad: Gastos con Soporte OCR (Expenses)
Registro de egresos operativos optimizado para la carga digital.

- **id (UUID):** Identificador de la transacción.
- **project_id (FK):** Vincula el gasto a una obra específica.
- **vendor_id (FK):** Identifica al proveedor. Este campo es poblado automáticamente por el motor OCR al detectar el CUIT/Tax ID.
- **amount (Decimal):** Valor total expresado en moneda de curso legal.
- **receipt_url (String):** Puntero al almacenamiento en la nube donde reside la imagen del comprobante (evidencia de auditoría).
 
## 3. Entidad: Metadatos de IA (OCR_METADATA)
Capa de auditoría técnica que separa el dato procesado del dato crudo extraído por la IA.

- **expense_id (PK/FK):** Referencia uno-a-uno con el gasto.
- **raw_text (Text):** Almacenamiento del bloque de texto completo extraído por el OCR. Permite re-procesar el gasto sin necesidad de re-escanear la imagen.
- **confidence (Float):** Puntaje de precisión (0.00 a 1.00). Si es menor a 0.80, el sistema debería forzar una revisión manual del Socio Gestor.

## 4. Entidad: Socios y Capital (Partners & Equity)
Define la estructura de propiedad y el riesgo de la inversión.

- **equity_contribution (Decimal):** Monto líquido aportado por el socio al proyecto.
- **share_percentage (Float):** Cuota de participación sobre las utilidades netas finales (Equity Share).




---

## 🏛️ Arquitectura del Sistema

### Flujo de Captura OCR
1. **Upload:** El Gestor sube foto del ticket desde la obra (Mobile Responsive).
2. **Analysis:** El motor OCR identifica CUIT, Fecha, Categoría y Monto.
3. **Audit:** El sistema compara el gasto contra el `renovation_budget` activo.
4. **Impact:** Actualización de KPIs en el Dashboard del Inversor.

### Módulos Críticos
- **Motor de Cálculo de Desvíos:** Compara en tiempo real `Real Spent` vs `Renovation Budget`.
- **Módulo de Reportes:** Generación de Variance Analysis para el Socio Inversor.

## 📊 Métricas de Éxito (KPIs)

### KPIs de Negocio
- **Precisión de Presupuesto:** Margen de error ±5% entre estimado y real.
- **Eficiencia de Carga:** Reducción del 70% en el tiempo de carga manual de gastos.
- **Transparencia:** Disponibilidad de reportes de ROI en < 10 segundos.

---
## 👥 Roles y Permisos

| Funcionalidad | Socio Gestor | Socio Inversor |
| :--- | :---: | :---: |
| Carga de Gastos / OCR | ✅ | ❌ |
| Gestión de Proveedores | ✅ | ❌ |
| Ver Dashboard de ROI | ✅ | ✅ |
| Edición de Presupuesto Inicial | ❌ | ✅ |
| Auditoría de Comprobantes | ✅ | ✅ |

---
## 🔄 Próximos Pasos

1. **Setup de Base de Datos**: Implementar el modelo físico en PostgreSQL.
2. **Módulo de Ingesta**: Desarrollar la interfaz de carga de imágenes.
3. **Integración OCR**: Conectar con la API de visión artificial.
