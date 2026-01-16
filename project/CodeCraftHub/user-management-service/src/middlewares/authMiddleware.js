/**
 * @fileoverview This file contains middleware for authentication and authorization.
 * @version 1.0.0
 * @author Your Name
 */

const jwt = require('jsonwebtoken');

/**
 * Middleware to verify the JWT token from the Authorization header.
 * @param {object} req - The request object.
 * @param {object} res - The response object.
 * @param {function} next - The next middleware function.
 */
const authMiddleware = (req, res, next) => {
    // Get token from header
    const token = req.header('Authorization')?.split(' ')[1];
    // Check if not token
    if (!token) {
        return res.status(401).json({ error: 'Access denied.' });
    }

    try {
        // Verify token
        const verified = jwt.verify(token, process.env.JWT_SECRET);
        // Add user from payload
        req.user = verified;
        next();
    } catch (error) {
        res.status(400).json({ error: 'Invalid token.' });
    }
};

module.exports = authMiddleware;
