import React from "react";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import BookDisplay from "./BookDisplay";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: () => ({
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-evenly",
    alignItems: "center",
    width: "100%",
    height: "100%",
    flexWrap: "wrap",
  }),
}));

function BooksPreview(props) {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      {props.books.map((book, ind) => console.log(book) || (
        <BookDisplay
          key={ind}
          title={book.title}
          author={book.author}
          description={book.description}
          tags={book.tags}
        />
      ))}
    </div>
  );
}

export default connect(
  (state) => ({
    books: state.content.books,
  }),
  (dispatch) => bindActionCreators({}, dispatch)
)(BooksPreview);
