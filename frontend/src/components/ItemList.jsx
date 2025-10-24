import React, { useEffect, useState } from "react";
import client from "../api/client";

function ItemList() {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState({ name: "", description: "" });
  const [error, setError] = useState(null);

  // Fetch items
  const fetchItems = () => {
    client.get("/items")
      .then(res => setItems(res.data))
      .catch(() => setError("Failed to load items"));
  };

  useEffect(() => {
    fetchItems(); // Load on mount
  }, []);

  // Create item
  const handleCreate = () => {
    client.post("/items", newItem)
      .then(() => {
        setNewItem({ name: "", description: "" });
        fetchItems();
      })
      .catch(() => setError("Failed to create item"));
  };

  // Update item
  const handleUpdate = (id) => {
    client.put(`/items/${id}`, newItem)
      .then(() => {
        setNewItem({ name: "", description: "" });
        fetchItems();
      })
      .catch(() => setError("Failed to update item"));
  };

  // Delete item
  const handleDelete = (id) => {
    client.delete(`/items/${id}`)
      .then(() => fetchItems())
      .catch(() => setError("Failed to delete item"));
  };

  return (
    <div>
      <h2>Items</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <input
        placeholder="Name"
        value={newItem.name}
        onChange={e => setNewItem({ ...newItem, name: e.target.value })}
      />
      <input
        placeholder="Description"
        value={newItem.description}
        onChange={e => setNewItem({ ...newItem, description: e.target.value })}
      />
      <button onClick={handleCreate}>Create</button>

      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name}: {item.description}
            <button onClick={() => handleUpdate(item.id)}>Update</button>
            <button onClick={() => handleDelete(item.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ItemList;