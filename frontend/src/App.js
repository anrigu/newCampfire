import logo from "./logo.svg";
import "./App.css";
import Body from "./homePage/Body";
import { Provider } from "react-redux";
import store, { history, persistor } from "./redux";
import { PersistGate } from "redux-persist/integration/react";
import { ConnectedRouter } from "connected-react-router";
import { Redirect, Route, Switch } from "react-router-dom";
import Results from './results/Results';

function App() {
  return (
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <ConnectedRouter history={history}>
          <Switch>
            <Route component={Results} path="/results" />
            <Route component={Body} path="/" />
          </Switch>
        </ConnectedRouter>
      </PersistGate>
    </Provider>
  );
}

export default App;
