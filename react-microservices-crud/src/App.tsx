import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Products from './components/admin/Products';
import { ProductsCreate } from './components/admin/ProductsCreate';
import ProductsEdit from './components/admin/ProductsEdit';
import Main from './components/main/Main';

function App() {
  return (
    <div className="App">

            <BrowserRouter>
              <Routes>
                <Route path='/' element={<Main/>}/>
                <Route path='/admin/products' element={<Products/>}/>
                <Route path='/admin/products/create' element={<ProductsCreate/>}/>
                <Route path='/admin/products/:id/edit' element={<ProductsEdit/>}/>
              </Routes>
            </BrowserRouter>

    </div>
  );
}

export default App;
