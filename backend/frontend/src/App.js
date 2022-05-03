import './App.css';
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [customers,setCustomer]=useState([])
  useEffect(()=>{
    async function getAllCustomer(){
      try{
        const customers=await axios.get("http://127.0.0.1:8000/api/customers/");
        console.log(customers.data)
        setCustomer(customers.data)
      }
      catch(error){
        console.log(error)
      }
    }
    getAllCustomer()
  },[])
  return (
    <div className="App">
      <h1>Connection Successful!!</h1>
    </div>
  );
}

export default App;
