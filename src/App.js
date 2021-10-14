import { render } from '@testing-library/react';
import React, { Component} from 'react';
import './App.css';
import { HomeList } from './components/home-list/home-list.component';
import Footer from './components/footer/footer.component';
import Header from './components/header/header.component';
import HomePage from './components/homepage/homepage.component';


class App extends Component {

  constructor() {
    super();

    this.state = {
      houses: [ 
        // This should just be AN EMPTY ARRAY!
        // Were gonna wait for our component to mount
        // then were gonna update our state houses property
        // with the new array of dynamic entries
        {
          name: 'Hard Coded... Need to Connect Backend!',
          id: 'asc1'
        },
        {
          name: 'Guido Van Rossum',
          id: 'asc2'
        },
        {
          name: 'Alan Turing',
          id: 'asc3'
        },
        {
          name: 'Ada Lovelace',
          id: 'asc4'
        },
        {
          name: 'J.S. Bach',
          id: 'asc5'
        },
        {
          name: 'Charles Babbage',
          id: 'asc6'
        }
      ]
    };
  }

  componentDidMount() {
    fetch('')                               // Need to call API/Firebase
    .then(response => response.json())
    .then(entries => this.setState({ houses: entries }));
  }

  render() {
    return (
      <div className='App'>
        <Header />
        <HomePage />
        <HomeList houses={this.state.houses} />
        <Footer />
      </div>
    );
  }
}


export default App;
