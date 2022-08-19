import React, {useEffect, useState} from 'react';
import {Grid, Pagination, PaginationItem, Stack, TablePagination} from '@mui/material';
import {useDispatch, useSelector} from "react-redux";
import {getProducts} from "./productsSlice";
import { selectProducts } from "./productsSlice";
import Product from "./Product";
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';


export default function Listing() {
    const [state, setState] = useState({page: 0});
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProducts())
    }, []);
    const {results: products} = useSelector(selectProducts);

    const handlePageChange = (event, newPage) => {
        newPage = newPage - 1;
        if (newPage > state.page)
            dispatch(getProducts(newPage));
        if (newPage < state.page)
            dispatch(getProducts(newPage));
        setState({page: newPage});
    };

    return(
        <div className="page">
            <div className="page__content">
                <div className="main-wrapper" >
                    <header className="row db" style={{paddingTop: 30, paddingLeft: '10%', paddingBottom: 20, marginBottom: 40, backgroundColor: "lightgrey", borderBottom: "inset grey"}}>
                        <div className="col s12">
                            <h1 className="bold" style={{fontSize: 45, color:"darkgoldenrod"}}>Heritage Craft</h1>
                        </div>
                    </header>
                    <div style={{marginLeft: 20, marginRight: 30, paddingLeft:100, paddingRight: 100}}>
                        <Grid container justify="center" spacing={2}>
                            {products.map((camera) => (
                                <Grid item xs={12} sm={6} md={4} lg={3}>
                                    <Product content={camera}/>
                                </Grid>
                            ))}
                        </Grid>
                    </div>
                    <Stack spacing={2} sx={{position:'absolute', left: "40%", marginTop: 4, paddingBottom: 10}}>
                      <Pagination
                        count={10}
                        color={"primary"}
                        variant="outlined"
                        size="large"
                        onChange={handlePageChange}
                      />
                    </Stack>
                </div>
            </div>
        </div>
    );
}
