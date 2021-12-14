import React, { SyntheticEvent, useState } from 'react'
import { Navigate } from 'react-router-dom';
import Wrapper from './Wrapper'


export const ProductsCreate = () => {

    const [title, setTitle] = useState('');
    const [image, setImage] = useState('');
    const [redirect, setRedirect] = useState(false);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        await fetch('http://localhost:9000/api/products/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title,
                image
            })
        })
        .then( response => {
            if (response.ok === true) 
                setRedirect(true);
        })
        .catch(err => console.error(err));
    }

    if (redirect) return <Navigate to={'/admin/products'}/>

    return (
        <Wrapper>
            <form onSubmit={submit}>
                <div className="form-group">
                    <label>Title</label>
                    <input type="text" className="form-control" name="title"
                           onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" name="image"
                           onChange={e => setImage(e.target.value)}
                    />
                </div>
                <button className="btn btn-outline-success mt-2">Save</button>
            </form>
        </Wrapper>
    )
}
