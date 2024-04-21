import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Document, Page } from 'react-pdf';
import { getFileDetails } from '../services/fileService';
import { Button } from 'antd';

const FileDetails = () => {
  const { id } = useParams();
  const [fileDetails, setFileDetails] = useState(null);
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getFileDetails(id);
      setFileDetails(result.data);
    };
    fetchData();
  }, [id]);

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
  }

  return (
    <div>
      {fileDetails && (
        <div>
          <h2>{fileDetails.name}</h2>
          <Document
            file={fileDetails.url}
            onLoadSuccess={onDocumentLoadSuccess}
          >
            <Page pageNumber={pageNumber} />
          </Document>
          <p>Page {pageNumber} of {numPages}</p>
          <Button onClick={() => setPageNumber(prevPageNumber => prevPageNumber - 1)} disabled={pageNumber <= 1}>Previous</Button>
          <Button onClick={() => setPageNumber(prevPageNumber => prevPageNumber + 1)} disabled={pageNumber >= numPages}>Next</Button>
          <h3>Extracted Tasks</h3>
          {fileDetails.tasks.map((task, index) => (
            <div key={index}>
              <h4>{task.name}</h4>
              <p>{task.description}</p>
              <a href={task.templateUrl} download>Download Filled Template</a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default FileDetails;