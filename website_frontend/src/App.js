import './App.css';
import Main from './Main'
import Details from './Details'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
function App() {
  return (
    <div className="Main">
      <Router>
        <Switch>
        <Route path="/details">
          <Details/>
        </Route>
        <Route path="/">
          <Main/>
        </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
