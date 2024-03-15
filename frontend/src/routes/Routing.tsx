import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from '@/pages/Home/Home';
import AppBar from '@/components/AppBar/AppBar';
import Buy from '@/pages/Buy/Buy';
import Balance from '@/pages/Balance/Balance';
import Sell from '@/pages/Sell/Sell';

const Routing = () => {
  return (
    <>
      <AppBar />
      <Routes>
        <Route path="*" element={<Home />} />
        <Route path="/buy" element={<Buy />} />
        <Route path="/sell" element={<Sell />} />
        <Route path="/balance" element={<Balance />} />
      </Routes>
    </>
  );
};

export default Routing;
