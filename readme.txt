1. mkdir myapp
2. cd myapp
3. python -m venv .venv
4. .venv\Scripts\Activate.ps1
5. pip install fastapi uvicorn
6. fastapi deploy

packages needs to be installed:

1. pip install azure-core
2. pip install azure-identity - ClientSecretCreddentials
3. pip install azure-mgmt-subscription - SubscriptionClient
4. pip install azure-mgmt-resource - ResourceManagementClient
5. pip install azure-mgmt-resourceGraph - ResourceGraphClient
6. pip install azure-mgmt-costmanagement - CostManagementClient
7. pip install apscheduler - for using the scheduler
8. pip install python-jose // optional - for jwt authentication
9. pip install "passlib[bcrypt]" // optional - for password hashing
10. pip install dotenv - accessing .env files
12. pip install fastapi-limiter - limits the api requests 
13. pip install msgraph-sdk


Grouping inputs:

1. None
2. ResourceGroup
3. ResourceId
4. ServiceFamily
5. MeterCategory
6. MeterSubCategory
7. Meter
8. Product
9. Location
10. PricingModel
11. RGS - Resource group with service name
12. RGRID  - Resource grooup with resource id
13. RIDMC - resource Id with meter MeterCategory
14. Service - resource id with service family and meter category
15. RGRIDS - resource group with resource id and service name
16. ServiceName

maximam grouping limit 15

Cost Type:
1. ActualCost
2. Usage
3. AmortizedCost

Granularity 
1. NONE
2. DAILY
3. MONTHLY

Aggregation:
1. PreTaxCost
2. PreTaxCostUSD
3. Cost
4. CostUSD
5. UsageQuantity

overall forcastCost = cost + forecastCost 

Implement Retry Logic for cost 429 error 

import time
import random
import requests

def call_api_with_retry(url, headers, max_retries=5):
    for i in range(max_retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 2))
            wait_time = retry_after + random.uniform(0, 1)
            print(f"Rate limited. Retrying in {wait_time:.2f}s")
            time.sleep(wait_time)
        else:
            return response
    raise Exception("Max retries exceeded")

    fastapi-project/
│
├── app/
│   ├── main.py              # Entry point
│   ├── core/                # Settings, configs
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── api/                 # Route handlers
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── user.py
│   │   │   │   └── auth.py
│   │   │   └── router.py
│   │
│   ├── models/              # Database models (SQLAlchemy, etc.)
│   │   └── user.py
│   │
│   ├── schemas/             # Pydantic schemas
│   │   └── user.py
│   │
│   ├── services/            # Business logic
│   │   └── user_service.py
│   │
│   ├── db/                  # Database connection/session
│   │   ├── base.py
│   │   └── session.py
│   │
│   └── utils/               # Helper functions
│       └── helpers.py
│
├── tests/                   # Test cases
│   └── test_user.py
│
├── alembic/                 # Migrations (if using Alembic)
├── requirements.txt
├── .env
└── README.md


