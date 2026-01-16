/**
 * @fileoverview This file defines the User schema and model.
 * @version 1.0.0
 * @author Your Name
 */

const mongoose = require('mongoose');

/**
 * Mongoose schema for the User model.
 * @type {mongoose.Schema}
 */
const userSchema = new mongoose.Schema({
    /**
     * The username of the user.
     * @type {string}
     * @required
     * @unique
     */
    username: {
        type: String,
        required: true,
        unique: true
    },
    /**
     * The email of the user.
     * @type {string}
     * @required
     * @unique
     */
    email: {
        type: String,
        required: true,
        unique: true
    },
    /**
     * The hashed password of the user.
     * @type {string}
     * @required
     */
    password: {
        type: String,
        required: true
    },
    /**
     * The role of the user.
     * @type {string}
     * @enum ['student', 'instructor', 'admin']
     * @default 'student'
     */
    role: {
        type: String,
        enum: ['student', 'instructor', 'admin'],
        default: 'student'
    },
    /**
     * The date the user was created.
     * @type {Date}
     * @default Date.now
     */
    createdAt: {
        type: Date,
        default: Date.now
    }
});

/**
 * Mongoose model for a User.
 * @type {mongoose.Model}
 */
const User = mongoose.model('User', userSchema);

module.exports = User;
