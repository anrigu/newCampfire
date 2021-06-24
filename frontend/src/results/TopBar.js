import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import SearchIcon from "@material-ui/icons/Search";
import { Button, Icon, Chip, IconButton } from "@material-ui/core";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import content from "../redux/content";
import MenuIcon from '@material-ui/icons/Menu';

const useStyles = makeStyles((theme) => ({
  topBar: () => ({
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
  }),
}));

export default function TopBar() {
  const classes = useStyles();
  return (
    <div className={classes.topBar}>
      <SearchBar />
      <IconButton onClick={}><MenuIcon/></IconButton>
    </div>
  );
}
