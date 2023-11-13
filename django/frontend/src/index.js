import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
// import reportWebVitals from './reportWebVitals';
// import * as serviceWorker from './serviceWorker';

// Ajoutez cette ligne pour inclure Bootstrap JS si nécessaire
import 'bootstrap/dist/js/bootstrap.bundle.min';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// serviceWorker.unregister();  // Commentez ou supprimez cette ligne si vous souhaitez activer le service worker