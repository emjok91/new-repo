```javascript
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import FileUpload from './components/FileUpload';
import FileList from './components/FileList';
import FileDetails from './components/FileDetails';
import TemplateManagement from './components/TemplateManagement';
import Authentication from './components/Authentication';
import PrivateRoute from './components/PrivateRoute';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login" component={Authentication} />
        <PrivateRoute exact path="/" component={Dashboard} />
        <PrivateRoute path="/upload" component={FileUpload} />
        <PrivateRoute path="/files" component={FileList} />
        <PrivateRoute path="/file/:id" component={FileDetails} />
        <PrivateRoute path="/templates" component={TemplateManagement} />
      </Switch>
    </Router>
  );
}

export default App;
```