# FastAPI Learning Task
A beginner-to-intermediate FastAPI task demonstrating core backend concepts like routing, data validation, middleware, and background tasks.

---

## Project Overview
This task is built using FastAPI, a modern Python web framework for building APIs quickly and efficiently.
It includes:
- Basic API setup
- CRUD-like operations
- Pydantic models for validation
- Middleware for logging
- Background tasks
- Query & path parameters

---

## What is FastAPI?
FastAPI is a high-performance web framework for building APIs with Python.

### Key Features:
- Very fast
- Automatic data validation using Pydantic
- Auto-generated API docs (Swagger UI)
- Type hint-based development
- Async support

---

## What is Uvicorn?
Uvicorn is an ASGI server used to run FastAPI applications.

### Why Uvicorn?
- High performance
- Supports async/await
- Runs FastAPI apps in production

# Run server:
uvicorn main:app --reload

# Concepts Used in This Project
## FastAPI App Initialization
```bash
app = FastAPI()
```
* Creates the main application instance
* Used to define routes and configurations

## Routing (API Endpoints)
```bash
@app.get("/")
@app.post("/items")
```
* Defines HTTP endpoints
* Supports GET, POST, PUT, DELETE

## Pydantic Models (Data Validation)
```bash
class Item(BaseModel):
    text: str | None = None
    is_done: bool = False
```
* Ensures request data is valid
* Automatically converts JSON → Python objects

# Request & Response Handling
* Accept JSON input
* Return JSON output automatically

# Path Parameters
```bash
@app.get("/items/{item_id}")
```
* Used to access dynamic values in URL

# Query Parameters
```bash
def list_items(limit: int = 10):
```
* Optional parameters in URL

Example:
```bash 
/items?limit=5
```

# Middleware
```bash
@app.middleware("http")
```
* Runs before and after each request
* Used for:
  1. Logging
  2. Authentication
  3. Performance tracking

# Background Tasks
```bash
background_tasks.add_task(write_log, item)
```
* Runs tasks after response is sent
* Improves performance
* Example:
  1. Logging
  2. Email sending

# Exception Handling
```bash
raise HTTPException(status_code=404, detail="Item not found")
```
* Handles errors gracefully
* Returns proper HTTP response

# In-Memory Storage
```bash
items = []
```
* Temporary data storage
* Used instead of database (for learning)

---

# How to Run the Project
1. Clone Repository
git clone https://github.com/Ashu11122000/fastapis.git
cd fastapis

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run Server
uvicorn main:app --reload

5. Open in Browser
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

# Project Structure
fastapis/
│
├── main.py          # Main FastAPI app
├── requirements.txt # Dependencies
├── .gitignore
└── README.md

# Example API Endpoints
Method	Endpoint	Description
GET	      /	        Hello World
POST	/items	    Create item
GET	    /items	    Get all items
GET	  /items/{id}	Get item by ID
