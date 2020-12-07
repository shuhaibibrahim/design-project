import './App.css';
import Navbar1 from './Navbar1'
import Login from './Login'
import {Container} from 'react-bootstrap'
function Main() {
  return (
    <div className="App">
      <Container fluid>
      <Navbar1/>
      <Login/>
      </Container> 
    </div>
  );
}

export default Main;