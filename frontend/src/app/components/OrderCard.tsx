import React from 'react';
import {Order} from '../types/Order';

interface Props {
    order: Order;
}

const OrderCard: React.FC<Props> = ({order}) => {
    return (
        <div className="border rounded-lg shadow-lg p-6 bg-white max-w-md mx-auto">
            <h2 className="text-2xl font-bold mb-6 text-center bg-blue-500 text-white p-3 rounded">
                Detalles de la Orden
            </h2>

            <ul className="divide-y divide-gray-300 mb-6">
                {order.items && order.items.length > 0 ? (
                    order.items.map((item, index) => (
                        <li
                            key={`${item.name}-${index}`}
                            className="py-2 flex justify-between items-center"
                        >
              <span className="text-gray-700 font-medium">
                {item.name} x{item.quantity || 0}
              </span>
                            <span className="text-green-600 font-bold">
                ${item.total?.toFixed(2) || "0.00"}
              </span>
                        </li>
                    ))
                ) : (
                    <li className="py-2 text-gray-500 text-center">No hay items en la orden.</li>
                )}
            </ul>

            <hr className="my-6"/>

            <div className="space-y-2 text-right">
                <p className="text-gray-600">
                    Subtotal:{" "}
                    <span className="font-bold">${order?.subtotal?.toFixed(2) || "0.00"}</span>
                </p>
                <p className="text-gray-600">
                    Impuestos:{" "}
                    <span className="font-bold">${order?.taxes?.toFixed(2) || "0.00"}</span>
                </p>
                <p className="text-red-500">
                    Descuento:{" "}
                    <span className="font-bold">-${order?.discounts?.toFixed(2) || "0.00"}</span>
                </p>
                <p className="text-2xl font-bold text-gray-800 mt-4">
                    Total: <span>${order?.total?.toFixed(2) || "0.00"}</span>
                </p>
            </div>
        </div>
    );
};

export default OrderCard;