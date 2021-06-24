import { createSlice } from "@reduxjs/toolkit";
import { ofType } from "redux-observable";
import api from "../api";
import { from, merge, of } from "rxjs";
import { map, mergeMap, catchError } from "rxjs/operators";
import { REHYDRATE } from "redux-persist";

const content = createSlice({
  name: "content",
  reducers: {
    setSearchTags: (state, { payload: searchTags }) => {
      state.searchTags = searchTags;
    },
    setSearchBooks: (state, { payload: books }) => {
      state.books = books;
    },
  },
  initialState: {
    searchTags: [],
    books: [],
  },
  slice: "content",
});

// export const initializeData = action$ =>
//     action$.pipe(
//         ofType(REHYDRATE),
//         mergeMap(() =>
//             merge(
//                 from(api.get('/universities/')).pipe(map(res => app.actions.setUniversities(res.data))),
//                 from(api.get('/schools/')).pipe(map(res => app.actions.setSchools(res.data)))
//             ).pipe(
//                 catchError(error => {
//                     return of(app.actions.unrecoverableFailure(error));
//                 })
//             )
//         )
//     );

export const searchEpic = (
  action$ //just tags so far
) =>
  action$.pipe(
    ofType(content.actions.setSearchTags),
    mergeMap(({ payload: searchTags }) => {
      return from(api.get(`/library/books/?tag=${searchTags}`)).pipe(
        mergeMap((res) => {
          console.log(res.data);
          return merge(
            of(content.actions.setSearchBooks(res.data)),
          );
        })
      );
    })
  );

export default content;
