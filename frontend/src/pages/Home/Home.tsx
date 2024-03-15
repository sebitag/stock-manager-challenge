import React from 'react';
import { Typography, Container } from '@mui/material';

const Home = () => {
  return (
    <Container sx={{ py: 2, position: 'relative' }}>
      <Typography textAlign="center" variant="h2">
        Stock Manager
      </Typography>
    </Container>
  );
};

export default Home;
