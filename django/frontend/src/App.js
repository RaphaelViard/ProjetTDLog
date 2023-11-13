// import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';  // Importez le CSS Bootstrap

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('/api/items/')
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  return (
    <div className="container mt-5">
      <h1>Welcome to our site!</h1>
      <ul className="list-group mt-3">
        {items.map(item => (
          <li key={item.id} className="list-group-item">
            {item.name} - {item.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;