# 📊 Modelo de Datos Pro - Flipping-App

## Diagrama Entidad-Relación (ERD)

```mermaid
erDiagram
    PROJECTS ||--o{ EXPENSES : "registra"
    PROJECTS ||--o{ PROJECT_MEMBERS : "tiene"
    VENDORS ||--o{ EXPENSES : "factura"
    EXPENSES ||--|| OCR_METADATA : "proviene de"

    PROJECTS {
        uuid id PK
        string name
        decimal purchase_price "Monto compra"
        decimal renovation_budget "Presupuesto obra"
        decimal total_spent "Calculado"
        enum status "PLANNING, IN_PROGRESS, SOLD"
    }

    EXPENSES {
        uuid id PK
        uuid project_id FK
        uuid vendor_id FK
        date date
        decimal amount
        string category "Materiales, Mano de Obra, Honorarios"
        string receipt_url "Link a la foto"
        boolean ocr_verified "Validado por Gestor"
    }

    OCR_METADATA {
        uuid expense_id PK/FK
        json raw_text "Texto extraído por IA"
        float confidence "Nivel de certeza"
        string processed_at
    }

    PROJECT_MEMBERS {
        uuid project_id FK
        uuid user_id FK
        decimal equity_contribution "Capital aportado"
        float share_percentage "% de ganancia"
    }
