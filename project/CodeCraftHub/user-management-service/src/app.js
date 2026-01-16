/**
 * @fileoverview Main application file to initialize the Express server.
 * @version 1.0.0
 * @author Your Name
 */

// Load environment variables from .env file
require('dotenv').config();

// Import required modules
const connectDB = require('./config/db');
const initServer = require('./config/server');
const userRoutes = require('./routes/userRoutes');
const errorHandler = require('./utils/errorHandler');

// Initialize the Express application
const app = initServer();

// Mount user routes at /api/users
app.use('/api/users', userRoutes);

// Use the centralized error handler
app.use(errorHandler);

/**
 * Starts the HTTP server after establishing the database connection.
 * Separated for reuse in tests to prevent auto-start.
 * @returns {Promise<import('http').Server>} The started HTTP server.
 */
const startServer = async () => {
    await connectDB();
    const PORT = process.env.PORT || 5000;
    return app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
};

// Only auto-start when run directly (e.g., `node src/app.js`)
if (require.main === module) {
    startServer();
}

module.exports = { app, startServer, connectDB };
