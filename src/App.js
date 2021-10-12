import React from 'react';
import './App.css';
import Footer from './components/footer/footer.component';
import Header from './components/header/header.component';
import HomePage from './components/homepage/homepage.component';



function App() {
  return (
    <div>
      <Header />
      <HomePage />
      <Footer />
    </div>
  );
}

export default App;
