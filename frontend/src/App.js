import React from 'react';
import './App.css';
import UserList from "./components/user";
import Footer from "./components/footer";
import Navbar from "./components/menu";
import axios from 'axios';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div className="container">
                <Navbar/>
                <UserList users={this.state.users}/>
                <Footer/>
            </div>
        )
    }
}

export default App;
