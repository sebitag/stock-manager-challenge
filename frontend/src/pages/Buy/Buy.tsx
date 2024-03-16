import React, { useState } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Button, Modal, Box, Typography, TextField, CircularProgress } from '@mui/material';
import { useBuyStockMutation, useStocksQuery } from '@/services/stocks';

const style = {
  position: 'absolute' as const,
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};
const Buy = () => {
  const [open, setOpen] = useState(false);
  const [selectedStock, setSelectedStock] = useState('');
  const [amount, setAmount] = useState(1);
  const operation = useBuyStockMutation();
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const handleBuy = (e: React.FormEvent) => {
    e.preventDefault();
    operation.mutate({ userId: 1, symbol: selectedStock, amount });
  };

  const { data: stocks, isLoading } = useStocksQuery();
  if (isLoading)
    return (
      <Box sx={{ display: 'flex' }}>
        <CircularProgress />
      </Box>
    );
  return (
    <>
      <TableContainer component={Paper} sx={{ maxWidth: '650px', margin: '16px' }}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Symbol</TableCell>
              <TableCell>Price</TableCell>
              <TableCell></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {stocks &&
              stocks.map((stock) => (
                <TableRow key={stock.name} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                  <TableCell component="th" scope="row">
                    {stock.name}
                  </TableCell>
                  <TableCell>{stock.symbol}</TableCell>
                  <TableCell>{stock.price}</TableCell>
                  <TableCell align="right">
                    <Button
                      onClick={() => {
                        setSelectedStock(stock.symbol);
                        handleOpen();
                      }}
                    >
                      Buy
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2" pb={2}>
            Buying: {selectedStock}
          </Typography>
          <form onSubmit={handleBuy}>
            <TextField
              required
              id="amount"
              inputProps={{ min: '1' }}
              type="number"
              size="small"
              label="Amount"
              variant="outlined"
              value={amount}
              onChange={(e) => setAmount(Number(e.target.value))}
            />
            <Button type="submit">Buy</Button>
          </form>
        </Box>
      </Modal>
    </>
  );
};

export default Buy;
