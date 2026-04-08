# 📊 Modelo de Datos Pro - Flipping-App

## Diagrama Entidad-Relación (ERD)

```mermaid
erDiagram
    PROJECTS ||--o{ EXPENSES : "registra"
    PROJECTS ||--o{ PROJECT_MEMBERS : "tiene"
    VENDORS ||--o{ EXPENSES : "factura"
    EXPENSES ||--|| OCR_METADATA : "proviene_de"

    PROJECTS {
        uuid id PK
        string name
        decimal purchase_price
        decimal renovation_budget
        decimal total_spent
        string status
    }

    EXPENSES {
        uuid id PK
        uuid project_id FK
        uuid vendor_id FK
        date date
        decimal amount
        string category
        string receipt_url
        boolean ocr_verified
    }

    OCR_METADATA {
        uuid expense_id PK
        string raw_text
        float confidence
        string processed_at
    }

    PROJECT_MEMBERS {
        uuid id FK
        uuid user_id FK
        decimal equity_contribution
        float share_percentage
    }
