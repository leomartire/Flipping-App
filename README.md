# 🏢 Flipping Management Tool - Documentación del Proyecto

## 📋 Descripción General

Sistema integral de gestión para proyectos de flipping inmobiliario en CABA, diseñado para optimizar la colaboración entre el Socio Gestor y el Socio Inversor.

### 🎯 Objetivos del Proyecto
- Centralizar información de propiedades y proyectos
- Automatizar cálculo y seguimiento de ROI
- Facilitar transparencia financiera
- Optimizar gestión de obras y proveedores
- Generar reportes automáticos

---

## 📚 Documentación Disponible

### 0. [📄 Descripción General del Proyecto](./docs/PROYECTO.md)

### 1. [🏗️ Arquitectura de la Solución](./docs/ARQUITECTURA.md)
Documento completo de arquitectura del sistema que incluye:
- Visión general del proyecto
- Stack tecnológico recomendado
- Arquitectura de 3 capas (Frontend, API, Database)
- Modelo de datos con todas las entidades
- Módulos funcionales detallados
- Flujos de usuario
- Matriz de permisos por rol
- Plan de implementación en 4 fases

**Ideal para**: Desarrolladores, arquitectos de software, gestores de proyecto

---

### 2. [📊 Modelo de Datos](./docs/MODELO_DATOS.md)
Diagrama Entidad-Relación completo con:
- Modelo de datos en formato Mermaid ERD
- Definición de todas las tablas
- Relaciones entre entidades
- Enumeraciones (UserRole, PropertyStatus, etc.)
- Índices recomendados para performance
- Constraints de negocio

**Ideal para**: DBAs, desarrolladores backend, arquitectos de datos

---

### 3. [🎨 Diseño de UI/UX](./docs/DISENO_UI_UX.md)
Sistema de diseño y wireframes que cubre:
- Paleta de colores completa
- Tipografía y espaciado
- Diseños de todas las pantallas principales
- Componentes reutilizables (Button, Card, StatusBadge, etc.)
- Patrones de interacción
- Responsive design
- Accesibilidad (WCAG 2.1 AA)
- Animaciones y transiciones

**Ideal para**: Diseñadores UI/UX, desarrolladores frontend

---

### 4. [📅 Plan de Desarrollo](./docs/PLAN_DESARROLLO.md)
Roadmap detallado de implementación con:
- Timeline de 15 semanas dividido en 4 fases
- Tareas día a día para cada sprint
- Entregables específicos por fase
- Estrategia de testing (unit, integration, E2E)
- Configuración de CI/CD
- KPIs del proyecto
- Presupuesto estimado
- Consideraciones de seguridad

**Ideal para**: Gestores de proyecto, desarrolladores, stakeholders

---

## 🗂️ Diagramas Visuales

Durante la presentación se generaron los siguientes diagramas interactivos:

### Arquitectura del Sistema
Diagrama de 3 capas mostrando:
- Frontend: Dashboards de Gestor e Inversor
- API Layer: Services de Propiedades, Proyectos, Finanzas, etc.
- Data Layer: Tablas de PostgreSQL

### Flujo del Proceso de Flipping
Flowchart completo del ciclo de vida:
1. Fase 1: Sourcing (Semanas 1-6)
2. Fase 2: Adquisición (Semanas 7-8)
3. Fase 3: Remodelación (Meses 2-7)
4. Fase 4: Venta (Meses 8-10)

---

## 🚀 Próximos Pasos Recomendados

### Inmediatos
1. **Validar Arquitectura**: Revisar estos documentos con el equipo técnico
2. **Refinamiento**: Ajustar el modelo de datos según necesidades específicas
3. **Diseño UI/UX**: Crear prototipos en Figma basándose en los wireframes

### Corto Plazo
4. **Setup del Proyecto**: Inicializar repositorio siguiendo el Plan de Desarrollo
5. **Sprint Planning**: Definir tareas granulares para la Fase 1 (MVP)
6. **Contratar Equipo**: Buscar Full-Stack Developer con experiencia en Next.js/React

### Mediano Plazo
7. **Desarrollo Fase 1**: Implementar MVP core (6 semanas)
8. **User Testing**: Validar con usuarios reales
9. **Iteración**: Ajustar según feedback

---

## 🛠️ Stack Tecnológico Recomendado

### Frontend
- **Framework**: Next.js 14+ (App Router)
- **UI Library**: React 18+
- **Styling**: Tailwind CSS + shadcn/ui
- **State**: Zustand + React Query
- **Charts**: Recharts

### Backend
- **Runtime**: Node.js 20+ / Bun
- **Framework**: Next.js API Routes / tRPC
- **Database**: PostgreSQL 15+ (Supabase)
- **ORM**: Prisma
- **Auth**: NextAuth.js / Clerk
- **Storage**: AWS S3 / Cloudinary

### DevOps
- **Hosting**: Vercel
- **CI/CD**: GitHub Actions
- **Monitoring**: Sentry
- **Analytics**: Posthog

---

## 📊 Métricas de Éxito

### KPIs Técnicos
- Tiempo de carga inicial: **< 2s**
- Time to Interactive: **< 3s**
- Uptime: **> 99.5%**
- Error rate: **< 0.5%**

### KPIs de Negocio
- Tiempo de setup de nuevo proyecto: **< 15 min**
- Precisión de presupuesto: **± 5%**
- Satisfacción de usuarios: **> 4.5/5**

---

## 👥 Roles y Permisos

| Funcionalidad | Gestor | Inversor | Viewer |
|---------------|:------:|:--------:|:------:|
| Ver propiedades/proyectos | ✅ | ✅ | ✅ |
| Crear/editar propiedades | ✅ | ❌ | ❌ |
| Ver finanzas | ✅ | ✅ | ❌ |
| Crear gastos | ✅ | ❌ | ❌ |
| Aprobar gastos >$5K | ❌ | ✅ | ❌ |
| Gestionar proveedores | ✅ | ❌ | ❌ |
| Generar reportes | ✅ | ✅ | ❌ |

---

## 💰 Presupuesto Estimado

### Desarrollo (3.5 meses)
- Full-Stack Developer: Por definir
- UI/UX Designer (part-time): Por definir
- QA Engineer (part-time): Por definir

### Infraestructura (mensual)
- Vercel Pro: $20/mes
- Supabase Pro: $25/mes
- Cloudinary: $0-89/mes
- Resend: $0-20/mes
- Sentry: $0-29/mes

**Total infraestructura**: ~$100-180/mes

---

## 📞 Contacto del Proyecto

**Socio Gestor**: Verona  
**Repositorio GitHub**: https://github.com/leomartire/Flipping  
**Documentación**: `/docs`

---

## 📝 Historial de Versiones

### v1.0 - Abril 2026
- Creación de documentación completa de arquitectura
- Modelo de datos ERD
- Diseño UI/UX con wireframes
- Plan de desarrollo detallado de 15 semanas

---

## ⚖️ Licencia y Uso

Esta documentación es propiedad de **Inversión Inmobiliaria - Buenos Aires** y está destinada exclusivamente para uso interno del proyecto.

**Confidencialidad**: Los documentos contienen información sensible del negocio y no deben ser compartidos fuera del equipo del proyecto sin autorización.

---

## 🔄 Contribuir

Para sugerir cambios o mejoras a esta documentación:

1. Crear un issue en GitHub describiendo la mejora
2. Hacer fork del repositorio
3. Crear una rama: `git checkout -b feature/mejora-docs`
4. Hacer commit de cambios: `git commit -m 'Mejora en sección X'`
5. Push a la rama: `git push origin feature/mejora-docs`
6. Crear Pull Request

---

## 🎓 Recursos Adicionales

### Para Aprender Next.js
- [Next.js Documentation](https://nextjs.org/docs)
- [Learn Next.js](https://nextjs.org/learn)

### Para Aprender Prisma
- [Prisma Documentation](https://www.prisma.io/docs)
- [Prisma Quickstart](https://www.prisma.io/docs/getting-started/quickstart)

### Para shadcn/ui
- [shadcn/ui Documentation](https://ui.shadcn.com)
- [Component Examples](https://ui.shadcn.com/examples)

---

*Documentación generada: Abril 2026*  
*Última actualización: 7 de Abril, 2026*  
*Mantenido por: Equipo de Desarrollo Flipping Management Tool*
