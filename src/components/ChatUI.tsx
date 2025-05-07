'use client';
import React, { useState } from 'react';

const ChatUI = () => {
  const [userInput, setUserInput] = useState('');
  const [chatHistory, setChatHistory] = useState<string[]>([]);

  const handleMessageSubmit = async () => {
    if (!userInput.trim()) return;

    setChatHistory(prev => [...prev, `You: ${userInput}`]);
    setUserInput('');

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userMessage: userInput }),
      });

      const data = await response.json();
      setChatHistory(prev => [...prev, `Mindmate: ${data.message}`]);

    } catch (error) {
      console.error(error);
      setChatHistory(prev => [...prev, 'Mindmate: Hmm, something went wrong. Please try again.']);
    }
  };

  return (
    <div className="p-4">
      <div className="mb-4">
        {chatHistory.map((msg, index) => (
          <div key={index} className="mb-2">{msg}</div>
        ))}
      </div>
      <input
        type="text"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        className="border p-2 w-full"
        placeholder="Type your feelings..."
      />
      <button
        onClick={handleMessageSubmit}
        className="mt-2 p-2 bg-blue-500 text-white rounded"
      >
        Send
      </button>
    </div>
  );
};

export default ChatUI;