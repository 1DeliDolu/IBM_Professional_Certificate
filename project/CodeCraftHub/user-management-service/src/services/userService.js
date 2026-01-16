/**
 * @fileoverview This file contains service layer functions for user-related operations.
 * @version 1.0.0
 * @author Your Name
 */

const User = require('../models/userModel');

/**
 * Finds a user by their ID.
 * @param {string} userId - The ID of the user to find.
 * @returns {Promise<User|null>} A promise that resolves to the user object or null if not found.
 */
exports.findUserById = async (userId) => {
    return await User.findById(userId);
};
