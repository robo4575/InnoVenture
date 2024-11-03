'use client';
import { useState } from 'react';

const Chatbox = () => {
  const [messages, setMessages] = useState<{ role: 'user' | 'bot'; content: string }[]>([]);
  const [input, setInput] = useState('');

  const handleSendMessage = () => {
    if (input.trim()) {
      // Append user's message
      setMessages([...messages, { role: 'user', content: input }]);

      // Placeholder for backend call
      console.log('Backend call to send message:', input);

      // Append bot's placeholder response
      setMessages((prev) => [
        ...prev,
        { role: 'bot', content: "I'm an AI, and this is a placeholder response." },
      ]);

      setInput('');
    }
  };

  return (
    <div className="w-full max-w-2xl bg-white shadow-lg rounded-lg p-4 mb-6">
      <div className="overflow-y-auto h-64 border-b border-gray-300 mb-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`p-2 my-2 rounded-lg ${
              msg.role === 'user' ? 'bg-blue-100 text-right' : 'bg-gray-100 text-left'
            }`}
          >
            {msg.content}
          </div>
        ))}
      </div>
      <div className="flex items-center">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          className="flex-grow p-2 border border-gray-300 rounded-l-lg focus:outline-none"
        />
        <button
          onClick={handleSendMessage}
          className="p-2 bg-blue-500 text-white rounded-r-lg hover:bg-blue-600"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbox;
