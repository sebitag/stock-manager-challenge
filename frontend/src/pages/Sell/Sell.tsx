import React, { useState } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Button, Modal, Box, Typography, TextField } from '@mui/material';
import { useHoldingsQuery } from '@/services/user';
import { useSellStockMutation } from '@/services/stocks';

const USER_ID = 1;

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
const Sell = () => {
  const [open, setOpen] = useState(false);
  const [selectedStock, setSelectedStock] = useState('');
  const [amount, setAmount] = useState(1);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const { data: holdings } = useHoldingsQuery(USER_ID);
  const operation = useSellStockMutation();
  const handleSell = (e: React.FormEvent) => {
    e.preventDefault();
    operation.mutate({ userId: 1, symbol: selectedStock, amount });
  };

  return (
    <>
      <TableContainer component={Paper} sx={{ maxWidth: '650px', margin: '16px' }}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Symbol</TableCell>
              <TableCell>Amount</TableCell>
              <TableCell></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {holdings &&
              holdings.map((row) => (
                <TableRow key={row.symbol} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                  <TableCell>{row.symbol}</TableCell>
                  <TableCell>{row.amount}</TableCell>
                  <TableCell align="right">
                    <Button
                      onClick={() => {
                        setSelectedStock(row.symbol);
                        handleOpen();
                      }}
                    >
                      Sell
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
            Selling: {selectedStock}
          </Typography>
          <form onSubmit={handleSell}>
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
            <Button type="submit">Sell</Button>
          </form>
        </Box>
      </Modal>
    </>
  );
};

export default Sell;
