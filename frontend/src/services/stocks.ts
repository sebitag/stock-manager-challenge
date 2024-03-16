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

export const buyStock = async ({ userId, symbol, amount }: { userId: number; symbol: string; amount: number }) => {
  await fetch(`${import.meta.env.VITE_API_URL}/stocks/buy`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userId, symbol, amount }),
  });
};

export const sellStock = async ({ userId, symbol, amount }: { userId: number; symbol: string; amount: number }) => {
  await fetch(`${import.meta.env.VITE_API_URL}/stocks/sell`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userId, symbol, amount }),
  });
};

export const useStocksQuery = () => useQuery('stocks', getStocks);

export const useBuyStockMutation = () => {
  // const queryClient = useQueryClient();
  return useMutation({
    mutationFn: buyStock,
    // onSuccess: (_, variables) => {
    //   queryClient.invalidateQueries(['balance', variables.userId]);
    //   return queryClient.invalidateQueries(['holdings', variables.userId]);
    // },
  });
};

export const useSellStockMutation = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: sellStock,
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries(['balance', variables.userId]);
      return queryClient.invalidateQueries(['holdings', variables.userId]);
    },
  });
};
