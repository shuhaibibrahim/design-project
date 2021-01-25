import React,{useState,useEffect} from 'react'
import Navbar1 from './Navbar1'
import {Table} from 'react-bootstrap'
import axios from 'axios'
function Details() {

    const[date,setdate]=useState('');
    const[data,setData]=useState([]);

    useEffect(() => {
      axios.get('https://design-server.herokuapp.com/vehicle')
      .then(res=>{
        console.log(res.data)
        setData(res.data)
      })
    }, [])

    return (
        <div className="App">
            <Navbar1/>
            <div style={{position:'absolute',right:'6%',marginTop:'2%',marginBottom:'2%'}}>
            <input type="date" value={date} onChange={(e)=>setdate(e.target.value)}/>
            </div>
            <div style={{width:'80%',display:'block',margin:'auto',borderRadius:'5px'}}>
            <Table striped bordered hover style={{margin:'4em',backgroundColor:'white',opacity:'0.88'}}>
            <thead>
            <tr>
                <th>Date</th>
                <th>Time</th>
                <th>License Plate Number</th>
            </tr>
            </thead>
  <tbody>
    {
      data.map(entry=>{
        return(
          <tr>
      <td>{entry.date.slice(0,10)}</td>
      <td>{entry.time}</td>
      <td>{entry.pnumber}</td>
    </tr>
        )
        
      })
    }


   
  </tbody>
</Table>
</div>
        </div>
    )
}

export default Details
