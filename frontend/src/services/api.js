import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

const api = axios.create({
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});

// Interceptor para injetar a Base URL dinâmica de forma assíncrona
api.interceptors.request.use(
  async (config) => {
    try {
      const savedIp = await AsyncStorage.getItem('server_ip');
      const savedPort = await AsyncStorage.getItem('server_port');
      
      const ip = savedIp || '192.168.15.98'; // Mantém o atual como fallback
      const port = savedPort || '8000';
      
      config.baseURL = `http://${ip}:${port}`;
      console.log(`[API Request] BaseURL: ${config.baseURL}, Path: ${config.url}`);
      return config;
    } catch (error) {
      console.error('Erro ao recuperar configurações de IP:', error);
      config.baseURL = 'http://192.168.15.98:8000';
      return config;
    }
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('Erro na API:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export default api;
