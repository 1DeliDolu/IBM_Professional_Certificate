/**
 * @fileoverview This file initializes the Express server and applies middleware.
 * @version 1.0.0
 * @author Your Name
 */

const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

/**
 * Initializes and configures the Express application.
 * @returns {object} The configured Express app object.
 */
const initServer = () => {
    const app = express();
    // Enable Cross-Origin Resource Sharing
    app.use(cors());
    // Parse incoming request bodies in a middleware before your handlers
    app.use(bodyParser.json());
    return app;
};

module.exports = initServer;
