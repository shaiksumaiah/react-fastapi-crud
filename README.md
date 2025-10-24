# react-fastapi-crud

A full-stack example project integrating a React frontend with a FastAPI backend, demonstrating:

- API client setup  
- CRUD operations (Create, Read, Update, Delete)  
- State synchronization between frontend and backend  
- React Error Boundaries for robust UI  
- Clean folder structure and best-practices  

---

## 📁 Project Structure

react-fastapi-crud/
│
├── backend/
│ ├── main.py # FastAPI entry-point
│ ├── models.py # ORM or Pydantic models
│ ├── schemas.py # Request/response schemas
│ ├── crud.py # CRUD‐logic (data access)
│ ├── database.py # DB connection/configuration
│ ├── requirements.txt # Python dependencies
│ └── … # Other backend files/configs
│
└── frontend/
├── public/
│ └── index.html # Static HTML container
├── src/
│ ├── api/
│ │ └── apiClient.js # Axios/fetch wrapper for API calls
│ ├── components/
│ │ ├── ErrorBoundary.jsx
│ │ ├── ItemCard.jsx
│ │ └── ItemForm.jsx
│ ├── pages/
│ │ └── Dashboard.jsx
│ ├── App.jsx # Main React component
│ ├── main.jsx # React entry point
│ └── styles/
│ └── app.css
├── package.json
└── vite.config.js # (or your build config)

yaml
Copy code

---

## 🧰 Setup & Installation

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate      # (on Windows: venv\Scripts\activate)
pip install -r requirements.txt
uvicorn main:app --reload     # Launch the API server (default port 8000)
Frontend
bash
Copy code
cd frontend
npm install
npm run dev                   # Launch the React development server (default port 3000)
🔌 API Client Setup
In frontend/src/api/apiClient.js (or similar) you’ll find functions like:

javascript
Copy code
import axios from "axios";

const API_URL = "http://localhost:8000/items";

export const getItems = () => axios.get(API_URL);
export const createItem = (data) => axios.post(API_URL, data);
export const updateItem = (id, data) => axios.put(`${API_URL}/${id}`, data);
export const deleteItem = (id) => axios.delete(`${API_URL}/${id}`);
This abstraction ensures that all HTTP communication between React and FastAPI is centralized and easy to manage.

🧮 CRUD Operations
Backend (FastAPI)
The API implements endpoints for standard CRUD operations:

GET /items → retrieve a list of items

POST /items → create a new item

PUT /items/{id} → update an existing item

DELETE /items/{id} → delete an item

Example (simplified):

python
Copy code
@app.get("/items", response_model=List[ItemSchema])
def read_items():
    return crud.get_items(db)

@app.post("/items", response_model=ItemSchema)
def create_item(item: ItemSchemaCreate):
    return crud.create_item(db, item)

@app.put("/items/{item_id}", response_model=ItemSchema)
def update_item(item_id: int, item: ItemSchemaUpdate):
    return crud.update_item(db, item_id, item)

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    crud.delete_item(db, item_id)
    return {"message": "Item deleted"}
Frontend (React)
In React you’ll use the API client functions to perform operations, then update local state accordingly. Example flows:

On component mount: call getItems(), set state

On “Add” button click: call createItem(), then append to state

On “Edit” or “Toggle” click: call updateItem(), then update state item

On “Delete” click: call deleteItem(), then remove item from state

This ensures UI stays in sync with backend.

🔄 State Synchronization
React manages local state (via hooks such as useState, useEffect) and keeps it synced with backend data.
Example (simplified):

javascript
Copy code
const [items, setItems] = useState([]);

useEffect(() => {
  getItems().then(res => setItems(res.data));
}, []);

const handleAdd = async (newItem) => {
  const res = await createItem(newItem);
  setItems(prev => [...prev, res.data]);
};

const handleUpdate = async (id, updatedData) => {
  const res = await updateItem(id, updatedData);
  setItems(prev => prev.map(item => item.id === id ? res.data : item));
};

const handleDelete = async (id) => {
  await deleteItem(id);
  setItems(prev => prev.filter(item => item.id !== id));
};
This pattern ensures the UI always mirrors the server state.

🛡 Error Boundaries in React
To prevent your application from crashing due to unhandled errors in sub‐components, use an Error Boundary:

jsx
Copy code
// components/ErrorBoundary.jsx
import React from "react";

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Uncaught error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h2>Something went wrong. Please try again later.</h2>;
    }
    return this.props.children;
  }
}

export default ErrorBoundary;
You then wrap your main component(s) in <ErrorBoundary> so that if any child crashes, the fallback UI is shown instead of the whole app breaking.

jsx
Copy code
// App.jsx
import ErrorBoundary from "./components/ErrorBoundary";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <ErrorBoundary>
      <Dashboard />
    </ErrorBoundary>
  );
}

export default App;
📌 Why Use This Setup?
Separation of concerns: Backend handles business logic and data; frontend handles UI and user interactions.

Scalable architecture: Easy to extend endpoints and UI components.

Modern stack: Built with FastAPI (Python) for backend, and React for frontend.

Reusable API client: Clean abstraction for HTTP requests.

Robust UI: State synchronization + Error Boundaries ensure reliable user experience.

✅ Getting Started Checklist
 Clone the repository

 Set up backend environment, install dependencies

 Launch backend server (uvicorn)

 Set up frontend environment (npm install)

 Launch frontend dev server (npm run dev)

 Open browser at http://localhost:3000 (or configured port)

 Test CRUD operations: Create, Read, Update, Delete items

 Inspect API requests/responses (browser dev tools or Postman)

 Introduce an error in a component to verify Error Boundary works

🧭 Future Improvements
Add authentication & authorization (JWT)

Integrate a persistent database (PostgreSQL, SQLite) instead of in-memory/storage

Add pagination, filtering & search on GET endpoints

Improve UI/UX: form validation, loading states, error notifications

Add unit & integration tests for both backend and frontend

📄 License
Distributed under the MIT License. See LICENSE for details.

📬 Contact
If you have questions or suggestions, feel free to open an issue or reach out to the author.

yaml
Copy code
