# Diagrama Entidad-Relación - Flipping Management Tool

## Modelo de Datos Completo

```mermaid
erDiagram
    USERS ||--o{ PROJECT_MEMBERS : "participa en"
    USERS ||--o{ ACTIVITIES : "realiza"
    
    PROPERTIES ||--|| PROJECTS : "tiene"
    PROPERTIES ||--o{ DOCUMENTS : "contiene"
    
    PROJECTS ||--o{ PROJECT_MEMBERS : "tiene"
    PROJECTS ||--o{ EXPENSES : "genera"
    PROJECTS ||--o{ TASKS : "incluye"
    PROJECTS ||--o{ PROJECT_VENDORS : "contrata"
    PROJECTS ||--o{ DOCUMENTS : "almacena"
    PROJECTS ||--o{ TIMELINE : "sigue"
    
    VENDORS ||--o{ EXPENSES : "cobra"
    VENDORS ||--o{ PROJECT_VENDORS : "trabaja en"
    
    USERS {
        uuid id PK
        string email UK
        string name
        enum role "GESTOR, INVERSOR, VIEWER"
        string password
        string avatar
        string phone
        timestamp created_at
        timestamp updated_at
    }
    
    PROPERTIES {
        uuid id PK
        string address
        enum neighborhood "PALERMO, BELGRANO, etc"
        enum property_type "DEPARTAMENTO, PH, CASA"
        int rooms
        float area_m2
        enum status "PROSPECTING to SOLD"
        decimal asking_price
        decimal purchase_price
        date purchase_date
        decimal estimated_value
        date valuation_date
        string notes
        string_array images
        timestamp created_at
        timestamp updated_at
        uuid created_by FK
    }
    
    PROJECTS {
        uuid id PK
        string name
        string code UK "FLIP-001"
        uuid property_id FK
        enum status "PLANNING to COMPLETED"
        date start_date
        date target_end_date
        date actual_end_date
        decimal total_budget
        decimal purchase_cost
        decimal renovation_budget
        decimal marketing_budget
        decimal taxes_fees
        decimal target_sale_price
        decimal actual_sale_price
        date sale_date
        decimal total_spent
        float profit_margin
        float roi
        timestamp created_at
        timestamp updated_at
    }
    
    PROJECT_MEMBERS {
        uuid id PK
        uuid project_id FK
        uuid user_id FK
        enum role "OWNER, INVESTOR, COLLABORATOR"
    }
    
    EXPENSES {
        uuid id PK
        uuid project_id FK
        enum category "PURCHASE, RENOVATION, etc"
        string subcategory
        string description
        decimal amount
        enum currency "USD, ARS"
        uuid vendor_id FK
        date date
        date due_date
        enum payment_status "PENDING to PAID"
        date paid_date
        string invoice_number
        string receipt_url
        uuid approved_by FK
        string notes
        timestamp created_at
        timestamp updated_at
    }
    
    VENDORS {
        uuid id PK
        string name
        enum category "ARCHITECT, CONTRACTOR, etc"
        string contact_name
        string phone
        string email
        string address
        float rating
        string notes
        timestamp created_at
        timestamp updated_at
    }
    
    PROJECT_VENDORS {
        uuid id PK
        uuid project_id FK
        uuid vendor_id FK
        decimal contract_value
        string notes
    }
    
    TASKS {
        uuid id PK
        uuid project_id FK
        string title
        string description
        enum category "DEMOLITION to CLEANING"
        enum priority "LOW to URGENT"
        enum status "TODO to COMPLETED"
        uuid assigned_to FK
        date due_date
        date completed_date
        string_array dependencies
        string_array photos
        string notes
        timestamp created_at
        timestamp updated_at
    }
    
    DOCUMENTS {
        uuid id PK
        string name
        enum type "ESCRITURA to PHOTO"
        string category
        string url
        int size_bytes
        uuid property_id FK
        uuid project_id FK
        uuid uploaded_by FK
        timestamp uploaded_at
        string notes
    }
    
    TIMELINE {
        uuid id PK
        uuid project_id FK
        enum phase "SOURCING to CLOSING"
        string title
        date start_date
        date end_date
        enum status "PENDING to DELAYED"
        string notes
        timestamp created_at
    }
    
    ACTIVITIES {
        uuid id PK
        uuid user_id FK
        string action
        string entity_type
        uuid entity_id
        json before
        json after
        string ip_address
        string user_agent
        timestamp created_at
    }
```

## Enumeraciones Clave

### UserRole
- `ADMIN`: Acceso total al sistema
- `GESTOR`: Socio Gestor (Verona) - Control operativo
- `INVERSOR`: Socio Inversor - Visualización y aprobaciones
- `VIEWER`: Solo lectura

### PropertyStatus
- `PROSPECTING`: En búsqueda
- `EVALUATING`: Bajo evaluación
- `NEGOTIATING`: En negociación
- `PURCHASED`: Comprada
- `IN_RENOVATION`: En obra
- `STAGING`: Home staging
- `ON_SALE`: En venta
- `SOLD`: Vendida
- `ARCHIVED`: Archivada

### ProjectStatus
- `PLANNING`: Planificación inicial
- `IN_PROGRESS`: Proyecto activo
- `ON_HOLD`: En pausa
- `COMPLETED`: Completado
- `CANCELLED`: Cancelado

### ExpenseCategory
- `PURCHASE`: Compra de propiedad
- `TAXES_FEES`: Impuestos y honorarios
- `RENOVATION`: Remodelación general
- `MATERIALS`: Materiales de construcción
- `LABOR`: Mano de obra
- `PERMITS`: Permisos y habilitaciones
- `UTILITIES`: Servicios (luz, agua, gas)
- `MARKETING`: Comercialización y publicidad
- `STAGING`: Home staging y fotografía
- `MAINTENANCE`: Mantenimiento
- `PROFESSIONAL`: Servicios profesionales
- `OTHER`: Otros gastos

### VendorCategory
- `ARCHITECT`: Arquitecto
- `CONTRACTOR`: Contratista general
- `PLUMBER`: Plomero
- `ELECTRICIAN`: Electricista
- `PAINTER`: Pintor
- `MASON`: Albañil
- `CARPENTER`: Carpintero
- `REALTOR`: Inmobiliaria
- `LAWYER`: Abogado
- `ACCOUNTANT`: Contador
- `STAGER`: Home stager
- `PHOTOGRAPHER`: Fotógrafo
- `MATERIALS_SUPPLIER`: Proveedor de materiales
- `OTHER`: Otros

### TaskCategory
- `DEMOLITION`: Demolición
- `PLUMBING`: Plomería
- `ELECTRICAL`: Electricidad
- `MASONRY`: Albañilería
- `PAINTING`: Pintura
- `FLOORING`: Pisos
- `CARPENTRY`: Carpintería
- `INSPECTION`: Inspección
- `PERMITS`: Permisos
- `STAGING`: Staging
- `PHOTOGRAPHY`: Fotografía
- `CLEANING`: Limpieza
- `OTHER`: Otros

### Phase (Timeline)
- `SOURCING`: Búsqueda de propiedad
- `DUE_DILIGENCE`: Due diligence
- `PURCHASE`: Compra y escrituración
- `RENOVATION`: Remodelación
- `STAGING`: Home staging
- `MARKETING`: Comercialización
- `SALE`: Negociación de venta
- `CLOSING`: Cierre

## Relaciones Importantes

1. **Properties → Projects**: Una propiedad puede convertirse en UN proyecto
2. **Projects → Expenses**: Un proyecto tiene MUCHOS gastos
3. **Projects → Tasks**: Un proyecto tiene MUCHAS tareas
4. **Projects → ProjectMembers**: Un proyecto tiene miembros (Gestor + Inversor)
5. **Vendors → Expenses**: Un proveedor cobra por MUCHOS gastos
6. **Projects → ProjectVendors**: Muchos a muchos con vendors
7. **Users → Activities**: Auditoría completa de acciones

## Índices Recomendados

```sql
-- Performance indexes
CREATE INDEX idx_properties_status ON properties(status);
CREATE INDEX idx_properties_neighborhood ON properties(neighborhood);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_expenses_project ON expenses(project_id);
CREATE INDEX idx_expenses_date ON expenses(date);
CREATE INDEX idx_tasks_project_status ON tasks(project_id, status);
CREATE INDEX idx_activities_user_created ON activities(user_id, created_at);

-- Search indexes
CREATE INDEX idx_properties_address ON properties USING gin(to_tsvector('spanish', address));
CREATE INDEX idx_vendors_name ON vendors USING gin(to_tsvector('spanish', name));
```

## Constraints de Negocio

```sql
-- Una propiedad solo puede tener un proyecto activo
ALTER TABLE projects ADD CONSTRAINT unique_active_project_per_property 
  EXCLUDE USING gist (property_id WITH =) 
  WHERE (status IN ('PLANNING', 'IN_PROGRESS'));

-- Total spent no puede exceder total budget * 1.2
ALTER TABLE projects ADD CONSTRAINT check_budget_overrun 
  CHECK (total_spent <= total_budget * 1.2);

-- ROI calculation
ALTER TABLE projects ADD CONSTRAINT check_roi_calculation 
  CHECK (
    (actual_sale_price IS NULL AND roi IS NULL) OR
    (actual_sale_price IS NOT NULL AND roi = ((actual_sale_price - total_spent) / total_spent * 100))
  );
```

---

*Versión: 1.0 | Fecha: Abril 2026*
