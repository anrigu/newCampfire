import { combineReducers, configureStore } from "@reduxjs/toolkit";
import { connectRouter, routerMiddleware } from "connected-react-router";
import { createBrowserHistory } from "history";
import { combineEpics, createEpicMiddleware } from "redux-observable";
import { persistReducer, persistStore } from "redux-persist";
import storage from "redux-persist/lib/storage";
import { catchError } from "rxjs/operators";
import content, { searchEpic } from "./content";
import logger from "redux-logger";

const persistConfig = {
  key: "root",
  storage,
  blacklist: [],
};
export const history = createBrowserHistory();
const persistedReducer = persistReducer(
  persistConfig,
  combineReducers({
    content: content.reducer,
    router: connectRouter(history),
  })
);

const rootEpic = (action$, store$, dependencies) =>
  combineEpics(searchEpic)(action$, store$, dependencies).pipe(
    catchError((error, source) => {
      return source;
    })
  );

const epicMiddleware = createEpicMiddleware();
const middleware = [routerMiddleware(history), epicMiddleware];
middleware.push(logger);

const store = configureStore({
  reducer: persistedReducer,
  middleware: middleware,
});
export default store;
export const persistor = persistStore(store);

epicMiddleware.run(rootEpic);
