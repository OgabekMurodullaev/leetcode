# import unittest
# import math
# import warnings
#
#
# class TestWeirdCases(unittest.TestCase):
#
#     def test_assertIsInstance(self):
#         self.assertIsInstance(1729, int)
#
#     def test_assertNotIsInstance(self):
#         self.assertNotIsInstance("melon", list)
#
#     def test_assertIs(self):
#         inf = float('inf')
#         self.assertIs(inf, inf)
#
#     def test_assertIsNot(self):
#         self.assertIsNot([1, 2, 3], [1, 2, 3])
#
#     def test_assertRaises(self):
#         with self.assertRaises(ZeroDivisionError):
#             _ = 42 / 0
#
#     def test_assertRaisesRegex(self):
#         def weird_square_root(x):
#             if x < 0:
#                 raise ValueError("Number must be positive, not negative")
#             return math.sqrt(x)
#
#         with self.assertRaisesRegex(ValueError, "positive"):
#             weird_square_root(-9)
#
#     def test_assertWarns(self):
#         with self.assertWarns(UserWarning):
#             warnings.warn("Aliens detected!", UserWarning)
#
#     def test_assertWarnsRegex(self):
#         with self.assertWarnsRegex(DeprecationWarning, "expired"):
#             warnings.warn("This feature expired yesterday!", DeprecationWarning)
#
#     def test_assertAlmostEqual(self):
#         self.assertAlmostEqual(3.141592, math.pi, places=5)
#
#     def test_assertNotAlmostEqual(self):
#         self.assertNotAlmostEqual(math.sqrt(2), 1.41, places=4)
#
#     def test_assertGreater(self):
#         self.assertGreater((2 + math.sqrt(5) / 2), math.e)
#
#     def test_assertGreaterEqual(self):
#         self.assertGreaterEqual(365, 365)
#
#     def test_assertLess(self):
#         self.assertLess(0.1e-9, 6.96e8)
#
#     def test_assertLessEqual(self):
#         self.assertLessEqual(0, 0)
#
#     def test_assertRegex(self):
#         self.assertRegex("abc123xyz", r"\d+")
#
#     def test_assertNotRegex(self):
#         self.assertNotRegex("spaceship", r"^\d+$")
#
#     def test_assertCountEqual(self):
#         self.assertCountEqual("cinema", "iceman")


import unittest

users_db = []


def register(name, surname, username, email, password, confirmpassword):
    if not name or not username:
        raise ValueError("Name va username bo‘sh bo‘lishi mumkin emas!")

    for u in users_db:
        if u["email"] == email:
            raise ValueError("Email allaqachon mavjud!")

    if len(password) < 6:
        raise ValueError("Parol kamida 6 belgidan iborat bo‘lishi kerak!")

    if password != confirmpassword:
        raise ValueError("Parol va tasdiqlash paroli mos emas!")

    user = {"name": name, "surname": surname, "username": username,
            "email": email, "password": password}
    users_db.append(user)
    return user


def login(username_or_email, password):
    for u in users_db:
        if u["username"] == username_or_email or u["email"] == username_or_email:
            if u["password"] == password:
                return True
            else:
                raise ValueError("Parol noto‘g‘ri!")
    raise ValueError("Foydalanuvchi topilmadi!")


class TestAuthSystem(unittest.TestCase):

    def setUp(self):
        users_db.clear()

    def test_register_name_and_username_not_empty(self):
        with self.assertRaises(ValueError):
            register("", "Murodullayev", "", "ogabek@mail.ru", "ogabeks45", "ogabeks45")

    def test_register_email_unique(self):
        register("Og'abek", "Murodullayev", "ogabek_murodullayev",
                 "ogabek@mail.ru", "ogabeks45", "ogabeks45")
        with self.assertRaises(ValueError):
            register("Og'abek", "Murodullayev", "ogabek_murodullayev2",
                     "ogabek@mail.ru", "anotherpass", "anotherpass")

    def test_register_password_length(self):
        with self.assertRaises(ValueError):
            register("Og'abek", "Murodullayev", "ogabek_shortpass",
                     "short@mail.ru", "123", "123")

    def test_register_password_match(self):
        with self.assertRaises(ValueError):
            register("Og'abek", "Murodullayev", "ogabek_diffpass",
                     "diff@mail.ru", "ogabeks45", "different")

    def test_login_username_exists(self):
        register("Og'abek", "Murodullayev", "ogabek_murodullayev",
                 "ogabek@mail.ru", "ogabeks45", "ogabeks45")
        self.assertTrue(login("ogabek_murodullayev", "ogabeks45"))

    def test_login_password_correct(self):
        register("Og'abek", "Murodullayev", "ogabek_murodullayev",
                 "ogabek@mail.ru", "ogabeks45", "ogabeks45")
        with self.assertRaises(ValueError):
            login("ogabek_murodullayev", "wrongpass")