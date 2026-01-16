const request = require('supertest');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const { MongoMemoryServer } = require('mongodb-memory-server');

const { app, connectDB } = require('../src/app');
const User = require('../src/models/userModel');

describe('User Controller (register/login)', () => {
    let mongoServer;

    beforeAll(async () => {
        mongoServer = await MongoMemoryServer.create();
        process.env.MONGO_URI = mongoServer.getUri('codecrafthub_users');
        process.env.JWT_SECRET = 'test_secret';
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

    it('registers a user and hashes the password', async () => {
        const payload = {
            username: 'john_smith_1',
            email: 'johnsmith_1@example.com',
            password: 'Password1234!'
        };

        const res = await request(app).post('/api/users/register').send(payload);

        expect(res.status).toBe(201);
        expect(res.body).toEqual({ message: 'User registered successfully.' });

        const storedUser = await User.findOne({ email: payload.email }).lean();
        expect(storedUser).toBeTruthy();
        expect(storedUser.username).toBe(payload.username);
        expect(storedUser.password).not.toBe(payload.password);

        const isHashed = await bcrypt.compare(payload.password, storedUser.password);
        expect(isHashed).toBe(true);
    });

    it('logs in an existing user and returns a JWT', async () => {
        const payload = {
            username: 'john_smith_1',
            email: 'johnsmith_1@example.com',
            password: 'Password1234!'
        };
        await request(app).post('/api/users/register').send(payload);

        const res = await request(app)
            .post('/api/users/login')
            .send({ email: payload.email, password: payload.password });

        expect(res.status).toBe(200);
        expect(res.body).toHaveProperty('token');
        expect(typeof res.body.token).toBe('string');
    });

    it('rejects login with incorrect password', async () => {
        const payload = {
            username: 'john_smith_1',
            email: 'johnsmith_1@example.com',
            password: 'Password1234!'
        };
        await request(app).post('/api/users/register').send(payload);

        const res = await request(app)
            .post('/api/users/login')
            .send({ email: payload.email, password: 'WrongPassword!' });

        expect(res.status).toBe(401);
        expect(res.body).toEqual({ error: 'Invalid credentials.' });
    });
});
