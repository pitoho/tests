import grpc
import unittest
import registration_pb2
import registration_pb2_grpc
import database_pb2
import database_pb2_grpc

class TestRegistrationService(unittest.TestCase):

    def setUp(self):
        self.channel = grpc.insecure_channel('localhost:3000/login')
        self.stub = registration_pb2_grpc.RegistrationStub(self.channel)

    def test_register_user(self):
        request = registration_pb2.RegisterRequest(useremail='adcd', password='123')

        response = self.stub.Register(request)

        self.assertEqual(response.status, registration_pb2.RegisterResponse.SUCCESS)

    def test_get_user(self):
        request = registration_pb2.GetUserRequest(username='adcd')

        response = self.stub.GetUser(request)

        self.assertEqual(response.username, 'adcd')

    def tearDown(self):
        self.channel.close()

class TestDatabaseService(unittest.TestCase):

    def setUp(self):
        self.channel = grpc.insecure_channel('localhost:5432')
        self.stub = database_pb2_grpc.DatabaseStub(self.channel)

    def test_store_data(self):
        request = database_pb2.StoreDataRequest(key='testkey', value='testdata')

        response = self.stub.StoreData(request)

        self.assertEqual(response.status, database_pb2.StoreDataResponse.SUCCESS)

    def test_retrieve_data(self):
        request = database_pb2.RetrieveDataRequest(key='testkey')

        response = self.stub.RetrieveData(request)

        self.assertEqual(response.value, 'testdata')

    def tearDown(self):
        self.channel.close()

if __name__ == '__main__':
    unittest.main()