import unittest

from api_response import get_github_api_root, get_github_meta_information, get_octocat, get_all_api_versions, \
    get_the_zen_of_github


class TestGitHubAPI(unittest.TestCase):
    def test_get_github_api_root(self):
        data = get_github_api_root()
        self.assertIsInstance(data, dict)
        self.assertIn('current_user_url', data)
        self.assertEqual(data['current_user_url'], 'https://api.github.com/user')

    def test_get_github_meta_information(self):
        data = get_github_meta_information()
        self.assertIsInstance(data, dict)
        self.assertIn('ssh_key_fingerprints', data)

    def test_get_octocat(self):
        data = get_octocat()
        self.assertIsInstance(data, str)

    def test_get_all_api_versions(self):
        data = get_all_api_versions()
        self.assertIsInstance(data, list)
        self.assertIn("2022-11-28", data)

    def test_get_the_zen_of_github(self):
        data = get_the_zen_of_github()
        self.assertIsInstance(data, str)


if __name__ == '__main__':
    unittest.main()
