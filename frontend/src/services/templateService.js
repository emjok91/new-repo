import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const getTemplates = async () => {
  try {
    const response = await axios.get(`${API_URL}/templates`);
    return response.data;
  } catch (error) {
    console.error('Error fetching templates', error);
    throw error;
  }
};

export const addTemplate = async (templateData) => {
  try {
    const response = await axios.post(`${API_URL}/templates`, templateData);
    return response.data;
  } catch (error) {
    console.error('Error adding template', error);
    throw error;
  }
};

export const editTemplate = async (templateId, updatedData) => {
  try {
    const response = await axios.put(`${API_URL}/templates/${templateId}`, updatedData);
    return response.data;
  } catch (error) {
    console.error('Error editing template', error);
    throw error;
  }
};

export const deleteTemplate = async (templateId) => {
  try {
    const response = await axios.delete(`${API_URL}/templates/${templateId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting template', error);
    throw error;
  }
};