import React from 'react'
import './App.css'

function Login() {
    return (
        <div className="login">
            <h1>MOTOR VEHICLE DEPARTMENT</h1>
            <div className="login_box">
                <form className="login_form">
                <h2>Login</h2>
                <input className="login_input" type="text" placeholder="POLICE ID NUMBER"/>
                <input className="login_input" type="password" placeholder="PASSWORD"/>
                <button className="submit">SIGN IN</button>
                </form>   
            </div>
        </div>
    )
}

export default Login
