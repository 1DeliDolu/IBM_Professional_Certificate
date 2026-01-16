/**
 * @fileoverview This file contains the logger configuration using Winston.
 * @version 1.0.0
 * @author Your Name
 */

const winston = require('winston');

/**
 * Winston logger instance.
 * @type {winston.Logger}
 */
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        //
        // - Write all logs with level `error` and below to `error.log`
        //
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
        //
        // - Write all logs with level `info` and below to the console
        //
        new winston.transports.Console()
    ]
});

module.exports = logger;
