'use client';

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import OrderCard from "@/app/components/OrderCard";
import {fetchOrderStatus} from "@/lib/api";

const OrderPage: React.FC = () => {
  const [order, setOrder] = useState(null);

 useEffect(() => {
    const getOrder = async () => {
      const orderData = await fetchOrderStatus();
      setOrder(orderData);
    };

    getOrder();
  }, []);

  if (!order) {
    return (
      <div className="flex items-center justify-center h-screen text-xl font-medium text-gray-600">
        Cargando orden...
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center px-4">
      <h1 className="text-2xl font-bold text-blue-500 mb-6">Detalles de la Orden</h1>
      <OrderCard order={order} />
    </div>
  );
};

export default OrderPage;