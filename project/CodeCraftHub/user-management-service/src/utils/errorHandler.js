/**
 * @fileoverview This file contains the centralized error handling middleware.
 * @version 1.0.0
 * @author Your Name
 */

const logger = require('./logger');

/**
 * Centralized error handler middleware.
 * @param {Error} err - The error object.
 * @param {object} req - The request object.
 * @param {object} res - The response object.
 * @param {function} next - The next middleware function.
 */
const errorHandler = (err, req, res, next) => {
    // Log the error
    logger.error(err);
    // Send a generic error response
    res.status(500).json({ error: 'Something went wrong.' });
};

module.exports = errorHandler;
