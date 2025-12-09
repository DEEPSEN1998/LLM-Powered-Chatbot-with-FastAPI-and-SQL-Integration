import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [sql, setSql] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendQuery = async () => {
    setLoading(true);
    setSql("");
    setResults([]);

    try {
      const res = await fetch("http://localhost:8000/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer mysecrettoken",
        },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();

      if (!res.ok) {
        alert(data.detail || "Error");
        setLoading(false);
        return;
      }

      setSql(data.sql);
      setResults(data.results);
    } catch (err) {
      console.error(err);
      alert("Network error");
    }

    setLoading(false);
  };

  return (
  <div className="d-flex justify-content-center align-items-start" style={{ minHeight: "100vh", paddingTop: "50px" }}>
    <div className="container" style={{ maxWidth: "700px" }}>
      
      <h2 className="mb-4 text-center">🧠 NL → SQL Generator</h2>

      <div className="card p-4 shadow">
        <label className="form-label fw-bold">Enter Natural Language Query</label>
        <input
          className="form-control mb-3"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g., show all male customers"
        />

        <button className="btn btn-primary" onClick={sendQuery} disabled={loading}>
          {loading ? "Processing..." : "Generate SQL + Run"}
        </button>
      </div>

      {sql && (
        <div className="card mt-4 p-3 shadow-sm">
          <h5 className="fw-bold">Generated SQL:</h5>
          <pre className="bg-light p-2 border rounded">{sql}</pre>
        </div>
      )}

      {results.length > 0 && (
        <div className="card mt-4 p-3 shadow-sm">
          <h5 className="fw-bold">Results:</h5>
          <table className="table table-striped mt-2">
            <thead>
              <tr>
                {Object.keys(results[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {results.map((row, i) => (
                <tr key={i}>
                  {Object.keys(row).map((col) => (
                    <td key={col}>{row[col]}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

    </div>
  </div>
);

}

export default App;
