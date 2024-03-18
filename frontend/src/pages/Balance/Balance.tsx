import { useAddBalanceMutation, useBalanceQuery } from '@/services/user';
import { TextField, Button, Box, CircularProgress, Typography } from '@mui/material';
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
    <Box m={2} display={'flex'} alignItems={'center'} flexDirection={'column'}>
      <Typography variant="h2" pb={2}>
        Current Balance: ${balance.toFixed(2)}
      </Typography>

      <form onSubmit={handleAddBalance}>
        <TextField
          required
          id="amount"
          type="number"
          value={inputValue}
          size="small"
          sx={{ pr: 1 }}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <Button variant="contained" type="submit">
          Add
        </Button>
      </form>
    </Box>
  );
};

export default Balance;
