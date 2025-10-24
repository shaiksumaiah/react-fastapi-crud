import axios from "axios";

// Axios client for FastAPI
const client = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

export default client;