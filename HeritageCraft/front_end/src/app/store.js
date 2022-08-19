import { configureStore } from '@reduxjs/toolkit';
import productsReducer from "../Features/Listing/productsSlice";

export const store = configureStore({
  reducer: {
    products: productsReducer,
  },
});
