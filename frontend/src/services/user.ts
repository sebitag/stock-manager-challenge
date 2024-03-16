import { useMutation, useQuery, useQueryClient } from 'react-query';

export type Holding = {
  symbol: string;
  price: number;
  amount: number;
};

const getBalance = async (userId: number) => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/user/balance/${userId}`);
  const data = await res.json();
  return data;
};

const getHoldings = async (userId: number): Promise<Holding[]> => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/user/holdings/${userId}`);
  const data = await res.json();
  return data;
};
const addBalance = async ({ userId, amount }: { userId: number; amount: number }) => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/user/balance/add`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userId, amount }),
  });
  const data = await res.json();
  return data;
};

export const useBalanceQuery = (userId: number) => useQuery(['balance', userId], () => getBalance(userId));

export const useHoldingsQuery = (userId: number) => useQuery(['holdings', userId], () => getHoldings(userId));

export const useAddBalanceMutation = () => {
  // todo: add optimistic updates
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: addBalance,
    onSuccess: (_, variables) => {
      return queryClient.invalidateQueries({
        queryKey: ['balance', variables.userId],
      });
    },
  });
};
