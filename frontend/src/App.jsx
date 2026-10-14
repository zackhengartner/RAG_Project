import Toledo from "./assets/toledo.png";
import "./index.css";

function App() {
  return (
    <div className="app">
      <div className="sidebar">
        <button className="new-chat-button">+ New Chat</button>

        <p className="history-title">HISTORY</p>
      </div>

      <div className="main-content">
        <div className="chat-container">
          <img src={Toledo} className="toledo-logo" />

          <h1>Rocket Bot</h1>

          <p className="description">
            Ask about courses, prerequisites, requirements, or university
            information.
          </p>

          <div className="input-box">
            <textarea
              className="question-input"
              placeholder="Ask RocketBot..."
              rows="4"
            />

            <div className="send-container">
              <button className="send-button">Send</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;