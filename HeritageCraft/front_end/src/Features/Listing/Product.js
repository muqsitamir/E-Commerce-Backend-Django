import React from "react";
import Typography from '@mui/material/Typography';
import {CardContent, CardMedia} from "@mui/material";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";



export default function Product(props){
    let content = props.content;
    return(
        <Box
          sx={{
            display: 'flex',
            flexWrap: 'wrap',
            '& > :not(style)': {
              m: 2,
              width: 360,
              height: 480,
              '&:hover': {
                opacity: [0.9, 0.8, 0.7],
              },
            },
          }}
        >
          <Paper elevation={10} sx={{overflow:"auto"}}>
                <CardMedia
                component="img"
                height="250"
                image={`http://0.0.0.0:8000/media/${content.image}`}
                alt="Product Image"
                />
                <CardContent >
                    <Typography variant="h5" gutterBottom component="div" marginTop={1} marginLeft={2}>
                        {content.title}
                    </Typography>
                    <Typography variant="h6"gutterBottom component="div" marginTop={1} marginLeft={2} >
                        Rs.{content.price}
                    </Typography>
                    <Typography variant="body2" color="text.secondary" gutterBottom component="div" marginTop={1} marginLeft={2}>
                        { content.description }
                    </Typography>
                </CardContent>
          </Paper>
        </Box>
    );
}