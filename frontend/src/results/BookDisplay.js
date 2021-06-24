import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import {
  Card,
  CardMedia,
  CardContent,
  CardActions,
  CardActionArea,
  Typography,
  Chip,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: () => ({
    maxWidth: "300px",
  }),
}));

export default function BookDisplay(props) {
  const classes = useStyles();
  console.log("reached");
  return (
    <Card className={classes.root}>
      {/* on click do something later */}
      <CardActionArea>
        <CardMedia>{/* Deal with later */}</CardMedia>
        <CardContent>
          <Typography variant="h5">{props.title}</Typography>
          <Typography variant="body1">{props.author}</Typography>
          <br/>
          <Typography variant="caption">{props.description}</Typography>
        </CardContent>
        <CardActions>
          {props.tags.map((tag) => {
            <Chip label={tag.name}></Chip>;
          })}
        </CardActions>
      </CardActionArea>
    </Card>
  );
}
