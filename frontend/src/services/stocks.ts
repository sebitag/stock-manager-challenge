import { useMutation, useQuery, useQueryClient } from 'react-query';

export type Stock = {
  symbol: string;
  name: string;
  price: number;
};

export const getStocks = async (): Promise<Stock[]> => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/stocks`);
  const data = await res.json();
  return data;
};

export const buyStock = async (userId: string, symbol: string, amount: number) => {
  await fetch(`${import.meta.env.VITE_API_URL}/stocks/buy`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userId, symbol, amount }),
  });
};

export const sellStock = async (userId: string, symbol: string, amount: number) => {
  await fetch(`${import.meta.env.VITE_API_URL}/stocks/sell`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userId, symbol, amount }),
  });
};

export const useStocksQuery = () => useQuery('stocks', getStocks);

export const useBuyStockMutation = (userId: string, symbol: string, amount: number) => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: () => buyStock(userId, symbol, amount),
    onSuccess: () => {
      return queryClient.invalidateQueries({
        queryKey: ['holdings', userId],
      });
    },
  });
};

export const useSellStockMutation = (userId: string, symbol: string, amount: number) => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: () => sellStock(userId, symbol, amount),
    onSuccess: () => {
      return queryClient.invalidateQueries({
        queryKey: ['holdings', userId],
      });
    },
  });
};
