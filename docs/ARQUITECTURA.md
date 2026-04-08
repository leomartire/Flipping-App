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

## 💾 Especificación de Atributos (Data Dictionary)

Esta sección define la lógica de negocio para los campos críticos del sistema:

### 1. Proyectos (Flipping Projects)
- **purchase_price:** Monto de adquisición incluyendo gastos legales (Escritura + Sellos).
- **renovation_budget:** Techo financiero aprobado para la reforma. Es el benchmark del Inversor.
- **status:** `PLANNING`, `IN_PROGRESS`, `SOLD`.

### 2. Gastos & OCR (Expenses Metadata)
- **vendor_tax_id:** CUIT del proveedor detectado por el motor OCR.
- **raw_ocr_text:** Texto plano extraído para auditoría y re-procesamiento.
- **confidence_score:** Nivel de certeza de la IA (0 a 1). Si es < 0.8, requiere validación manual.

---

## 🏛️ Arquitectura del Sistema

### Flujo de Captura OCR
1. **Upload:** El Gestor sube foto del ticket desde la obra (Mobile Responsive).
2. **Analysis:** El motor OCR identifica CUIT, Fecha, Categoría y Monto.
3. **Audit:** El sistema compara el gasto contra el `renovation_budget` activo.
4. **Impact:** Actualización de KPIs en el Dashboard del Inversor.



## 📊 Métricas de Éxito (KPIs)

### KPIs de Negocio
- **Precisión de Presupuesto:** Margen de error ±5% entre estimado y real.
- **Eficiencia de Carga:** Reducción del 70% en el tiempo de carga manual de gastos.
- **Transparencia:** Disponibilidad de reportes de ROI en < 10 segundos.

---

## 🔄 Próximos Pasos

1. **Setup de Base de Datos**: Implementar el modelo físico en PostgreSQL.
2. **Módulo de Ingesta**: Desarrollar la interfaz de carga de imágenes.
3. **Integración OCR**: Conectar con la API de visión artificial.
