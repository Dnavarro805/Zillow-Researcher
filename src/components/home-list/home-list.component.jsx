import React from "react";
import { Home } from '../home/home.component';
import './home-list.styles.css';


export const HomeList = props => (
    <div className='house-list'>
        {props.houses.map(house => (
            <Home key={house.id} house={house} />
        ))}
    </div>
);

