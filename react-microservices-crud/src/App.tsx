import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Products from './components/admin/Products';
import Main from './components/main/Main';

function App() {
  return (
    <div className="App">

            <BrowserRouter>
              <Routes>
                <Route path='/' element={<Main/>}/>
                <Route path='/admin/products' element={<Products/>}/>
              </Routes>
            </BrowserRouter>

    </div>
  );
}

export default App;
