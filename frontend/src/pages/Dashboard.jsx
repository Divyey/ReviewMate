import { useState } from "react";

function Dashboard() {
  const [owner, setOwner] = useState("");
  const [repo, setRepo] = useState("");
  const [prNumber, setPrNumber] = useState("");
  const [prData, setPrData] = useState(null);

  const fetchPR = async () => {
    const res = await fetch(
      `http://localhost:8000/fetch-pr?owner=${owner}&repo=${repo}&pr_number=${prNumber}`
    );
    const data = await res.json();
    setPrData(data);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Fetch GitHub Pull Request</h2>
      <input
        placeholder="Owner"
        value={owner}
        onChange={e => setOwner(e.target.value)}
        style={{ marginRight: "1rem" }}
      />
      <input
        placeholder="Repo"
        value={repo}
        onChange={e => setRepo(e.target.value)}
        style={{ marginRight: "1rem" }}
      />
      <input
        placeholder="PR Number"
        value={prNumber}
        onChange={e => setPrNumber(e.target.value)}
        style={{ marginRight: "1rem" }}
      />
      <button onClick={fetchPR}>Fetch PR</button>
      <pre style={{ marginTop: "2rem", background: "#eee", padding: "1rem" }}>
        {prData && JSON.stringify(prData, null, 2)}
      </pre>
    </div>
  );
}

export default Dashboard;
