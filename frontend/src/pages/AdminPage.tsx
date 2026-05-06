import React from 'react';
import ProductList from '../components/ProductList';
import ProductForm from '../components/ProductForm';

const AdminPage: React.FC = () => {
  return (
    <div>
      <h1>Admin Panel</h1>
      <ProductForm />
      <ProductList />
    </div>
  );
};

export default AdminPage;