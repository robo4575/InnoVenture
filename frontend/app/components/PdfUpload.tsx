'use client';
import { useState } from 'react';

const PdfUpload = () => {
  const [pdfFile, setPdfFile] = useState<File | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setPdfFile(e.target.files[0]);
      console.log('Selected PDF file:', e.target.files[0].name); // Placeholder for backend upload call
    }
  };

  const handleUpload = () => {
    if (pdfFile) {
      // Placeholder for backend file upload
      console.log('Backend call to upload PDF file:', pdfFile.name);
    }
  };

  return (
    <div className="w-full max-w-2xl bg-white shadow-lg rounded-lg p-4">
      <h2 className="text-lg font-bold mb-4">Upload PDF</h2>
      <input type="file" accept="application/pdf" onChange={handleFileChange} className="mb-2" />
      <button
        onClick={handleUpload}
        className="p-2 bg-green-500 text-white rounded-lg hover:bg-green-600"
      >
        Upload PDF
      </button>
    </div>
  );
};

export default PdfUpload;
