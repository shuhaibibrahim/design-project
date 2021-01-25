import React,{ useState } from 'react'
import {useHistory} from 'react-router-dom'
import LockIcon from '@material-ui/icons/Lock';
import './App.css'

function Login() {

    const history=useHistory();

    const[policeid,setPoliceid]=useState('');
    const[password,setPassword]=useState('');

    const handleLogin = () =>{
        history.push('/services')
    }

    return (
        <div className="login">
            <h1>PROJECT THIRD-EYE</h1>
            <div className="login_box">
                <form className="login_form" onSubmit={handleLogin}>
                <h2>Login</h2>
                <input className="login_input" type="text" value={policeid} placeholder="POLICE ID NUMBER" onChange={(e)=>setPoliceid(e.target.value)}/>
                <input className="login_input" type="password" value={password} placeholder="PASSWORD" onChange={(e)=>setPassword(e.target.value)}/>
                <button className="submit">SIGN IN</button>
                </form>   
            </div>
        </div>
    )
}

export default Login
