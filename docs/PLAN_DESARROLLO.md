# Plan de Desarrollo - Flipping Management Tool

## 🎯 Objetivos del Proyecto

### Objetivo Principal
Crear una plataforma web integral para gestionar el ciclo completo de proyectos de flipping inmobiliario en CABA, optimizando la colaboración entre el Socio Gestor y el Socio Inversor.

### Objetivos Específicos
1. ✅ Centralizar toda la información de propiedades y proyectos
2. ✅ Automatizar el cálculo y seguimiento de ROI
3. ✅ Facilitar la transparencia financiera con el inversor
4. ✅ Optimizar la gestión de obras y proveedores
5. ✅ Generar reportes automáticos para stakeholders

---

## 📅 Timeline General del Proyecto

### Fase 1: MVP Core (6 semanas) - Abril - Mayo 2026
**Objetivo**: Sistema funcional básico para 1-2 proyectos

### Fase 2: Funcionalidades Avanzadas (4 semanas) - Junio 2026
**Objetivo**: Completar módulos operativos

### Fase 3: Analytics & UX (3 semanas) - Julio 2026
**Objetivo**: Reportes avanzados y optimización

### Fase 4: Integraciones (2 semanas) - Agosto 2026
**Objetivo**: Conectar con servicios externos

**Total: ~15 semanas (3.5 meses)**

---

## 📦 Fase 1: MVP Core (6 semanas)

### Semana 1-2: Setup + Autenticación + Database

#### Objetivos
- Inicializar proyecto Next.js con TypeScript
- Configurar base de datos PostgreSQL
- Implementar sistema de autenticación
- Setup de herramientas de desarrollo

#### Tareas Detalladas

**Día 1-3: Inicialización del Proyecto**
```bash
# Setup del proyecto
npx create-next-app@latest flipping-app --typescript --tailwind --app
cd flipping-app
npm install prisma @prisma/client zustand react-query zod react-hook-form
npm install -D @types/node

# Setup de Prisma
npx prisma init
```

```prisma
# prisma/schema.prisma - Esquema inicial
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

// Modelos básicos: User, Property, Project
```

**Día 4-6: Autenticación**
```bash
npm install next-auth @next-auth/prisma-adapter bcryptjs
npm install -D @types/bcryptjs
```

Implementar:
- [ ] NextAuth.js configuration
- [ ] Login page (`/app/(auth)/login`)
- [ ] Register page (`/app/(auth)/register`)
- [ ] Protected routes middleware
- [ ] Session management
- [ ] User roles (GESTOR, INVERSOR, VIEWER)

**Día 7-10: Database Setup**
```bash
# Setup Supabase project
# Get connection string
# Update .env.local

npx prisma migrate dev --name init
npx prisma generate
```

Implementar:
- [ ] Seed script con datos de ejemplo
- [ ] Database utilities (`/src/lib/db`)
- [ ] Prisma Client singleton
- [ ] Basic CRUD repositories

**Día 11-14: DevOps Inicial**
- [ ] Setup GitHub repository
- [ ] Configure Vercel project
- [ ] Environment variables setup
- [ ] First deployment (staging)
- [ ] CI/CD pipeline básico

#### Entregables Semana 1-2
✅ Proyecto Next.js configurado  
✅ Base de datos PostgreSQL con esquema inicial  
✅ Sistema de autenticación funcional  
✅ Deploy en Vercel (staging)  
✅ README.md con instrucciones de setup

---

### Semana 3: Módulo de Propiedades

#### Objetivos
- CRUD completo de propiedades
- Vista de pipeline (Kanban)
- Upload de imágenes

#### Tareas Detalladas

**Días 15-17: Backend**
```typescript
// src/app/api/properties/route.ts
export async function GET(request: Request) {
  // List properties with filters
}

export async function POST(request: Request) {
  // Create property
}

// src/app/api/properties/[id]/route.ts
export async function GET(params: { id: string }) {
  // Get property by ID
}

export async function PATCH(params: { id: string }) {
  // Update property
}

export async function DELETE(params: { id: string }) {
  // Soft delete property
}
```

Implementar:
- [ ] Properties API routes
- [ ] Zod validation schemas
- [ ] Image upload to Cloudinary/S3
- [ ] Filtering and search logic
- [ ] Status transitions validation

**Días 18-21: Frontend**
```typescript
// src/app/(dashboard)/gestor/propiedades/page.tsx
// Vista de pipeline Kanban
```

Implementar:
- [ ] Property list page (Kanban view)
- [ ] Property detail page
- [ ] Create property form
- [ ] Edit property form
- [ ] Image upload component
- [ ] Status badge component
- [ ] Filters sidebar

#### Entregables Semana 3
✅ CRUD de propiedades funcional  
✅ Vista Kanban del pipeline  
✅ Upload de imágenes  
✅ Búsqueda y filtros básicos

---

### Semana 4: Módulo de Proyectos

#### Objetivos
- Crear proyecto desde propiedad
- Vista detalle de proyecto
- Timeline básico

#### Tareas Detalladas

**Días 22-24: Backend**
```typescript
// src/app/api/projects/route.ts
// src/app/api/projects/[id]/route.ts
// src/app/api/projects/[id]/timeline/route.ts
```

Implementar:
- [ ] Projects API routes
- [ ] Create project from property
- [ ] Project status transitions
- [ ] Timeline phases management
- [ ] Budget calculations
- [ ] ROI calculations

**Días 25-28: Frontend**
```typescript
// src/app/(dashboard)/gestor/proyectos/[id]/page.tsx
// Vista detalle del proyecto con tabs
```

Implementar:
- [ ] Projects list page
- [ ] Project detail page (tabs: General, Finanzas, Obras, Docs, Timeline)
- [ ] Create project wizard
- [ ] Budget breakdown component
- [ ] Timeline visualization
- [ ] Progress bar component

#### Entregables Semana 4
✅ CRUD de proyectos  
✅ Conversión propiedad → proyecto  
✅ Vista detalle con timeline  
✅ Cálculo de ROI básico

---

### Semana 5: Módulo de Finanzas

#### Objetivos
- Registro de gastos
- Categorización
- Upload de comprobantes

#### Tareas Detalladas

**Días 29-31: Backend**
```typescript
// src/app/api/projects/[id]/expenses/route.ts
// src/app/api/expenses/[id]/route.ts
```

Implementar:
- [ ] Expenses API routes
- [ ] Category validation
- [ ] Budget tracking logic
- [ ] Alert system (budget overrun)
- [ ] Receipt upload
- [ ] Currency conversion (USD/ARS)

**Días 32-35: Frontend**
```typescript
// src/app/(dashboard)/gestor/proyectos/[id]/finanzas/page.tsx
```

Implementar:
- [ ] Expenses list view
- [ ] Create expense form
- [ ] Receipt upload
- [ ] Budget vs Actual chart
- [ ] Category breakdown (pie chart)
- [ ] Expense filters
- [ ] Alert notifications

#### Entregables Semana 5
✅ Registro de gastos funcional  
✅ Categorización automática  
✅ Upload de comprobantes  
✅ Alertas de presupuesto

---

### Semana 6: Dashboards + Testing + Deploy

#### Objetivos
- Dashboard del Gestor
- Dashboard del Inversor
- Testing end-to-end
- Production deploy

#### Tareas Detalladas

**Días 36-38: Dashboards**
```typescript
// src/app/(dashboard)/gestor/page.tsx
// src/app/(dashboard)/inversor/page.tsx
```

Implementar:
- [ ] Gestor dashboard con métricas clave
- [ ] Lista de proyectos activos
- [ ] Tareas pendientes
- [ ] Gastos por aprobar
- [ ] Inversor dashboard con portfolio
- [ ] ROI por proyecto
- [ ] Aprobaciones pendientes

**Días 39-40: Testing**
```bash
npm install -D @testing-library/react @testing-library/jest-dom jest
npm install -D @playwright/test
```

Implementar:
- [ ] Unit tests para utilidades
- [ ] Integration tests para API routes
- [ ] E2E tests para flujos críticos
- [ ] Test coverage report

**Días 41-42: Deploy y Documentación**
- [ ] Environment variables production
- [ ] Production deploy
- [ ] User acceptance testing
- [ ] Documentation update
- [ ] Video demo

#### Entregables Semana 6
✅ Dashboard Gestor funcional  
✅ Dashboard Inversor funcional  
✅ Test suite completo  
✅ Deploy en producción  
✅ Documentación actualizada

---

## 📦 Fase 2: Funcionalidades Avanzadas (4 semanas)

### Semana 7-8: Gestión de Obras y Proveedores

#### Objetivos
- Tablero Kanban de tareas
- Gestión de proveedores
- Asignación de tareas

#### Tareas

**Backend**
- [ ] Tasks API routes
- [ ] Vendors API routes
- [ ] Project-Vendors relationship
- [ ] Task dependencies logic

**Frontend**
- [ ] Tasks Kanban board (drag & drop)
- [ ] Task detail modal
- [ ] Vendors directory
- [ ] Vendor rating system
- [ ] Task assignment

#### Entregables
✅ Kanban de tareas funcional  
✅ CRUD de proveedores  
✅ Asignación de tareas  
✅ Historial de trabajos

---

### Semana 9: Documentos y Storage

#### Objetivos
- Upload de documentos
- Categorización
- Integración con S3/Cloudinary

#### Tareas

**Backend**
- [ ] Documents API routes
- [ ] S3/Cloudinary integration
- [ ] File type validation
- [ ] Virus scanning (ClamAV)

**Frontend**
- [ ] Document upload component
- [ ] Document viewer
- [ ] Category filters
- [ ] Search functionality

#### Entregables
✅ Sistema de documentos  
✅ Upload multi-archivo  
✅ Preview de documentos  
✅ Búsqueda full-text

---

### Semana 10: Sistema de Aprobaciones y Notificaciones

#### Objetivos
- Workflow de aprobación de gastos
- Notificaciones email + in-app

#### Tareas

**Backend**
- [ ] Approval workflow logic
- [ ] Email service integration (Resend)
- [ ] Notification system
- [ ] Webhook for events

**Frontend**
- [ ] Approval modal
- [ ] Notification center
- [ ] Email templates
- [ ] Real-time updates (polling/websocket)

#### Entregables
✅ Workflow de aprobaciones  
✅ Notificaciones email  
✅ Centro de notificaciones  
✅ Updates en tiempo real

---

## 📦 Fase 3: Analytics & UX (3 semanas)

### Semana 11: Analytics Dashboard

#### Objetivos
- KPIs avanzados
- Gráficos interactivos
- Comparativas

#### Tareas
- [ ] Analytics API endpoints
- [ ] Chart components (Recharts)
- [ ] ROI comparison charts
- [ ] Budget tracking charts
- [ ] Timeline gantt chart

#### Entregables
✅ Dashboard de analytics  
✅ Comparativa de proyectos  
✅ Gráficos interactivos

---

### Semana 12: Búsqueda y Filtros Avanzados

#### Objetivos
- Búsqueda full-text
- Filtros combinados
- Saved filters

#### Tareas
- [ ] Search API with PostgreSQL full-text
- [ ] Advanced filters UI
- [ ] Filter presets
- [ ] Export results (CSV/Excel)

#### Entregables
✅ Búsqueda full-text  
✅ Filtros avanzados  
✅ Export de datos

---

### Semana 13: Mobile Responsive + Performance

#### Objetivos
- Mobile responsive completo
- Optimizaciones de performance

#### Tareas
- [ ] Mobile layouts
- [ ] Touch gestures
- [ ] Image optimization
- [ ] Code splitting
- [ ] Lazy loading
- [ ] Lighthouse audit > 90

#### Entregables
✅ Mobile responsive  
✅ Performance optimizado  
✅ Lighthouse score > 90

---

## 📦 Fase 4: Integraciones (2 semanas)

### Semana 14: Integraciones Externas

#### Objetivos
- Google Drive (opcional)
- API pública

#### Tareas
- [ ] Google Drive API integration
- [ ] Public API documentation
- [ ] API rate limiting
- [ ] API authentication (API keys)

---

### Semana 15: Monitoring y Backups

#### Objetivos
- Monitoreo con Sentry
- Backups automáticos

#### Tareas
- [ ] Sentry integration
- [ ] Error tracking
- [ ] Performance monitoring
- [ ] Database backups (daily)
- [ ] Disaster recovery plan

---

## 🧪 Estrategia de Testing

### Unit Tests
```bash
npm run test:unit
```
- Utilities y helpers
- Validation schemas
- Business logic

### Integration Tests
```bash
npm run test:integration
```
- API routes
- Database operations
- External services

### E2E Tests (Playwright)
```bash
npm run test:e2e
```
- User flows completos
- Critical paths
- Cross-browser testing

### Coverage Goal
- **Statements**: >80%
- **Branches**: >75%
- **Functions**: >80%
- **Lines**: >80%

---

## 🚀 Estrategia de Deploy

### Environments

**Development**
- URL: `http://localhost:3000`
- Database: Local PostgreSQL
- Auto-reload on changes

**Staging**
- URL: `https://flipping-staging.vercel.app`
- Database: Supabase staging
- Deploy on PR merge to `develop`

**Production**
- URL: `https://flipping.app` (TBD)
- Database: Supabase production
- Deploy on PR merge to `main`
- Manual approval required

### CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/ci.yml
name: CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm run test
      - run: npm run lint
      - run: npm run build

  deploy-staging:
    needs: test
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}

  deploy-production:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
          vercel-args: '--prod'
```

---

## 📊 KPIs del Proyecto

### Métricas de Desarrollo
- **Velocity**: Story points por sprint
- **Bug Rate**: Bugs nuevos vs resueltos
- **Test Coverage**: % de código cubierto
- **Code Quality**: SonarQube score

### Métricas de Performance
- **Page Load**: < 2s
- **Time to Interactive**: < 3s
- **API Response Time**: < 200ms (p95)
- **Error Rate**: < 0.5%

### Métricas de Negocio
- **Time to Setup**: < 15 min para nuevo proyecto
- **User Satisfaction**: > 4.5/5
- **ROI Accuracy**: ±5% del real

---

## 🛠️ Stack de Desarrollo

### Core
- **Framework**: Next.js 14+ (App Router)
- **Language**: TypeScript 5+
- **Database**: PostgreSQL 15+ (Supabase)
- **ORM**: Prisma 5+

### Frontend
- **UI**: React 18+
- **Styling**: Tailwind CSS 3+
- **Components**: shadcn/ui
- **State**: Zustand + React Query
- **Forms**: React Hook Form + Zod
- **Charts**: Recharts

### Backend
- **API**: Next.js API Routes / tRPC
- **Auth**: NextAuth.js
- **Storage**: AWS S3 / Cloudinary
- **Email**: Resend

### DevOps
- **Hosting**: Vercel
- **CI/CD**: GitHub Actions
- **Monitoring**: Sentry
- **Analytics**: Posthog

---

## 👥 Equipo y Roles

### Necesidades del Proyecto

**Full-Stack Developer** (1-2)
- Next.js/React expertise
- TypeScript proficiency
- PostgreSQL/Prisma experience
- API design

**UI/UX Designer** (0.5 - part-time)
- Figma proficiency
- Design system creation
- User research

**QA Engineer** (0.5 - part-time)
- E2E testing
- Test automation
- Bug tracking

**DevOps** (consultoría)
- Vercel setup
- Database optimization
- Monitoring setup

---

## 💰 Presupuesto Estimado

### Desarrollo
- Full-Stack Developer (3.5 meses): $X
- UI/UX Designer (part-time): $Y
- QA Engineer (part-time): $Z

### Infraestructura (mensual)
- Vercel Pro: $20/mes
- Supabase Pro: $25/mes
- Cloudinary: $0-89/mes
- Resend: $0-20/mes
- Sentry: $0-29/mes

**Total infraestructura**: ~$100-180/mes

---

## 📚 Documentación

### Durante el Desarrollo
- [ ] README.md con setup instructions
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Component Storybook
- [ ] Database schema docs
- [ ] Deployment guide

### Post-Lanzamiento
- [ ] User manual (Gestor)
- [ ] User manual (Inversor)
- [ ] Video tutorials
- [ ] FAQ
- [ ] Troubleshooting guide

---

## 🎓 Capacitación

### Para el Equipo de Desarrollo
- Next.js 14 App Router workshop
- Prisma best practices
- Security training

### Para los Usuarios
- Onboarding session (2h)
- Video tutorials cortos (5-10 min cada uno)
- Support channel (Slack/Discord)

---

## 🔐 Consideraciones de Seguridad

### Implementar
- [ ] HTTPS obligatorio
- [ ] Password hashing (bcrypt)
- [ ] JWT tokens con expiración
- [ ] Rate limiting
- [ ] SQL injection protection (Prisma)
- [ ] XSS protection
- [ ] CSRF tokens
- [ ] Input validation (Zod)
- [ ] File upload validation
- [ ] Audit logging completo
- [ ] 2FA opcional

---

## 📝 Notas Finales

Este plan es un documento vivo que se actualizará según:
- Feedback de usuarios
- Cambios en requerimientos
- Descubrimientos técnicos
- Restricciones de presupuesto/tiempo

**Última actualización**: Abril 2026  
**Próxima revisión**: Final de Fase 1 (Mayo 2026)

---

*Documento creado para: Flipping Management Tool*  
*Cliente: Verona (Socio Gestor)*  
*Versión: 1.0*
