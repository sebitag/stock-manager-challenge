import { useAddBalanceMutation, useBalanceQuery } from '@/services/user';
import { TextField, Button, Box, CircularProgress } from '@mui/material';
import React, { useState } from 'react';

const USER_ID = 1;

const Balance = () => {
  const [inputValue, setInputValue] = useState('');
  const { data: balance, isLoading } = useBalanceQuery(USER_ID);
  const operation = useAddBalanceMutation();

  const handleAddBalance = () => {
    const amount = parseFloat(inputValue);
    if (!isNaN(amount)) {
      setInputValue('');
      operation.mutate({ userId: USER_ID, amount });
    }
  };

  if (isLoading) {
    return (
      <Box sx={{ display: 'flex' }}>
        <CircularProgress />
      </Box>
    );
  }
  return (
    <div>
      <h2>Current Balance: ${balance.toFixed(2)}</h2>

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
