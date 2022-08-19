import { createSlice } from '@reduxjs/toolkit'
import axios from "axios";
// import {showLoadingScreen, setSnackBar} from "../../reusable_components/site_data/siteDataSlice";


export const productsSlice = createSlice({
  name: 'products',
  initialState: {
      products: {
          "count": 0,
          "results": []
      },
  },
  reducers: {
      setProducts: (state, action) => {
          state.products.results = action.payload;
          state.products.count = action.payload.length;
      },
  },
})

const Header = {
    // 'Access-Control-Allow-Origin': '*',
    // 'Access-Control-Allow-Headers': "*",
    // 'Accept': '*/*'
};
export const getProducts = (page) => (dispatch) => {
    let config = {
        headers: Header,
    };
    let page_no = !page ? 0 : page;
    // debugger;
    axios.get(`http://0.0.0.0:8000/shop/api/products/?page=${page_no}`, config).then((res) => {
        dispatch(setProducts(res.data));
    }).catch((err) => {
        // dispatch(setSnackBar(err.response.data.non_field_errors[0]));
    }).finally(() => {
        // dispatch(showLoadingScreen(false));
    })
}


// Action creators are generated for each case reducer function
export const { setProducts } = productsSlice.actions
export const selectProducts = (state) => state.products.products;
export default productsSlice.reducer

