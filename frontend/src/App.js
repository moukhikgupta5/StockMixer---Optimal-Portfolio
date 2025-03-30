import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/home'

function App() {

  return (
    <div className="App">
      <BrowserRouter>
      <h1>StockMixer - Optimal Portfolio</h1>
        <Routes>
          <Route path='/' element=<Home/> />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
