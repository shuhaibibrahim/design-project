import React from 'react'
import {Navbar,Nav, NavLink} from 'react-bootstrap'
import {Link} from 'react-router-dom'

function Navbar1() {
    return (
        <div>
            <Navbar varint="dark" expand="lg">
            <Navbar.Brand href="#home"> <Link to="/"><img src="logo.png" alt="" className="logo"/></Link> </Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
            <ul className="ml-auto navs">
            <li className="nav_link">LOGIN</li>
            <li className="nav_link">SERVICES</li>
            <li className="nav_link">ABOUT</li>
            <li className="nav_link">CONTACT</li>
            </ul>
            </Navbar.Collapse>
            </Navbar>
        </div>
    )
}

export default Navbar1
