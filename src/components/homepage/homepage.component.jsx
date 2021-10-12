import React from 'react';
import './homepage.styles.css';


function handleClick() {
    console.log("Clicked");
}


function HomePage() {
    return (    
        <div className='homepage'> 
            <div className='search-container'>
                <input className='search-bar' type='text' placeholder='Enter a city, state: Los Angeles, CA' />
                <button onClick={handleClick} className='button' type='submit'>Search</button>
            </div>
        </div>
    )
}


export default HomePage;