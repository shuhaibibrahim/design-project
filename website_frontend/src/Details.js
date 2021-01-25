import React,{useState} from 'react'
import Navbar1 from './Navbar1'
import {Table} from 'react-bootstrap'
function Details() {

    const[date,setdate]=useState('');

    return (
        <div className="App">
            <Navbar1/>
            <div>
            <input type="date" value={date} onChange={(e)=>setdate(e.target.value)}/>
            </div>
            <Table striped bordered hover style={{margin:'4em',backgroundColor:'white',opacity:'0.88'}}>
            <thead>
            <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Username</th>
            </tr>
            </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <td>3</td>
      <td colSpan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</Table>
        </div>
    )
}

export default Details
