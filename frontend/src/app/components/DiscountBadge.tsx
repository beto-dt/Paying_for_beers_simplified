import React from 'react';

interface Props {
  discount: number;
}

const DiscountBadge: React.FC<Props> = ({ discount }) => {
  if (discount > 0) {
    return (
      <div className="bg-green-100 text-green-800 font-bold py-1 px-3 rounded-full inline-block">
        ¡Descuento Aplicado!
      </div>
    );
  }
  return null;
};

export default DiscountBadge;