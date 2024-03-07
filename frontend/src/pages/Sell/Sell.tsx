import React, { useState } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Button, Modal, Box, Typography, TextField } from '@mui/material';

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
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const handleSell = () => alert('Selling');
  const rows = [
    {
      name: 'UAN POWER CORP',
      symbol: 'UPOW',
      price: 100,
    },
    {
      name: 'APPLE INC',
      symbol: 'AAPL',
      price: 100,
    },
    {
      name: 'EXCO TECHNOLOGIES LTD',
      symbol: 'EXCOF',
      price: 100,
    },
  ];
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
            {rows.map((row) => (
              <TableRow key={row.name} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell>{row.symbol}</TableCell>
                <TableCell>{row.price}</TableCell>
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
            <TextField required id="amount" size="small" label="Amount" variant="outlined" />
            <Button type="submit">Sell</Button>
          </form>
        </Box>
      </Modal>
    </>
  );
};

export default Sell;
