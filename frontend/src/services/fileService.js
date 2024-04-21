import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await axios.post(`${API_URL}/upload`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const getFiles = async () => {
  const response = await axios.get(`${API_URL}/files`);
  return response.data;
};

export const getFileDetails = async (fileId) => {
  const response = await axios.get(`${API_URL}/files/${fileId}`);
  return response.data;
};

export const processFile = async (fileId) => {
  const response = await axios.post(`${API_URL}/process/${fileId}`);
  return response.data;
};