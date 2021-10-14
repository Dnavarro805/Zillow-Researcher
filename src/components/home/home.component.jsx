import React from "react";
import './home.styles.css';


export const Home = props => (
    <div className='home-container'>
    {/* <img alt='home' src={`...{props.house.id}...`} /> */}
        <h2>{props.house.name}</h2>
        {/* <p>{props.house.address}</p> */}
    </div>
);