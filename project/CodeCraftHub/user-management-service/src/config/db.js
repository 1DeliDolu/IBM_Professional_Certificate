/**
 * @fileoverview This file contains the database connection logic.
 * @version 1.0.0
 * @author Your Name
 */

const mongoose = require('mongoose');

/**
 * Connects to the MongoDB database using the connection string from environment variables.
 * @async
 * @function connectDB
 */
const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URI, {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
        console.log('MongoDB connected successfully.');
    } catch (error) {
        console.error('MongoDB connection failed:', error);
        process.exit(1);
    }
};

module.exports = connectDB;
