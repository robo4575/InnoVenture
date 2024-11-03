import { useState } from 'react';
import Chatbox from './components/Chatbot';
import PdfUpload from './components/PdfUpload';

const Home = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-4 flex flex-col items-center">
      <h1 className="text-2xl font-bold mb-6">AI Chatbot Interface</h1>
      <Chatbox />
      <PdfUpload />
    </div>
  );
};

export default Home;
