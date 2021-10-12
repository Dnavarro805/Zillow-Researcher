import React from 'react';
import './header.styles.css';


function Header() {
    return (
        <div className='header'>
            <div className='logo-container' to='/'>
                <div className='logo'>Zillow Researcher</div>
            </div>
        </div>
    )
}


export default Header;