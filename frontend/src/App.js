import React from 'react';
import './App.css';
import UserList from "./components/user";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        const users = [
            {
                'username': 'BorisToboltsov',
                'first_name': 'Boris',
                'last_name': 'Toboltsov',
                'email': 'boris@boris.boris',
            },
            {
                'username': 'BorisToboltsov1',
                'first_name': 'Boris1',
                'last_name': 'Toboltsov1',
                'email': 'boris1@boris.boris',
            },
            {
                'username': 'BorisToboltsov2',
                'first_name': 'Boris2',
                'last_name': 'Toboltsov2',
                'email': 'boris2@boris.boris',
            }
        ]
      this.setState(
          {
            'users': users
          }
      )
    }

    render() {
        return (
            <div>
                <UserList users={this.state.users}/>
            </div>
        )
    }
}

export default App;
