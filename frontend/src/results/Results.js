import React from "react";
import BooksPreview from "./BooksPreview";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: () => ({
    height: "100vh",
    width: "100%",
  }),
}));

export default function Results() {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <BooksPreview />
    </div>
  );
}
