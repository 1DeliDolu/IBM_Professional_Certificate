/**
 * @fileoverview This file contains the controller functions for user-related operations.
 * @version 1.0.0
 * @author Your Name
 */

const User = require('../models/userModel');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

/**
 * Registers a new user.
 * @param {object} req - The request object.
 * @param {object} res - The response object.
 * @returns {object} The response object.
 */
exports.registerUser = async (req, res) => {
    const { username, email, password } = req.body;
    try {
        // Hash the password
        const hashedPassword = await bcrypt.hash(password, 10);
        // Create a new user
        const newUser = new User({ username, email, password: hashedPassword });
        // Save the user to the database
        await newUser.save();
        res.status(201).json({ message: 'User registered successfully.' });
    } catch (error) {
        res.status(500).json({ error: 'Registration failed.' });
    }
};

/**
 * Logs in a user.
 * @param {object} req - The request object.
 * @param {object} res - The response object.
 * @returns {object} The response object with a JWT token.
 */
exports.loginUser = async (req, res) => {
    const { email, password } = req.body;
    try {
        // Find the user by email
        const user = await User.findOne({ email });
        if (!user) return res.status(404).json({ error: 'User not found.' });
        // Compare the provided password with the stored hashed password
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) return res.status(401).json({ error: 'Invalid credentials.' });
        // Create and sign a JSON Web Token
        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET || 'secret', { expiresIn: '1h' });
        res.status(200).json({ token });
    } catch (error) {
        res.status(500).json({ error: 'Login failed.' });
    }
};
