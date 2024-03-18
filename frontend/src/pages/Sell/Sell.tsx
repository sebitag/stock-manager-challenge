import React, { useState } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import {
  Button,
  Box,
  Typography,
  TextField,
  CircularProgress,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
} from '@mui/material';
import { useHoldingsQuery } from '@/services/user';
import { useSellStockMutation, useStocksQuery } from '@/services/stocks';

const USER_ID = 1;

const Sell = () => {
  const [open, setOpen] = useState(false);
  const [selectedStock, setSelectedStock] = useState('');
  const [amount, setAmount] = useState(1);

  const { data: stocks, isLoading: loadingStocks } = useStocksQuery();
  const { data: holdings, isLoading: loadingHoldings } = useHoldingsQuery(USER_ID);
  const sellOperation = useSellStockMutation();

  const handleSell = async (e: React.FormEvent) => {
    e.preventDefault();
    if (selectedStock) await sellOperation.mutateAsync({ userId: USER_ID, symbol: selectedStock, amount });
    setOpen(false);
  };

  const getPrice = (selectedStock: string) => {
    const stock = stocks?.find((stock) => stock.symbol === selectedStock);
    return stock?.price;
  };

  if (loadingStocks || loadingHoldings) {
    return (
      <Box sx={{ display: 'flex' }}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <>
      <TableContainer component={Paper} sx={{ maxWidth: '650px', margin: '16px' }}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell align="center">Symbol</TableCell>
              <TableCell align="center">Holding</TableCell>
              <TableCell align="center">Current Price</TableCell>
              <TableCell></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {holdings &&
              holdings.map((stock) => (
                <TableRow key={stock.symbol} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                  <TableCell align="center">{stock.symbol}</TableCell>
                  <TableCell align="center">{stock.amount}</TableCell>
                  <TableCell align="center">${getPrice(stock.symbol)?.toFixed(2)}</TableCell>
                  <TableCell align="center">
                    <Button
                      variant="contained"
                      onClick={() => {
                        setSelectedStock(stock.symbol);
                        setOpen(true);
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

      <Dialog
        open={open}
        onClose={() => setOpen(false)}
        PaperProps={{
          component: 'form',
          onSubmit: handleSell,
        }}
      >
        <DialogTitle>Sell {selectedStock}</DialogTitle>
        <DialogContent sx={{ overflow: 'unset' }}>
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
          <Typography variant="body2" align="right">
            Total: ${((getPrice(selectedStock) ?? 0) * amount).toFixed(2)}
          </Typography>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpen(false)}>Cancel</Button>
          <Button variant={'contained'} type="submit" disabled={sellOperation.isLoading}>
            Sell
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
};

export default Sell;
