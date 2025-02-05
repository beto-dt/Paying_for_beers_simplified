   import axios from 'axios';

   const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000';

   export const fetchOrder = async () => {
     try {
       const response = await axios.get(`${API_BASE_URL}/orders/status`);
       return response.data;
     } catch (error) {
       console.error('Error al obtener la orden:', error);
       throw error;
     }
   };