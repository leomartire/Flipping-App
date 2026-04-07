# 🏗️ Arquitectura de la Aplicación - Flipping Management Tool

## 📋 Índice
1. [Visión General](#visión-general)
2. [Stack Tecnológico](#stack-tecnológico)
3. [Arquitectura del Sistema](#arquitectura-del-sistema)
4. [Modelo de Datos](#modelo-de-datos)
5. [Módulos Funcionales](#módulos-funcionales)
6. [Flujos de Usuario](#flujos-de-usuario)
7. [Seguridad y Roles](#seguridad-y-roles)
8. [Plan de Implementación](#plan-de-implementación)

---

## 🎯 Visión General

### Propósito
Plataforma integral para la gestión de proyectos de flipping inmobiliario en CABA, permitiendo el seguimiento completo del ciclo de vida desde la identificación de propiedades hasta la venta final.

### Usuarios Principales
- **Socio Gestor (Verona)**: Control operativo total, gestión de propiedades, obras y proveedores
- **Socio Inversor**: Visualización de inversiones, ROI, reportes y aprobaciones

### Objetivos Clave
- ✅ Centralizar información de todos los proyectos de flipping
- ✅ Tracking financiero en tiempo real (USD)
- ✅ Control de obras y proveedores
- ✅ Generación automática de reportes para inversores
- ✅ Gestión documental (escrituras, contratos, permisos)

---

## 🛠️ Stack Tecnológico

### Frontend
```
Framework: Next.js 14+ (App Router)
Lenguaje: TypeScript
UI Library: React 18+
Styling: Tailwind CSS + shadcn/ui
Estado: Zustand / React Query
Gráficos: Recharts / Chart.js
Validación: Zod
Formularios: React Hook Form
```

### Backend
```
Runtime: Node.js 20+ / Bun
Framework: Next.js API Routes / tRPC
Base de Datos: PostgreSQL 15+ (Supabase / Railway)
ORM: Prisma
Autenticación: NextAuth.js / Clerk
Storage: AWS S3 / Cloudinary (documentos/imágenes)
Email: Resend / SendGrid
```

### DevOps & Infraestructura
```
Hosting: Vercel (Frontend + API)
Base de Datos: Supabase / Railway
CI/CD: GitHub Actions
Monitoreo: Sentry / LogRocket
Analytics: Posthog / Mixpanel
```

### Justificación del Stack
- **Next.js 14**: SSR, optimización automática, API routes integradas
- **TypeScript**: Type-safety crítico para datos financieros
- **PostgreSQL**: Integridad relacional para finanzas y auditoría
- **Vercel**: Deploy automático, edge functions, excelente DX
- **Supabase**: PostgreSQL + Auth + Storage + Real-time en una plataforma

---

## 🏛️ Arquitectura del Sistema

### Diagrama de Alto Nivel

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (Next.js)                    │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Gestor     │  │   Inversor   │  │    Admin     │  │
│  │  Dashboard   │  │  Dashboard   │  │   Panel      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│              API LAYER (Next.js API / tRPC)             │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Propiedades  │  │  Finanzas    │  │    Obras     │  │
│  │   Service    │  │   Service    │  │   Service    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Proveedores  │  │  Documentos  │  │   Reportes   │  │
│  │   Service    │  │   Service    │  │   Service    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  DATA LAYER (Prisma ORM)                │
├─────────────────────────────────────────────────────────┤
│                 PostgreSQL Database                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │Properties│ │ Projects │ │ Finances │ │ Documents│  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ Vendors  │ │  Tasks   │ │  Users   │ │  Audits  │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Arquitectura de Carpetas

```
flipping-app/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── (auth)/
│   │   │   ├── login/
│   │   │   └── register/
│   │   ├── (dashboard)/
│   │   │   ├── gestor/         # Gestor Dashboard
│   │   │   ├── inversor/       # Inversor Dashboard
│   │   │   └── layout.tsx
│   │   ├── api/                # API Routes
│   │   │   ├── properties/
│   │   │   ├── projects/
│   │   │   ├── finances/
│   │   │   ├── vendors/
│   │   │   └── reports/
│   │   └── layout.tsx
│   ├── components/             # Componentes React
│   │   ├── ui/                 # shadcn components
│   │   ├── properties/
│   │   ├── projects/
│   │   ├── finances/
│   │   └── shared/
│   ├── lib/                    # Utilidades
│   │   ├── db/                 # Prisma client
│   │   ├── utils/
│   │   └── validations/
│   ├── hooks/                  # Custom React Hooks
│   ├── store/                  # Zustand stores
│   ├── types/                  # TypeScript types
│   └── server/                 # Server-side logic
│       ├── services/
│       └── repositories/
├── prisma/
│   ├── schema.prisma
│   └── migrations/
├── public/
├── .env.local
├── next.config.js
├── tailwind.config.ts
└── package.json
```

---

## 💾 Modelo de Datos

### Entidades Principales

#### 1. **Users** (Usuarios)
```prisma
model User {
  id            String    @id @default(cuid())
  email         String    @unique
  name          String
  role          UserRole  @default(VIEWER)
  password      String    // Hashed
  avatar        String?
  phone         String?
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  
  projects      ProjectMember[]
  activities    Activity[]
}

enum UserRole {
  ADMIN         // Acceso total
  GESTOR        // Socio Gestor (Verona)
  INVERSOR      // Socio Inversor
  VIEWER        // Solo lectura
}
```

#### 2. **Properties** (Propiedades)
```prisma
model Property {
  id              String          @id @default(cuid())
  address         String
  neighborhood    Neighborhood
  propertyType    PropertyType
  rooms           Int             // Ambientes
  area            Float           // m²
  status          PropertyStatus  @default(PROSPECTING)
  
  // Datos de Compra
  askingPrice     Decimal         @db.Decimal(12, 2)
  purchasePrice   Decimal?        @db.Decimal(12, 2)
  purchaseDate    DateTime?
  
  // Valuación
  estimatedValue  Decimal?        @db.Decimal(12, 2)
  valuationDate   DateTime?
  
  // Metadata
  notes           String?
  images          String[]        // URLs de imágenes
  documents       Document[]
  
  createdAt       DateTime        @default(now())
  updatedAt       DateTime        @updatedAt
  createdBy       String
  
  project         Project?
}

enum Neighborhood {
  PALERMO_SOHO
  PALERMO_HOLLYWOOD
  BELGRANO_R
  BELGRANO_C
  VILLA_DEVOTO
  COLEGIALES
  CHACARITA
  RECOLETA
  CABALLITO
  OTROS
}

enum PropertyType {
  DEPARTAMENTO
  PH
  CASA
  LOCAL
}

enum PropertyStatus {
  PROSPECTING      // Búsqueda
  EVALUATING       // Evaluación
  NEGOTIATING      // Negociación
  PURCHASED        // Comprada
  IN_RENOVATION    // En obra
  STAGING          // Home Staging
  ON_SALE          // En venta
  SOLD             // Vendida
  ARCHIVED         // Archivada
}
```

#### 3. **Projects** (Proyectos de Flipping)
```prisma
model Project {
  id                String          @id @default(cuid())
  name              String
  code              String          @unique // ej: FLIP-001
  propertyId        String          @unique
  property          Property        @relation(fields: [propertyId], references: [id])
  
  status            ProjectStatus   @default(PLANNING)
  startDate         DateTime
  targetEndDate     DateTime
  actualEndDate     DateTime?
  
  // Presupuesto
  totalBudget       Decimal         @db.Decimal(12, 2)
  purchaseCost      Decimal         @db.Decimal(12, 2)
  renovationBudget  Decimal         @db.Decimal(12, 2)
  marketingBudget   Decimal         @db.Decimal(12, 2)
  taxesFees         Decimal         @db.Decimal(12, 2)
  
  // Proyección de Venta
  targetSalePrice   Decimal         @db.Decimal(12, 2)
  actualSalePrice   Decimal?        @db.Decimal(12, 2)
  saleDate          DateTime?
  
  // Calculados
  totalSpent        Decimal         @db.Decimal(12, 2) @default(0)
  profitMargin      Float?          // %
  roi               Float?          // %
  
  members           ProjectMember[]
  expenses          Expense[]
  tasks             Task[]
  vendors           ProjectVendor[]
  documents         Document[]
  timeline          Timeline[]
  
  createdAt         DateTime        @default(now())
  updatedAt         DateTime        @updatedAt
}

enum ProjectStatus {
  PLANNING
  IN_PROGRESS
  ON_HOLD
  COMPLETED
  CANCELLED
}

model ProjectMember {
  id          String   @id @default(cuid())
  projectId   String
  userId      String
  role        MemberRole
  
  project     Project  @relation(fields: [projectId], references: [id])
  user        User     @relation(fields: [userId], references: [id])
  
  @@unique([projectId, userId])
}

enum MemberRole {
  OWNER       // Gestor principal
  INVESTOR    // Inversor
  COLLABORATOR
}
```

#### 4. **Expenses** (Gastos)
```prisma
model Expense {
  id              String          @id @default(cuid())
  projectId       String
  project         Project         @relation(fields: [projectId], references: [id])
  
  category        ExpenseCategory
  subcategory     String?
  description     String
  amount          Decimal         @db.Decimal(12, 2)
  currency        Currency        @default(USD)
  
  vendorId        String?
  vendor          Vendor?         @relation(fields: [vendorId], references: [id])
  
  date            DateTime        @default(now())
  dueDate         DateTime?
  paymentStatus   PaymentStatus   @default(PENDING)
  paidDate        DateTime?
  
  invoiceNumber   String?
  receipt         String?         // URL del comprobante
  
  approvedBy      String?
  notes           String?
  
  createdAt       DateTime        @default(now())
  updatedAt       DateTime        @updatedAt
}

enum ExpenseCategory {
  PURCHASE          // Compra propiedad
  TAXES_FEES        // Impuestos y honorarios
  RENOVATION        // Remodelación
  MATERIALS         // Materiales
  LABOR             // Mano de obra
  PERMITS           // Permisos
  UTILITIES         // Servicios
  MARKETING         // Comercialización
  STAGING           // Home Staging
  MAINTENANCE       // Mantenimiento
  PROFESSIONAL      // Servicios profesionales
  OTHER
}

enum PaymentStatus {
  PENDING
  PARTIAL
  PAID
  OVERDUE
  CANCELLED
}

enum Currency {
  USD
  ARS
}
```

#### 5. **Vendors** (Proveedores)
```prisma
model Vendor {
  id              String          @id @default(cuid())
  name            String
  category        VendorCategory
  contactName     String?
  phone           String
  email           String?
  address         String?
  
  rating          Float?          // 1-5
  notes           String?
  
  expenses        Expense[]
  projects        ProjectVendor[]
  
  createdAt       DateTime        @default(now())
  updatedAt       DateTime        @updatedAt
}

enum VendorCategory {
  ARCHITECT
  CONTRACTOR
  PLUMBER
  ELECTRICIAN
  PAINTER
  MASON
  CARPENTER
  REALTOR
  LAWYER
  ACCOUNTANT
  STAGER
  PHOTOGRAPHER
  MATERIALS_SUPPLIER
  OTHER
}

model ProjectVendor {
  id          String   @id @default(cuid())
  projectId   String
  vendorId    String
  
  project     Project  @relation(fields: [projectId], references: [id])
  vendor      Vendor   @relation(fields: [vendorId], references: [id])
  
  contractValue Decimal? @db.Decimal(12, 2)
  notes       String?
  
  @@unique([projectId, vendorId])
}
```

#### 6. **Tasks** (Tareas de Obra)
```prisma
model Task {
  id              String      @id @default(cuid())
  projectId       String
  project         Project     @relation(fields: [projectId], references: [id])
  
  title           String
  description     String?
  category        TaskCategory
  priority        Priority    @default(MEDIUM)
  status          TaskStatus  @default(TODO)
  
  assignedTo      String?
  dueDate         DateTime?
  completedDate   DateTime?
  
  dependencies    String[]    // IDs de tareas dependientes
  
  photos          String[]    // URLs de fotos antes/después
  notes           String?
  
  createdAt       DateTime    @default(now())
  updatedAt       DateTime    @updatedAt
}

enum TaskCategory {
  DEMOLITION
  PLUMBING
  ELECTRICAL
  MASONRY
  PAINTING
  FLOORING
  CARPENTRY
  INSPECTION
  PERMITS
  STAGING
  PHOTOGRAPHY
  CLEANING
  OTHER
}

enum Priority {
  LOW
  MEDIUM
  HIGH
  URGENT
}

enum TaskStatus {
  TODO
  IN_PROGRESS
  BLOCKED
  REVIEW
  COMPLETED
}
```

#### 7. **Documents** (Documentos)
```prisma
model Document {
  id              String          @id @default(cuid())
  name            String
  type            DocumentType
  category        String?
  url             String
  size            Int?            // bytes
  
  propertyId      String?
  property        Property?       @relation(fields: [propertyId], references: [id])
  
  projectId       String?
  project         Project?        @relation(fields: [projectId], references: [id])
  
  uploadedBy      String
  uploadedAt      DateTime        @default(now())
  
  notes           String?
}

enum DocumentType {
  ESCRITURA
  BOLETO
  CONTRACT
  INVOICE
  RECEIPT
  PERMIT
  INSPECTION
  PHOTO
  FLOOR_PLAN
  RENDER
  OTHER
}
```

#### 8. **Timeline** (Línea de Tiempo)
```prisma
model Timeline {
  id          String      @id @default(cuid())
  projectId   String
  project     Project     @relation(fields: [projectId], references: [id])
  
  phase       Phase
  title       String
  startDate   DateTime
  endDate     DateTime?
  status      PhaseStatus @default(PENDING)
  
  notes       String?
  
  createdAt   DateTime    @default(now())
}

enum Phase {
  SOURCING
  DUE_DILIGENCE
  PURCHASE
  RENOVATION
  STAGING
  MARKETING
  SALE
  CLOSING
}

enum PhaseStatus {
  PENDING
  IN_PROGRESS
  COMPLETED
  DELAYED
}
```

#### 9. **Activity Log** (Auditoría)
```prisma
model Activity {
  id          String      @id @default(cuid())
  userId      String
  user        User        @relation(fields: [userId], references: [id])
  
  action      String      // ej: "created_project", "updated_expense"
  entityType  String      // ej: "Project", "Expense"
  entityId    String
  
  before      Json?       // Estado anterior
  after       Json?       // Estado nuevo
  
  ipAddress   String?
  userAgent   String?
  
  createdAt   DateTime    @default(now())
}
```

---

## 🎨 Módulos Funcionales

### 1. **Dashboard del Gestor**
**Componentes:**
- Resumen de proyectos activos
- Tareas pendientes prioritarias
- Alertas de presupuesto
- Próximos vencimientos de pagos
- Gráficos de progreso de obras
- Accesos rápidos a propiedades en pipeline

**Funcionalidades:**
- Vista kanban de propiedades por fase
- Calendario de tareas y milestones
- Notificaciones de eventos críticos
- Búsqueda rápida de propiedades/proyectos

### 2. **Dashboard del Inversor**
**Componentes:**
- Portfolio general (inversión total, ROI promedio)
- Proyectos activos con métricas clave
- Proyectos completados y rendimiento histórico
- Gráficos de distribución de capital
- Comparativa de ROI proyectado vs real
- Documentos importantes

**Funcionalidades:**
- Visualización de flujo de caja
- Reportes descargables (PDF/Excel)
- Vista detallada de cada proyecto
- Aprobación de gastos mayores (workflow)

### 3. **Gestión de Propiedades**
**Funcionalidades:**
- CRUD completo de propiedades
- Pipeline visual (Kanban/List view)
- Filtros avanzados (barrio, precio, m², estado)
- Subida de imágenes y documentos
- Historial de cambios de precio
- Comparación de propiedades
- Mapa de ubicaciones

### 4. **Gestión de Proyectos**
**Funcionalidades:**
- Creación de proyecto desde propiedad
- Timeline visual del proyecto
- Gestión de presupuesto por categoría
- Control de gastos reales vs presupuestados
- Asignación de equipo y roles
- Gestión de hitos (milestones)
- Dashboard de métricas del proyecto

### 5. **Control Financiero**
**Funcionalidades:**
- Registro de gastos con categorización
- Upload de comprobantes
- Flujo de aprobación de gastos
- Conciliación de pagos
- Reportes financieros por proyecto
- Cálculo automático de ROI
- Proyecciones de ganancia
- Alertas de desvío presupuestario

### 6. **Gestión de Obras**
**Funcionalidades:**
- Tablero Kanban de tareas
- Asignación de tareas a proveedores
- Seguimiento de progreso
- Upload de fotos de avance
- Gestión de dependencias entre tareas
- Cronograma Gantt
- Checklist de inspecciones

### 7. **Gestión de Proveedores**
**Funcionalidades:**
- Directorio de proveedores
- Calificación y reviews
- Historial de trabajos
- Contactos y notas
- Asignación a proyectos
- Análisis de desempeño

### 8. **Documentación**
**Funcionalidades:**
- Repositorio centralizado
- Categorización automática
- Búsqueda full-text
- Versionado de documentos
- Compartir con stakeholders
- Integración con Google Drive (opcional)

### 9. **Reportes y Analytics**
**Funcionalidades:**
- Dashboard de KPIs
- Reportes personalizables
- Exportación a PDF/Excel
- Comparativas entre proyectos
- Análisis de rentabilidad por barrio
- Tendencias de mercado
- Time-to-market promedio

---

## 👥 Flujos de Usuario

### Flujo 1: Identificación de Propiedad → Proyecto
```
1. Gestor agrega nueva propiedad (PROSPECTING)
2. Completa datos: dirección, barrio, m², precio
3. Sube fotos e información relevante
4. Cambia estado a EVALUATING
5. Registra valuación estimada y notas
6. Cambia estado a NEGOTIATING
7. Registra precio de compra acordado
8. Cambia estado a PURCHASED
9. Sistema crea automáticamente Proyecto
10. Gestor completa presupuesto detallado
11. Asigna miembros del equipo
12. Define timeline con hitos
```

### Flujo 2: Ejecución de Obra
```
1. Gestor crea tareas de obra en el proyecto
2. Asigna proveedores a cada tarea
3. Proveedores ejecutan trabajos
4. Gestor sube fotos de avance
5. Marca tareas como completadas
6. Registra gastos asociados
7. Sube comprobantes
8. Sistema actualiza presupuesto gastado
9. Alerta si hay desvío >10%
10. Inversor puede ver progreso en tiempo real
```

### Flujo 3: Registro de Gastos
```
1. Gestor crea nuevo gasto
2. Selecciona proyecto y categoría
3. Ingresa monto, descripción y proveedor
4. Sube foto del comprobante
5. Si gasto >$5000 USD → requiere aprobación
6. Inversor recibe notificación
7. Inversor aprueba/rechaza
8. Si aprobado → marca como PAID
9. Sistema actualiza métricas del proyecto
10. Gasto se refleja en reportes
```

### Flujo 4: Cierre de Venta
```
1. Propiedad cambia a ON_SALE
2. Gestor registra actividad de marketing
3. Recibe oferta de comprador
4. Registra precio de venta acordado
5. Cambia estado a SOLD
6. Ingresa fecha de escritura
7. Sistema calcula ROI final
8. Genera reporte de cierre automático
9. Distribuye utilidades según esquema 70/30
10. Cierra el proyecto
```

---

## 🔐 Seguridad y Roles

### Matriz de Permisos

| Funcionalidad | Gestor | Inversor | Viewer |
|---------------|:------:|:--------:|:------:|
| Ver todas las propiedades | ✅ | ✅ | ✅ |
| Crear/editar propiedades | ✅ | ❌ | ❌ |
| Eliminar propiedades | ✅ | ❌ | ❌ |
| Ver proyectos | ✅ | ✅ | ✅ |
| Crear/editar proyectos | ✅ | ❌ | ❌ |
| Ver finanzas | ✅ | ✅ | ❌ |
| Crear gastos | ✅ | ❌ | ❌ |
| Aprobar gastos >$5K | ❌ | ✅ | ❌ |
| Ver proveedores | ✅ | ✅ | ❌ |
| Gestionar proveedores | ✅ | ❌ | ❌ |
| Ver tareas | ✅ | ✅ | ❌ |
| Crear/editar tareas | ✅ | ❌ | ❌ |
| Ver documentos | ✅ | ✅ | ✅ |
| Subir documentos | ✅ | ✅ | ❌ |
| Generar reportes | ✅ | ✅ | ❌ |
| Ver activity log | ✅ | ✅ | ❌ |

### Seguridad Implementada
- Autenticación con JWT tokens
- Refresh tokens para sesiones persistentes
- Encriptación de contraseñas con bcrypt
- Rate limiting en API endpoints
- Validación de datos con Zod
- SQL injection protection (Prisma)
- XSS protection
- CORS configurado
- HTTPS obligatorio en producción
- Audit log completo de acciones
- 2FA opcional para inversores

---

## 📅 Plan de Implementación

### Fase 1: MVP Core (4-6 semanas)
**Objetivo:** Sistema funcional básico para gestión de 1-2 proyectos

**Entregables:**
- ✅ Setup inicial (Next.js + Prisma + Supabase)
- ✅ Autenticación (login/registro)
- ✅ CRUD de Propiedades
- ✅ CRUD de Proyectos
- ✅ Registro de Gastos básico
- ✅ Dashboard del Gestor (básico)
- ✅ Dashboard del Inversor (básico)
- ✅ Deploy en Vercel

**Sprints:**
```
Semana 1-2: Setup + Auth + Database
Semana 3: Módulo Propiedades
Semana 4: Módulo Proyectos
Semana 5: Módulo Finanzas
Semana 6: Dashboards + Testing + Deploy
```

### Fase 2: Funcionalidades Avanzadas (4 semanas)
**Objetivo:** Completar módulos de gestión operativa

**Entregables:**
- ✅ Gestión de Obras (Tareas + Timeline)
- ✅ Gestión de Proveedores
- ✅ Upload de Documentos (S3/Cloudinary)
- ✅ Sistema de Aprobaciones
- ✅ Notificaciones (Email + In-app)
- ✅ Reportes básicos (PDF)

**Sprints:**
```
Semana 7-8: Obras + Proveedores
Semana 9: Documentos + Storage
Semana 10: Aprobaciones + Notificaciones
```

### Fase 3: Analytics & UX (3 semanas)
**Objetivo:** Reportes avanzados y mejoras de experiencia

**Entregables:**
- ✅ Reportes personalizables
- ✅ Gráficos interactivos (Recharts)
- ✅ Búsqueda avanzada y filtros
- ✅ Vista de mapa de propiedades
- ✅ Mobile responsive completo
- ✅ Optimizaciones de performance

**Sprints:**
```
Semana 11: Analytics Dashboard
Semana 12: Búsqueda + Filtros
Semana 13: Mobile + Performance
```

### Fase 4: Integraciones & Automatización (2 semanas)
**Objetivo:** Conectar con servicios externos

**Entregables:**
- ✅ Integración con Google Drive (opcional)
- ✅ Webhooks para eventos clave
- ✅ API pública (para futuras integraciones)
- ✅ Backups automáticos
- ✅ Monitoreo y alertas (Sentry)

**Sprints:**
```
Semana 14: Integraciones
Semana 15: API + Monitoring
```

---

## 📊 Métricas de Éxito

### KPIs Técnicos
- Tiempo de carga inicial: <2s
- Time to Interactive: <3s
- Uptime: >99.5%
- Error rate: <0.5%
- API response time: <200ms p95

### KPIs de Negocio
- Tiempo de setup de nuevo proyecto: <15 min
- Precisión de presupuesto: ±5%
- Tiempo de generación de reporte: <10s
- Satisfacción de usuarios: >4.5/5

---

## 🔄 Próximos Pasos

1. **Validación de Arquitectura**: Revisar este documento con el equipo
2. **Refinamiento de Modelo de Datos**: Ajustar según necesidades específicas
3. **Diseño de UI/UX**: Crear wireframes y mockups
4. **Setup de Proyecto**: Inicializar repositorio y ambiente de desarrollo
5. **Sprint Planning**: Definir tareas detalladas para Fase 1

---

## 📞 Contacto del Proyecto

**Socio Gestor**: Verona  
**Repositorio**: https://github.com/leomartire/Flipping  
**Documentación**: `/docs`

---

*Documento creado: Abril 2026*  
*Versión: 1.0*
