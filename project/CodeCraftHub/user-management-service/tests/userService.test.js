const mongoose = require('mongoose');
const { MongoMemoryServer } = require('mongodb-memory-server');

const { connectDB } = require('../src/app');
const User = require('../src/models/userModel');
const userService = require('../src/services/userService');

describe('userService', () => {
    let mongoServer;

    beforeAll(async () => {
        mongoServer = await MongoMemoryServer.create();
        process.env.MONGO_URI = mongoServer.getUri('codecrafthub_users');
        await connectDB();
    });

    afterEach(async () => {
        await User.deleteMany({});
    });

    afterAll(async () => {
        await mongoose.connection.dropDatabase();
        await mongoose.connection.close();
        await mongoServer.stop();
    });

    it('returns a user when an existing id is provided', async () => {
        const createdUser = await User.create({
            username: 'service_user',
            email: 'service_user@example.com',
            password: 'hashedpass'
        });

        const found = await userService.findUserById(createdUser._id);
        expect(found).toBeTruthy();
        expect(found.email).toBe('service_user@example.com');
    });

    it('returns null when the user does not exist', async () => {
        const result = await userService.findUserById(new mongoose.Types.ObjectId());
        expect(result).toBeNull();
    });
});
