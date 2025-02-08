import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function fetchOrderStatus() {
    try {
        const response = await axios.get(`${API_BASE_URL}/order/status`);
        return response.data.order;
    } catch (error) {
        console.error('Error al obtener la orden:', error);
        throw error;
    }
}