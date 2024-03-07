import { TextField, Button } from '@mui/material';
import React, { useState } from 'react';

const Balance = () => {
  const [balance, setBalance] = useState(0);
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const handleAddBalance = () => {
    const amount = parseFloat(inputValue);
    if (!isNaN(amount)) {
      setBalance(balance + amount);
      setInputValue('');
    }
  };

  return (
    <div>
      <h2>Current Balance: ${balance}</h2>
      <TextField type="number" value={inputValue} onChange={handleInputChange} />
      <Button variant="contained" color="primary" onClick={handleAddBalance}>
        Add Balance
      </Button>
    </div>
  );
};

export default Balance;
