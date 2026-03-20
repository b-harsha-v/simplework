import { useState } from "react";
import API from "../services/api";

function Chat() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState(null);

  const user_id = 1; // temporary (later from auth)

  const sendMessage = async () => {
    try {
      const res = await API.post("/chat", {
        message: "Create a 4 week DSA study plan",
        user_id: 1,
        goal: "Data Structures and Algorithms",
        duration: 4,
      });

      console.log("RESPONSE:", res.data);
      setResponse(res.data);
    } catch (err) {
      console.error("ERROR:", err.response?.data || err.message);
    }
  };

  return (
    <div>
      <h1>SimpleWork Chat</h1>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter your message"
      />

      <button onClick={sendMessage}>Send</button>

      <pre>{JSON.stringify(response, null, 2)}</pre>
    </div>
  );
}

export default Chat;