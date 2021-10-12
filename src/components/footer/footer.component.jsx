import React from 'react';
import './footer.styles.css';


function Footer() {

    const currentYear = new Date().getFullYear();
    return (
        <div className='footer'>
            <footer>
                <p>Copyright © {currentYear} Zillow Researcher, All Rights Reserved. DANIEL NAVARRO.</p>
            </footer>
        </div>
    );
}


export default Footer;