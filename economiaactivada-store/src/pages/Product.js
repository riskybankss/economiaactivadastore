import React from 'react';

const Product = ({ product }) => {
    return (
        <div className="product-detail">
            <h1>{product.name}</h1>
            <img src={product.image} alt={product.name} />
            <p>{product.description}</p>
            <h2>Price: ${product.price}</h2>
        </div>
    );
};

export default Product;