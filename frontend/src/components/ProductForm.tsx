import React, { useState } from 'react';
import axios from 'axios';

const ProductForm: React.FC = () => {
  const [name, setName] = useState('');
  const [price, setPrice] = useState('');
  const [stock, setStock] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    axios.post('http://localhost:8000/products', {
      name,
      price_cents: parseInt(price) * 100,
      stock: parseInt(stock)
    }, {
      headers: { Authorization: 'Bearer admin' } // Mock
    })
    .then(() => alert('Product added'))
    .catch(error => console.error(error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
      <input type="number" placeholder="Price" value={price} onChange={e => setPrice(e.target.value)} />
      <input type="number" placeholder="Stock" value={stock} onChange={e => setStock(e.target.value)} />
      <button type="submit">Add Product</button>
    </form>
  );
};

export default ProductForm;