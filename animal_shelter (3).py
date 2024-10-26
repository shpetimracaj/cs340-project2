from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Connection Variables
        USER = 'aacuser'  # Replace with your credentials
        PASS = 'new_password'  # Replace with your credentials
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31621
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None and isinstance(data, dict):
            # Insert the provided data into the collection and check if it succeeded.
            result = self.collection.insert_one(data)  # data should be a dictionary
            return result.acknowledged  # Return True if insert was successful, False otherwise
        else:
            raise Exception("Data is invalid or empty")

    # Read method to implement the R in CRUD.
    def read(self, search_data=None):
        if search_data:
            # Find documents matching the search criteria, excluding the '_id' field from the results.
            data = self.collection.find(search_data, {"_id": False})
        else:
            # If no search criteria, return all documents, excluding the '_id' field.
            data = self.collection.find({}, {"_id": False})
        return list(data)  # Convert the cursor to a list and return it.

    # Update method to implement the U in CRUD.
    def update(self, search_data, update_data):
        if search_data:
            # Update multiple documents that match the search criteria with the new data.
            result = self.collection.update_many(search_data, {"$set": update_data})
            return result.modified_count  # Return the count of updated documents
        else:
            return 0  # Return 0 if no search_data.

    # Delete method to implement the D in CRUD.
    def delete(self, delete_data):
        if delete_data:
            # Delete multiple documents that match the specified criteria.
            result = self.collection.delete_many(delete_data)
            return result.deleted_count  # Return the count of deleted documents
        else:
            return 0  # Return 0 if no delete_data.

