import { useAddBalanceMutation, useBalanceQuery } from '@/services/user';
import { TextField, Button } from '@mui/material';
import React, { useState } from 'react';

const USER_ID = 1;

const Balance = () => {
  const [inputValue, setInputValue] = useState('');
  const { data: balance } = useBalanceQuery(USER_ID);
  const operation = useAddBalanceMutation();

  const handleAddBalance = () => {
    const amount = parseFloat(inputValue);
    if (!isNaN(amount)) {
      setInputValue('');
      operation.mutate({ userId: USER_ID, amount });
    }
  };

  return (
    <div>
      <h2>Current Balance: ${balance}</h2>

      <form onSubmit={handleAddBalance}>
        <TextField
          required
          id="amount"
          type="number"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <Button type="submit">Add Balance</Button>
      </form>
    </div>
  );
};

export default Balance;
