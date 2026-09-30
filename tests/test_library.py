import unittest


class TestLibrarySystem(unittest.TestCase):

    def test_add_book(self):
        books = []
        books.append({
            "id": "B1",
            "title": "Python Basics",
            "author": "Test Author",
            "available": True
        })

        self.assertEqual(len(books), 1)
        self.assertTrue(books[0]["available"])

    def test_add_member(self):
        members = []
        members.append({
            "id": "M1",
            "name": "Test Member"
        })

        self.assertEqual(len(members), 1)


if __name__ == "__main__":
    unittest.main()
