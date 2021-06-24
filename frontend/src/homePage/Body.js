import React from "react";
import { makeStyles } from "@material-ui/styles";
import Background from "./Background";
import SearchBar from "./SearchBar";

const useStyles = makeStyles((theme) => ({
  body: () => ({
    height: "100vh",
    overflow:'hidden',
    width: "100%",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  }),
}));

export default function Body() {
  const classes = useStyles();
  return (
    <div className={classes.body}>
      <SearchBar />
      <Background />
    </div>
  );
}
