# 📊 Modelo de Datos Pro - Flipping-App

## 1. Diagrama Entidad-Relación (ERD)

Este diagrama representa la arquitectura lógica del sistema, optimizado para la Fase 3 de Refinamiento Financiero.

```mermaid
erDiagram
    PROJECTS ||--o{ EXPENSES : "registra"
    PROJECTS ||--o{ PROJECT_MEMBERS : "tiene"
    VENDORS ||--o{ EXPENSES : "factura"
    EXPENSES ||--|| OCR_METADATA : "proviene_de"

    PROJECTS {
        uuid id PK
        string name "Nombre de la propiedad"
        decimal purchase_price "Costo adquisición USD"
        decimal renovation_budget "Presupuesto obra aprobado"
        decimal estimated_sale_price "Precio venta proyectado"
        string currency "Moneda base (USD/ARS)"
        string status "PLANNING | IN_PROGRESS | SOLD | LIQUIDATED"
    }

    EXPENSES {
        uuid id PK
        uuid project_id FK
        uuid vendor_id FK
        string vendor_name "Nombre del Proveedor"
        string invoice_num "Número de Factura/Ticket"
        date invoice_date
        string invoice_currency "Moneda del comprobante (USD/ARS)"
        decimal invoice_amount "Monto en moneda original"
        decimal invoice_exchange_rate "TC para conversión a base"
        string category "Materiales | Mano de Obra | Tasas | etc"
        string payment_type "Efectivo | Transferencia | Tarjeta"
        string receipt_url "Link a la evidencia física"
        string additional_comments "Comentarios"    
        boolean manual_verified "Validación por Socio Gestor"
    }

    PROJECT_MEMBERS {
        uuid project_id FK
        uuid user_id FK
        string member_Fullname "Nombre del Miembro"
        string role "GESTOR | INVERSOR"
        decimal equity_contribution "Capital real aportado"
        float share_percentage "% Participación en ganancias"
    }

    VENDORS {
        uuid id PK
        string name
        string tax_id "CUIT/CUIL"
        string category "Rubro principal"
    }

    OCR_METADATA {
        uuid expense_id PK
        string raw_text "Texto crudo para auditoría"
        float confidence "Nivel de certeza IA"
        datetime processed_at
    }
