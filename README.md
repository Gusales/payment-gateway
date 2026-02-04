# 💳 Payment Gateway API

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker)
![Architecture](https://img.shields.io/badge/Architecture-Clean%2FModular-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

> **Simulation of a robust and resilient Payment Gateway.**
>
> This project implements an intermediary API capable of processing financial transactions, ensuring **idempotency**, rigorous data validation, and intelligent routing between multiple acquirers (mocking providers like Stone/Cielo).

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Architecture & Design](#-architecture--design)
- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [How to Run](#-how-to-run)
- [Project Structure](#-project-structure)

---

## 💡 About the Project

The goal of this technical challenge is to demonstrate advanced Software Engineering skills focused on the back-end. The system solves real-world payment processing problems, such as:
1.  **Double Charge Prevention:** Uses idempotency keys to prevent network failures from causing duplicate charges.
2.  **High Availability:** Implements a *failover* strategy (if one provider fails, another takes over).
3.  **Maintainability:** Decoupled code allowing for database or provider swaps without affecting business logic.

---

## 🏗 Architecture & Design

The project follows **Clean Architecture** principles, dividing the application into isolated layers to protect Business Rules from infrastructure details.

### Conceptual Layers
*(See the full diagram in `/docs/architecture/c4_model.png`)*

1.  **Domain (Core):** Contains Entities (`Transaction`, `CreditCard`) and pure Business Rules. No external library dependencies.
2.  **Use Cases (Application):** Orchestrates the data flow (e.g., `ProcessPayment`). It interacts with repositories, validates data, and calls the gateway.
3.  **Infrastructure (Adapters):** Concrete implementations of Databases (Postgres/SQLAlchemy), Cache (Redis), and Integrations (StoneProvider, CieloProvider).
4.  **Entrypoints (Presentation):** The layer that handles external requests. In this case, **FastAPI** controllers.

---

## 🚀 Tech Stack

-   **Language:** Python 3.11+
-   **Web Framework:** FastAPI (High performance & automatic validation)
-   **Server:** Uvicorn
-   **Database:** PostgreSQL (Persistence) & Redis (Cache/Idempotency)
-   **Validation:** Pydantic V2
-   **Containerization:** Docker & Docker Compose
-   **Testing:** Pytest (Unit & E2E)
-   **Linter/Formatter:** Ruff

---

## ✨ Key Features

| Feature | Description | Status |
| :--- | :--- | :---: |
| **Process Payment** | Receives card data and routes it to the acquirer. | ✅ |
| **Idempotency** | Ensures requests with the same `Idempotency-Key` are processed only once. | ✅ |
| **Strict Validation** | Prevents negative values, expired cards, or invalid formats. | ✅ |
| **Multi-Provider** | Supports multiple acquirers via Dependency Injection. | ✅ |
| **Auto Fallback** | Retries with a secondary provider if the primary times out (Simulated). | 🚧 |

---

## ⚡ How to Run

### Prerequisites
-   [Docker](https://www.docker.com/) and Docker Compose installed.

### Step-by-Step

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/payment-gateway.git](https://github.com/your-username/payment-gateway.git)
    cd payment-gateway
    ```

2.  **Configure environment variables:**
    ```bash
    cp .env.example .env
    ```

3.  **Spin up the environment with Docker:**
    ```bash
    docker-compose up --build
    ```
    *This starts the API, Database, and Redis.*

4.  **Access the Interactive Docs:**
    Open your browser at: `http://localhost:8000/docs`

### Running Tests
To run unit and integration tests inside the container:
```bash
docker-compose run --rm app pytest
```

### 📁 Project Structure
This project uses a Colocated Testing strategy for unit tests (keeping tests next to the logic) and a root folder for E2E tests.

```
payment-gateway/
│
├── .github/                    
│   └── workflows/
│       └── ci.yml              # CI Pipeline (Lint/Test)
│
├── app/                        # SOURCE CODE + UNIT TESTS
│   ├── __init__.py
│   ├── main.py                 # App Entrypoint
│   ├── config.py               # Environment Variables (pydantic-settings)
│   │
│   ├── domain/                 # Layer 1: Pure Business Logic
│   │   ├── __init__.py
│   │   ├── models.py           
│   │   ├── test_models.py      
│   │   ├── exceptions.py       
│   │   └── interfaces.py       
│   │
│   ├── use_cases/              # Layer 2: Application Logic
│   │   ├── __init__.py
│   │   ├── process_payment.py  
│   │   └── test_process_payment.py 
│   │
│   ├── infrastructure/         # Layer 3: Adapters & External World
│   │   ├── db/                 
│   │   ├── repositories/       
│   │   │   ├── transaction_repo.py
│   │   │   └── test_transaction_repo.py 
│   │   ├── providers/          
│   │   │   ├── stone.py
│   │   │   ├── test_stone.py  
│   │   │   ├── cielo.py
│   │   │   └── test_cielo.py   
│   │   └── cache/              
│   │
│   └── entrypoints/            # Layer 4: Presentation
│       └── api/
│           ├── endpoints.py    
│           ├── test_endpoints.py 
│           ├── schemas.py      
│           └── middlewares.py  
│
├── docs/                       # Documentation & Diagrams
├── tests/                      # E2E / INTEGRATION TESTS ONLY
│   ├── __init__.py
│   ├── conftest.py             # Global Pytest Config (DB/Client Fixtures)
│   └── e2e/                    
│       └── test_transaction_flow.py # 🔄 "Black Box" Test: Real requests to running app
│
├── .dockerignore               # Important: Add pattern to ignore unit tests in prod build
├── docker-compose.yml          
├── Dockerfile                  
├── pyproject.toml              # Dependencies & Tool Config
└── README.md

```