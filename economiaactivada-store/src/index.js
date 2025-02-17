import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Product from './pages/Product';
import './styles/main.css';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={Home} />
                <Route path="/product/:id" component={Product} />
            </Switch>
        </Router>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));