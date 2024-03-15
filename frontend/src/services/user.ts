import { useMutation, useQuery, useQueryClient } from 'react-query';

const getBalance = async (userId: string) => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/user/balance/${userId}`);
  const data = await res.json();
  return data;
};

const getHoldings = async (userId: string) => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/user/holdings/${userId}`);
  const data = await res.json();
  return data;
};
const addBalance = async ({ userId, amount }: { userId: string; amount: number }) => {
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

export const useBalanceQuery = (userId: string) => useQuery(['balance', userId], () => getBalance(userId));

export const useHoldingsQuery = (userId: string) => useQuery(['holdings', userId], () => getHoldings(userId));

export const useAddBalanceMutation = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: addBalance,
    onSuccess: () => {
      return queryClient.invalidateQueries({
        queryKey: ['balance'],
      });
    },
  });
};
