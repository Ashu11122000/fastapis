# Import required modules from FastAPI
# fastapi → main framework package
# FastAPI → class used to create API application
# HTTPException → used to raise API errors (like 404, 500)
# Request → represents incoming HTTP request
# BackgroundTasks → allows running tasks after response is sent
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks


# Import BaseModel for data validation
# pydantic → library for data validation and parsing
# BaseModel → class used to define request/response schema
from pydantic import BaseModel


# Import time module to measure request processing time
# time → built-in Python module
# used for timestamps and performance measurement
import time


# Create FastAPI app instance
# app → variable holding FastAPI object
# FastAPI() → initializes the web application
app = FastAPI()


# -----------------------------
# Pydantic Model (Data Schema)
# -----------------------------
# class → keyword to define a class
# Item → class name (represents structure of data)
# (BaseModel) → inheritance (Item gets features of BaseModel)
class Item(BaseModel):

    # text → field name
    # : → type annotation
    # str → string type
    # | None → means optional (can be string OR None)
    # = None → default value is None
    text: str | None = None

    # is_done → field name
    # bool → boolean type (True/False)
    # = False → default value is False
    is_done: bool = False


# -----------------------------
# In-memory storage
# -----------------------------
# items → variable name
# = [] → empty list (used to store data)
# This acts like a temporary database
items = []


# -----------------------------
# Middleware (logs request time)
# -----------------------------
# @ → decorator (modifies function behavior)
# app.middleware("http") → registers middleware for all HTTP requests
@app.middleware("http")

# async → defines asynchronous function (non-blocking)
# def → function definition keyword
# log_request_time → function name
# request: Request → parameter with type (incoming request)
# call_next → function to pass request to next handler
async def log_request_time(request: Request, call_next):

    # start_time → variable name
    # time.time() → returns current timestamp (in seconds)
    start_time = time.time()

    # await → waits for async operation to complete
    # call_next(request) → passes request to route handler
    # response → stores returned response
    response = await call_next(request)

    # process_time → total time taken
    # time.time() - start_time → difference gives execution time
    process_time = time.time() - start_time

    # print → outputs to console
    # f"" → formatted string (f-string)
    # request.method → GET, POST, etc.
    # request.url → full request URL
    # :.4f → format float to 4 decimal places
    print(f"{request.method} {request.url} - {process_time:.4f}s")

    # return → sends response back to client
    return response


# -----------------------------
# Background Task
# -----------------------------
# def → function definition
# write_log → function name
# item: Item → parameter of type Item
def write_log(item: Item):

    """
    Multi-line comment (docstring)
    Explains function purpose
    """

    # with → context manager (handles file closing automatically)
    # open("log.txt", "a") →
    # "log.txt" → file name
    # "a" → append mode (adds data without deleting old data)
    with open("log.txt", "a") as f:

        # f.write() → writes data into file
        # \n → new line character
        f.write(f"Item added: {item}\n")


# -----------------------------
# Routes (API Endpoints)
# -----------------------------

# @app.get("/") →
# decorator defining GET API
# "/" → root URL
@app.get("/")

# def → function definition
# root → function name
def root():

    """
    Returns simple response
    """

    # return → sends JSON response
    # {"Hello": "World"} → dictionary converted to JSON
    return {"Hello": "World"}


# Create Item (POST)
# @app.post("/items") → POST API endpoint
@app.post("/items")

# create_item → function name
# item: Item → request body (validated using Pydantic)
# background_tasks: BackgroundTasks → dependency injection
def create_item(item: Item, background_tasks: BackgroundTasks):

    """
    Handles item creation
    """

    # items.append() → adds new item to list
    # item.dict() → converts Pydantic object to dictionary
    items.append(item.dict())

    # background_tasks.add_task() →
    # schedules function to run in background
    # write_log → function name
    # item → argument passed to function
    background_tasks.add_task(write_log, item)

    # return → sends response
    return items


# Get All Items
# response_model=list[Item] →
# ensures response follows schema of list of Item
@app.get("/items", response_model=list[Item])

# limit: int = 10 →
# query parameter with default value 10
def list_items(limit: int = 10):

    """
    Returns limited number of items
    """

    # items[:limit] → slicing list
    # returns first 'limit' items
    return items[:limit]


# Get Single Item by ID
# {item_id} → path parameter
@app.get("/items/{item_id}", response_model=Item)

# item_id: int → parameter must be integer
def get_item(item_id: int):

    """
    Returns item by index
    """

    # if → conditional statement
    # len(items) → total number of items
    if item_id < len(items):

        # return specific item
        return items[item_id]

    else:
        # raise → throws exception
        # HTTPException → FastAPI error handler
        # status_code=404 → Not Found error
        # detail → error message
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found"
        )