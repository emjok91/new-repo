import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api';

const apiService = {
  get: async (url, params) => {
    const response = await axios.get(`${BASE_URL}${url}`, { params });
    return response.data;
  },

  post: async (url, data) => {
    const response = await axios.post(`${BASE_URL}${url}`, data);
    return response.data;
  },

  put: async (url, data) => {
    const response = await axios.put(`${BASE_URL}${url}`, data);
    return response.data;
  },

  delete: async (url) => {
    const response = await axios.delete(`${BASE_URL}${url}`);
    return response.data;
  },
};

export default apiService;