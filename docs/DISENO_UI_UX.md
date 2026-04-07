# Diseño UI/UX - Flipping Management Tool

## 🎨 Sistema de Diseño

### Paleta de Colores

#### Colores Primarios
```css
--primary-50:  #F0F9FF;
--primary-100: #E0F2FE;
--primary-500: #0EA5E9;
--primary-600: #0284C7;
--primary-700: #0369A1;
```

#### Colores Secundarios
```css
--secondary-50:  #F8FAFC;
--secondary-100: #F1F5F9;
--secondary-500: #64748B;
--secondary-600: #475569;
```

#### Colores Semánticos
```css
--success:  #10B981;
--warning:  #F59E0B;
--danger:   #EF4444;
--info:     #3B82F6;
```

#### Colores para Estados de Proyecto
```css
--prospecting:    #8B5CF6; /* Púrpura */
--evaluating:     #EC4899; /* Rosa */
--negotiating:    #F59E0B; /* Ámbar */
--purchased:      #3B82F6; /* Azul */
--in-renovation:  #F97316; /* Naranja */
--staging:        #14B8A6; /* Teal */
--on-sale:        #10B981; /* Verde */
--sold:           #6366F1; /* Índigo */
```

### Tipografía

```css
/* Font Family */
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;

/* Font Sizes */
--text-xs:   0.75rem;   /* 12px */
--text-sm:   0.875rem;  /* 14px */
--text-base: 1rem;      /* 16px */
--text-lg:   1.125rem;  /* 18px */
--text-xl:   1.25rem;   /* 20px */
--text-2xl:  1.5rem;    /* 24px */
--text-3xl:  1.875rem;  /* 30px */

/* Font Weights */
--font-normal:  400;
--font-medium:  500;
--font-semibold: 600;
--font-bold:    700;
```

### Espaciado

```css
--space-1:  0.25rem;  /* 4px */
--space-2:  0.5rem;   /* 8px */
--space-3:  0.75rem;  /* 12px */
--space-4:  1rem;     /* 16px */
--space-6:  1.5rem;   /* 24px */
--space-8:  2rem;     /* 32px */
--space-12: 3rem;     /* 48px */
```

### Bordes y Sombras

```css
--radius-sm: 0.25rem;  /* 4px */
--radius-md: 0.5rem;   /* 8px */
--radius-lg: 0.75rem;  /* 12px */
--radius-xl: 1rem;     /* 16px */

--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
```

---

## 📱 Diseños de Pantallas

### 1. Dashboard del Gestor

#### Layout General
```
┌─────────────────────────────────────────────────────────────┐
│  [Logo] Flipping Manager              [Notif] [Avatar] ▼   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  📊 Resumen General                                │    │
│  ├────────────┬────────────┬────────────┬────────────┤    │
│  │ Proyectos  │ Inversión  │ ROI Prom.  │ Propiedades│    │
│  │ Activos    │ Total      │            │ Pipeline   │    │
│  │    3       │ $845,000   │   18.5%    │     7      │    │
│  └────────────┴────────────┴────────────┴────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  🏗️ Proyectos Activos                              │    │
│  │                                              [+ New]│    │
│  ├────────────────────────────────────────────────────┤    │
│  │  FLIP-003: Palermo Soho                            │    │
│  │  ├─ Estado: En Obra (45%)  ███████░░░░░░░░░        │    │
│  │  ├─ Presupuesto: $75K / $82K ⚠️                    │    │
│  │  └─ Próximo: Inspección Eléctrica (2 días)        │    │
│  │                                                      │    │
│  │  FLIP-004: Belgrano R                              │    │
│  │  ├─ Estado: Staging (90%)  █████████████░░         │    │
│  │  ├─ Presupuesto: $58K / $60K ✓                     │    │
│  │  └─ Próximo: Sesión Fotos (Mañana)                │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─────────────────┐  ┌────────────────────────────┐      │
│  │ 📋 Tareas Hoy   │  │ 💰 Gastos Pendientes       │      │
│  ├─────────────────┤  ├────────────────────────────┤      │
│  │ □ Reunión arq.  │  │ Electricista | $3,200      │      │
│  │ ✓ Aprobar mat.  │  │ Vence: Hoy                 │      │
│  │ □ Visita obra   │  │                            │      │
│  │ □ Call inversor │  │ Pintura | $8,500           │      │
│  └─────────────────┘  │ Vence: 3 días              │      │
│                        └────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

#### Componentes Clave

**Card de Proyecto Activo**
```tsx
interface ProjectCard {
  code: string;           // FLIP-003
  name: string;           // Palermo Soho
  status: ProjectStatus;
  progress: number;       // 0-100
  budget: {
    spent: number;
    total: number;
    alertLevel: 'ok' | 'warning' | 'danger';
  };
  nextMilestone: {
    title: string;
    daysUntil: number;
  };
}
```

**Metric Card**
```tsx
interface MetricCard {
  label: string;
  value: string | number;
  change?: {
    value: number;
    direction: 'up' | 'down';
    period: string;
  };
  icon?: ReactNode;
}
```

### 2. Dashboard del Inversor

#### Layout General
```
┌─────────────────────────────────────────────────────────────┐
│  [Logo] Flipping Manager              [Notif] [Avatar] ▼   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  💼 Mi Portfolio                                    │    │
│  ├─────────────┬──────────────┬────────────────────┤        │
│  │ Capital     │ Proyectos    │ ROI Promedio        │        │
│  │ Invertido   │ Activos      │                     │        │
│  │ $400,000    │      3       │     21.3%           │        │
│  └─────────────┴──────────────┴────────────────────┘        │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  📈 Rendimiento por Proyecto                       │    │
│  │                                                      │    │
│  │  ┌─────────────────────────────────────────────┐  │    │
│  │  │                                              │  │    │
│  │  │     ROI Chart (Bar Chart)                    │  │    │
│  │  │     FLIP-001: 24.5% ████████████             │  │    │
│  │  │     FLIP-002: 19.8% ██████████               │  │    │
│  │  │     FLIP-003: 18.2% (proyectado)             │  │    │
│  │  │                                              │  │    │
│  │  └─────────────────────────────────────────────┘  │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌───────────────────────┐  ┌──────────────────────┐      │
│  │ ⚠️ Requiere Aprobación│  │ 📄 Reportes          │      │
│  ├───────────────────────┤  ├──────────────────────┤      │
│  │ Gasto Excepcional     │  │ • Reporte Mensual    │      │
│  │ Materiales Premium    │  │ • Balance Trimestral │      │
│  │ $12,500 USD           │  │ • Estado Proyectos   │      │
│  │                       │  │                      │      │
│  │ [Aprobar] [Rechazar]  │  │ [Generar PDF]        │      │
│  └───────────────────────┘  └──────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

### 3. Vista de Pipeline de Propiedades (Kanban)

```
┌─────────────────────────────────────────────────────────────┐
│  📍 Pipeline de Propiedades                  [+ Nueva] [⚙️] │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐   │
│  │Búsque-│  │Evalua-│  │Negoci-│  │Compra-│  │En Obra│   │
│  │da (4) │  │ción(2)│  │ción(1)│  │da (3) │  │  (2)  │   │
│  ├───────┤  ├───────┤  ├───────┤  ├───────┤  ├───────┤   │
│  │       │  │       │  │       │  │       │  │       │   │
│  │ ┌───┐ │  │ ┌───┐ │  │ ┌───┐ │  │ ┌───┐ │  │ ┌───┐ │   │
│  │ │🏢 │ │  │ │🏢 │ │  │ │🏢 │ │  │ │🏢 │ │  │ │🏢 │ │   │
│  │ │Pal│ │  │ │Bel│ │  │ │Rec│ │  │ │Pal│ │  │ │Col│ │   │
│  │ │erm│ │  │ │gra│ │  │ │ole│ │  │ │erm│ │  │ │egi│ │   │
│  │ │o  │ │  │ │no │ │  │ │ta │ │  │ │o  │ │  │ │ale│ │   │
│  │ │   │ │  │ │   │ │  │ │   │ │  │ │   │ │  │ │s  │ │   │
│  │ │95m²│ │  ││110m│ │  │ │85m│ │  ││105m│ │  │ │92m│ │   │
│  │ │$245│ │  │ │$28│ │  │ │$19│ │  │ │$26│ │  │ │$21│ │   │
│  │ │K  │ │  │ │0K │ │  │ │5K │ │  │ │0K │ │  │ │5K │ │   │
│  │ └───┘ │  │ └───┘ │  │ └───┘ │  │ └───┘ │  │ └───┘ │   │
│  │       │  │       │  │       │  │       │  │       │   │
│  └───────┘  └───────┘  └───────┘  └───────┘  └───────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### Card de Propiedad
```tsx
interface PropertyCard {
  id: string;
  address: string;
  neighborhood: Neighborhood;
  area: number;           // m²
  rooms: number;
  price: number;
  status: PropertyStatus;
  images: string[];
  notes?: string;
  valuationDate?: Date;
}
```

### 4. Vista Detalle de Proyecto

```
┌─────────────────────────────────────────────────────────────┐
│  ← FLIP-003: Palermo Soho 3 Amb                  [Editar]   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [General] [Finanzas] [Obras] [Docs] [Timeline]            │
│  ━━━━━━━━                                                   │
│                                                              │
│  ┌─────────────────────┐  ┌──────────────────────────┐    │
│  │ 📊 Métricas Clave   │  │ 📍 Información           │    │
│  ├─────────────────────┤  ├──────────────────────────┤    │
│  │ Estado: En Obra     │  │ Dirección: Gorriti 4580  │    │
│  │ Progreso: 45%       │  │ Barrio: Palermo Soho     │    │
│  │ ███████░░░░░░░░░    │  │ Superficie: 95 m²        │    │
│  │                     │  │ Ambientes: 3             │    │
│  │ Presupuesto         │  │ Compra: $260,000         │    │
│  │ $75K / $82K ⚠️      │  │ Fecha: 15/01/2026        │    │
│  │                     │  │                          │    │
│  │ ROI Proyectado      │  │ Equipo                   │    │
│  │ 22.5%               │  │ 👤 Verona (Gestor)       │    │
│  │                     │  │ 👤 XXX (Inversor)        │    │
│  └─────────────────────┘  └──────────────────────────┘    │
│                                                              │
│  ┌──────────────────────────────────────────────────┐      │
│  │ 📅 Timeline del Proyecto                          │      │
│  ├──────────────────────────────────────────────────┤      │
│  │                                                    │      │
│  │  ✓ Compra          15/01 - 22/01                  │      │
│  │  ✓ Demolición      23/01 - 30/01                  │      │
│  │  → Obra Gruesa     01/02 - 15/03  [65% completo]  │      │
│  │  ○ Terminaciones   16/03 - 10/04                  │      │
│  │  ○ Staging         11/04 - 20/04                  │      │
│  │  ○ Venta           21/04 - 30/05                  │      │
│  │                                                    │      │
│  └──────────────────────────────────────────────────┘      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 5. Vista de Finanzas del Proyecto

```
┌─────────────────────────────────────────────────────────────┐
│  FLIP-003: Palermo Soho > Finanzas                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Distribución del Presupuesto                       │    │
│  │                                                      │    │
│  │  ┌────────────────────────────────────────────┐    │    │
│  │  │                Pie Chart                    │    │    │
│  │  │   Compra: $260K (68%)                       │    │    │
│  │  │   Remodelación: $75K (20%)                  │    │    │
│  │  │   Marketing: $15K (4%)                      │    │    │
│  │  │   Impuestos: $32K (8%)                      │    │    │
│  │  └────────────────────────────────────────────┘    │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Gastos Recientes                      [+ Nuevo]   │    │
│  ├────────────────────────────────────────────────────┤    │
│  │                                                      │    │
│  │  Fecha    │ Categoría  │ Proveedor    │ Monto      │    │
│  │  ────────┼────────────┼──────────────┼──────────  │    │
│  │  04/04   │ Materiales │ CasaFerro    │ $3,200 ✓   │    │
│  │  02/04   │ Mano Obra  │ Constructora │ $8,500 ⏱   │    │
│  │  28/03   │ Electricidad│ ElectroPro  │ $4,100 ✓   │    │
│  │  25/03   │ Plomería   │ PlumberMax   │ $2,800 ✓   │    │
│  │                                                      │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─────────────────┐  ┌──────────────────────────┐        │
│  │ Total Gastado   │  │ Margen Disponible        │        │
│  │ $75,200         │  │ $6,800 (8.2%)            │        │
│  │ de $82,000      │  │                          │        │
│  └─────────────────┘  └──────────────────────────┘        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 6. Vista de Tareas (Kanban de Obras)

```
┌─────────────────────────────────────────────────────────────┐
│  FLIP-003: Palermo Soho > Obras y Tareas                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │ Por     │  │ En      │  │ Revisión│  │ Comple- │       │
│  │ Hacer(5)│  │ Progreso│  │   (2)   │  │ tadas   │       │
│  │         │  │   (3)   │  │         │  │  (12)   │       │
│  ├─────────┤  ├─────────┤  ├─────────┤  ├─────────┤       │
│  │         │  │         │  │         │  │         │       │
│  │ ┌─────┐ │  │ ┌─────┐ │  │ ┌─────┐ │  │ ┌─────┐ │       │
│  │ │ 🎨  │ │  │ │ ⚡  │ │  │ │ 🚰  │ │  │ │ 🔨  │ │       │
│  │ │Paint│ │  │ │Elec │ │  │ │Plom │ │  │ │Demo │ │       │
│  │ │Livng│ │  │ │Inst │ │  │ │Insp │ │  │ │lish │ │       │
│  │ │Room │ │  │ │all  │ │  │ │     │ │  │ │     │ │       │
│  │ │     │ │  │ │     │ │  │ │     │ │  │ │     │ │       │
│  │ │Due: │ │  │ │60%  │ │  │ │Pend │ │  │ │Done │ │       │
│  │ │8 Apr│ │  │ │     │ │  │ │Aprob│ │  │ │     │ │       │
│  │ │     │ │  │ │     │ │  │ │     │ │  │ │     │ │       │
│  │ │👷Jua│ │  │ │👷Mar│ │  │ │👷Lui│ │  │ │👷Jua│ │       │
│  │ │n    │ │  │ │cos  │ │  │ │s    │ │  │ │n    │ │       │
│  │ └─────┘ │  │ └─────┘ │  │ └─────┘ │  │ └─────┘ │       │
│  │         │  │         │  │         │  │         │       │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧩 Componentes Reutilizables

### Button Component

```tsx
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
  size: 'sm' | 'md' | 'lg';
  children: ReactNode;
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  isLoading?: boolean;
  disabled?: boolean;
  onClick?: () => void;
}

// Ejemplo de uso
<Button variant="primary" size="md" leftIcon={<PlusIcon />}>
  Nuevo Proyecto
</Button>
```

### Card Component

```tsx
interface CardProps {
  title?: string;
  subtitle?: string;
  actions?: ReactNode;
  children: ReactNode;
  className?: string;
}

// Ejemplo de uso
<Card 
  title="Proyectos Activos" 
  actions={<Button variant="ghost">Ver todos</Button>}
>
  {content}
</Card>
```

### Metric Card Component

```tsx
interface MetricCardProps {
  label: string;
  value: string | number;
  icon?: ReactNode;
  trend?: {
    value: number;
    direction: 'up' | 'down';
    isPositive?: boolean;
  };
  color?: 'primary' | 'success' | 'warning' | 'danger';
}

// Ejemplo de uso
<MetricCard 
  label="ROI Promedio"
  value="21.3%"
  trend={{ value: 3.5, direction: 'up', isPositive: true }}
  icon={<TrendingUpIcon />}
  color="success"
/>
```

### Status Badge Component

```tsx
interface StatusBadgeProps {
  status: PropertyStatus | ProjectStatus | TaskStatus | PaymentStatus;
  size?: 'sm' | 'md';
}

// Mapeo de colores por estado
const statusColors = {
  // Properties
  PROSPECTING: 'purple',
  EVALUATING: 'pink',
  NEGOTIATING: 'amber',
  PURCHASED: 'blue',
  IN_RENOVATION: 'orange',
  STAGING: 'teal',
  ON_SALE: 'green',
  SOLD: 'indigo',
  
  // Projects
  PLANNING: 'gray',
  IN_PROGRESS: 'blue',
  ON_HOLD: 'amber',
  COMPLETED: 'green',
  CANCELLED: 'red',
};
```

### Progress Bar Component

```tsx
interface ProgressBarProps {
  value: number;        // 0-100
  max?: number;
  label?: string;
  showPercentage?: boolean;
  color?: 'primary' | 'success' | 'warning' | 'danger';
  size?: 'sm' | 'md' | 'lg';
}

// Ejemplo de uso
<ProgressBar 
  value={65} 
  label="Progreso de Obra"
  showPercentage
  color="primary"
/>
```

---

## 📐 Patrones de Interacción

### Modal de Confirmación
- Usarlo para acciones destructivas (eliminar proyecto, cancelar obra)
- Título claro de la acción
- Descripción de consecuencias
- Botones: "Cancelar" (secundario) + "Confirmar" (peligro)

### Toast Notifications
- **Success**: Verde, auto-cierre 3s
- **Error**: Rojo, auto-cierre 5s
- **Warning**: Ámbar, auto-cierre 4s
- **Info**: Azul, auto-cierre 3s

### Formularios
- Validación en tiempo real
- Mensajes de error debajo del campo
- Required fields marcados con asterisco
- Submit deshabilitado si hay errores
- Loading state en el botón de submit

### Tablas
- Paginación: 10, 25, 50, 100 items
- Ordenamiento por columna (asc/desc)
- Filtros en header
- Acciones de fila: [...] menú contextual
- Selección múltiple con checkbox

---

## 📱 Responsive Design

### Breakpoints

```css
--mobile:  640px;   /* sm */
--tablet:  768px;   /* md */
--laptop:  1024px;  /* lg */
--desktop: 1280px;  /* xl */
```

### Mobile First Approach

```tsx
// Stack cards verticalmente en mobile
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <MetricCard ... />
  <MetricCard ... />
  <MetricCard ... />
</div>

// Sidebar colapsable en mobile
<aside className="hidden lg:block w-64">
  {sidebar}
</aside>

// Table responsive con scroll horizontal
<div className="overflow-x-auto">
  <table className="min-w-full">
    ...
  </table>
</div>
```

---

## ♿ Accesibilidad (WCAG 2.1 AA)

### Contraste de Colores
- Textos principales: ratio mínimo 4.5:1
- Textos grandes (18px+): ratio mínimo 3:1
- Elementos interactivos: ratio mínimo 3:1

### Navegación por Teclado
- Todos los elementos interactivos deben ser accesibles con Tab
- Focus visible en todos los elementos
- Escape para cerrar modales
- Enter/Space para activar botones

### Screen Readers
- Alt text en todas las imágenes
- ARIA labels en iconos sin texto
- ARIA live regions para notificaciones
- Semantic HTML (nav, main, aside, footer)

---

## 🎭 Animaciones y Transiciones

### Principios
- Duración: 150-300ms para interacciones rápidas
- Easing: ease-in-out para la mayoría
- Reducir animaciones en prefers-reduced-motion

### Ejemplos

```css
/* Hover en botones */
.button {
  transition: all 150ms ease-in-out;
}

.button:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

/* Fade in de cards */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.card {
  animation: fadeIn 300ms ease-out;
}

/* Loading spinner */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.spinner {
  animation: spin 1s linear infinite;
}
```

---

## 📊 Gráficos y Visualizaciones

### Chart.js / Recharts

**ROI por Proyecto (Bar Chart)**
```tsx
<BarChart data={projects}>
  <XAxis dataKey="code" />
  <YAxis />
  <Bar dataKey="roi" fill="#0EA5E9" />
  <Tooltip />
</BarChart>
```

**Distribución Presupuesto (Pie Chart)**
```tsx
<PieChart>
  <Pie 
    data={budgetBreakdown}
    dataKey="amount"
    nameKey="category"
    cx="50%"
    cy="50%"
  />
  <Tooltip />
  <Legend />
</PieChart>
```

**Timeline de Gastos (Line Chart)**
```tsx
<LineChart data={monthlyExpenses}>
  <XAxis dataKey="month" />
  <YAxis />
  <Line type="monotone" dataKey="amount" stroke="#10B981" />
  <Tooltip />
</LineChart>
```

---

*Documento creado: Abril 2026*  
*Versión: 1.0*  
*Figma / Diseño de Referencia: TBD*
