import React from 'react';

const GreetingCard = () => {
  return (
    <div style={{ 
      padding: '20px', 
      border: '1px solid #ccc', 
      borderRadius: '8px',
      backgroundColor: '#f9f9f9',
      textAlign: 'center',
      maxWidth: '400px',
      margin: '20px auto'
    }}>
      <h1>Welcome to Our Application!</h1>
      <p>We're glad to have you here. Enjoy your stay!</p>
    </div>
  );
};

export default GreetingCard;