import { useState } from 'react';
import JoinForm from './components/JoinForm';
import { LiveKitRoom, VideoConference } from '@livekit/components-react';
import '@livekit/components-styles';
// We import v4 from the uuid library we installed earlier
import { v4 as uuidv4 } from 'uuid'; 

function App() {
  const [token, setToken] = useState(null);
  const [serverUrl, setServerUrl] = useState(null);

  // This function is passed to JoinForm. It triggers when the user clicks submit.
  const handleJoinRequest = async (name, roomCode) => {
    // Generate a unique ID for this user session
    const participantId = uuidv4();

    try {
      // Reaching out to your FastAPI backend
      const response = await fetch("http://localhost:8000/api/livekit/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          room_code: roomCode,
          participant_name: name,
          id: participantId
        }),
      });

      if (!response.ok) {
        // If the backend returns a 404 (Room not found), we throw an error
        const errorData = await response.json();
        console.error("FASTAPI ERROR DETAILS:", errorData);
        throw new Error(errorData.detail || "Failed to join room");
      }

      // Parse the token and URL from FastAPI's response
      const data = await response.json();
      
      // Update state! This hides the JoinForm and renders the LiveKitRoom
      setToken(data.token);
      setServerUrl(data.url);
      
    } catch (error) {
      console.error(error);
      alert(error.message);
    }
  };

  // Screen A: The Form
  if (token === null) {
    return (
      <div className="min-h-screen flex items-center justify-center p-4">
        <JoinForm onJoin={handleJoinRequest} />
      </div>
    );
  }

  // Screen B: The Video Room
  return (
    <LiveKitRoom
      video={true}
      audio={true}
      token={token}
      serverUrl={serverUrl}
      data-lk-theme="default"
      style={{ height: '100vh' }}
      onDisconnected={ ()=>{
        setToken(null);
        setServerUrl(null);
      }}
    >
      <VideoConference />
    </LiveKitRoom>
  );
}

export default App;