import React, { Component } from "react";
import { CONFIG } from "./config.js";

class App extends Component {
  constructor() {
    super();
    this.state = {
      users: [],
    };
  }

  componentDidMount() {
    fetch(CONFIG.API_BASE_URL)
      .then((results) => {
        return results.json();
      })
      .then((users) => {
        this.setState({ users: users });
      });
  }

  render() {
    const users = this.state.users.map((user, index) => (
      <li key={index}>
        {user.lastname} {user.firstname}
      </li>
    ));

    return (
      <div>
        <h1>Users list</h1>
        <ul>{users}</ul>
      </div>
    );
  }
}

export default App;
