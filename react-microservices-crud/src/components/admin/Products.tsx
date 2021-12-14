/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Product } from "../../interfaces/Product";
import Wrapper from "./Wrapper";

const Products = () => {

    const [products, setProducts] = useState([]);


    useEffect(() => {
      (async() => {
        const response = await fetch('http://localhost:9000/api/products');
        const data = await response.json();
        
        setProducts(data);
      })();
    }, [])

    const del = async (id: number) => {
      if(window.confirm('Are you sure you want to delete this product?')) {
        await fetch('http://localhost:9000/api/products/' + id, {
          method: 'DELETE'})
        .then( response => {
          if (response.ok === true) setProducts(products.filter((p:Product) => p.id !== id))
        })
        .catch(err => console.error(err));
      }
    }

    return(
        <Wrapper>
          <div className="table-responsive">

          <div className="pt-3 pb-2 mb-3 border-bottom">
                <div className="btn-toolbar mb-2 mb-md-0">
                    <Link to='/admin/products/create' className="btn btn-sm btn-outline-primary">Add</Link>
                </div>
            </div>
            
            <table className="table table-striped table-sm">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Image</th>
                  <th scope="col">Title</th>
                  <th scope="col">Likes</th>
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                {
                  products.map((product: Product ) =>(
                    <tr key={product.id}>
                      <td> {product.id} </td>
                      <td> <img src={product.image} height="175" alt={product.title}/> </td>
                      <td> {product.title}</td>
                      <td> {product.likes}</td>
                      <td> 
                        <div className="btn-group mr-2">
                          <Link to={`/admin/products/${product.id}/edit`} className="btn btn-sm btn-outline-secondary"> Edit </Link>
                          <a href="#" className="btn btn-sm btn-outline-danger"
                            onClick={() => del(product.id)}> Delete </a>
                        </div>
                      </td>
                    </tr>
                  ))
                }
              </tbody>
            </table>
          </div>
        </Wrapper>
    );
};

export default Products;