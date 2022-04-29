import unittest
from repo import *
import shutil

class TestRepo(unittest.TestCase):
    newRepoPath = "./tests/garbage"

    def test_repo_create(self):
        """
        creating a repo
        """
        shutil.rmtree(self.newRepoPath)
        repo_create(self.newRepoPath)

        if os.path.exists(f'{self.newRepoPath}/.git'):
            shutil.rmtree(self.newRepoPath)
            return True
        else:
            raise "Git repo wasn't created"
    
    def test_repo_default_config(self):
        """
        if repo default config was created succesfully
        """
        repo_create(self.newRepoPath)

        defaultConfig = configparser.ConfigParser()
        defaultConfig.read(f'/../{defaultConfigName}')

        newConfig = configparser.ConfigParser()
        newConfig.read(f'{self.newRepoPath}/.git/config')

        

        for i, section in enumerate(defaultConfig.sections()):
            newConfigSections = newConfig.sections()
            newConfigCurrentSection = newConfigSections[i]
            self.assertEqual(section, newConfigCurrentSection, "Checking default and the created config right after creating the repo")
            for index, (key, val) in enumerate(defaultConfig.items(section)):
                self.assertEqual(newConfig.items(newConfigCurrentSection)[index][key], val)
        
        shutil.rmtree(self.newRepoPath)


        
if __name__ == "__main__":
    unittest.main()