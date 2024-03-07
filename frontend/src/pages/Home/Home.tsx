import React from 'react';
import { Typography, Stack, Container } from '@mui/material';
import Counter from '@/components/Counter/Counter';

const Home = () => {
  return (
    <Container sx={{ py: 2, position: 'relative' }}>
      <Typography textAlign="center" variant="h2">
        Stock Manager
      </Typography>
      <Counter />
    </Container>
  );
};

export default Home;
