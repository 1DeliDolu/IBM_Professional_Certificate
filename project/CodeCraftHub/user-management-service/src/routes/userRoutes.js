/**
 * @fileoverview This file defines the API routes for user management.
 * @version 1.0.0
 * @author Your Name
 */

const express = require('express');
const { registerUser, loginUser } = require('../controllers/userController');
const router = express.Router();

/**
 * Route for user registration.
 * @name POST /api/users/register
 * @function
 * @memberof module:routes/userRoutes
 * @inner
 * @param {string} path - Express path
 * @param {callback} middleware - Express middleware.
 */
router.post('/register', registerUser);

/**
 * Route for user login.
 * @name POST /api/users/login
 * @function
 * @memberof module:routes/userRoutes
 * @inner
 * @param {string} path - Express path
 * @param {callback} middleware - Express middleware.
 */
router.post('/login', loginUser);

module.exports = router;
