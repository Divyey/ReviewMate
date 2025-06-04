import { useEffect } from "react";

function App() {
  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then(res => res.json())
      .then(data => console.log(data));
  }, []);
  return <h1>ReviewMate Frontend is Working!</h1>;
}
export default App;
