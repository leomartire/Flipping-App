# 🔄 Ciclo de Vida del Desarrollo (SDLC) - Flipping-App

Este documento define las fases y estándares para el desarrollo de la aplicación de control de gastos familiares, asegurando la calidad y trazabilidad del software.

## 📋 Metodología
Se utiliza un enfoque **Ágil-Híbrido**, combinando la flexibilidad de Scrum con el rigor documental de metodologías empresariales (inspirado en Oracle OUM).



## 🏗️ Fases del Ciclo

### 1. Planificación y Requerimientos (Análisis)
- **Objetivo:** Definir las necesidades financieras del proyecto (ingresos, gastos, presupuestos). Definir formas de ingreso de gastos: manual / automatizada por medio de OCR.
- **Entregable:** `docs/PROYECTO.md` y `docs/PLAN_DESARROLLO.md`.

### 2. Diseño de la Solución
- **Objetivo:** Estructurar la base de datos y la arquitectura técnica.
- **Entregable:** `docs/MODELO_DATOS.md` y `docs/ARQUITECTURA.md`.

### 3. Configuración del Entorno (Setup)
- **Objetivo:** Preparar el repositorio de GitHub y el entorno local de Python.
- **Entregable:** Archivos `.gitignore`, `requirements.txt` y estructura de carpetas.

### 4. Desarrollo (Build)
- **Objetivo:** Codificación de la lógica de negocio (Python) e interfaz.
- **Estándar:** Uso de Commits descriptivos y código limpio.

### 5. Pruebas (Testing / QA)
- **Objetivo:** Validar la integridad de los datos financieros (conciliación de saldos).
- **Actividad:** Pruebas unitarias de las funciones de cálculo.

### 6. Despliegue (Deployment)
- **Objetivo:** Publicación de la aplicación en la nube para uso real.
- **Plataforma sugerida:** Streamlit Cloud o Render.

### 7. Mantenimiento y Evolución
- **Objetivo:** Agregar nuevas funcionalidades (ej. visualización de gráficos) y corrección de errores.

---
*Última actualización: Abril 2026*
