import React from "react";

const Navbar = ({navbar}) => {
    return (
        <ul>
            <li>
                <a href="/#">Главная</a>
            </li>
            <li>
                <a href="/#">Пользователи</a>
            </li>
            <li className="todo">To-do list</li>
        </ul>
    )
}

export default Navbar
